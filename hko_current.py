import requests
import os
import os.path
import urllib
import json
import re
#import datetime
from datetime import datetime
from datetime import timedelta

from bs4 import BeautifulSoup

def getPage(url):
	print ("Fetching data")
	result = requests.get(url)
	c = result.content
	c = BeautifulSoup(c, "html.parser")
	return c

#Set the Source of our data to Hong Kong Observatory
page = getPage("http://www.weather.gov.hk/wxinfo/ts/text_readings_e.htm") #Reginal Weather english version

#Grab Content from the page
content = page.body
content = content.find_all('pre')
content = content[0].contents[0] 
#print(content)

#Grab the latest recorded date, saving into lastUpdateDatetime some value like: "14:10 Hong Kong Time 27 December 2017"
searchResult = re.search('Latest readings recorded at (\d{2}:\d{2} Hong Kong Time \d{2} \w+ \d{4})', content)
lastUpdateDatetime = searchResult.group(1)
#print(lastUpdateDatetime)

#Grab the protion that contains all stations data for temperature, and humidity, removing anything below
data = re.sub(r"[\w\W]+\(degree Celsius\)\n*","",content) #remove the decoration before useful data
data = re.search('([\w\W\s]*)10-Minute Mean Wind Direction, Speed and Maximum Gust \(km/hour\)', data)
data = data.group(1)
#print(data)

pattern = re.compile(r'([a-zA-Z \']+)[\s]+(N/A|[\d.]+\*?)[\s]+(N/A|[\d.]+\*?)[\s]+(N/A|[\d.]+)[\*?\s]+/[\s]+(N/A|[\d.]+)\*?')
stationNameArray = []
airTempArray = []
humidityArray = []
maxTempArray = []
minTempArray = []
for (stationName, airTemp, humidity, maxTemp, minTemp) in re.findall(pattern, data):
	stationNameArray.append(stationName.strip())
	airTempArray.append(airTemp)
	humidityArray.append(humidity)
	maxTempArray.append(maxTemp)
	minTempArray.append(minTemp)

jsonResult = json.dumps([{'stn' : stnDesc, 'airTemp' : airTemp, 'humidity' : humidity, 'maxTemp': maxTemp, 'minTemp': minTemp} for stnDesc, airTemp, humidity, maxTemp, minTemp in zip(stationNameArray, airTempArray, humidityArray, maxTempArray, minTempArray)])
print(jsonResult)


