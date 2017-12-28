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

def get9dayJson():
	#Set the Source of our data to Hong Kong Observatory
	page = getPage("http://www.hko.gov.hk/wxinfo/currwx/fnd.htm") #english version

	todayDesc = re.sub(r"Last revision date: <","", page.find(id="last_modify_date").get_text())
	todayDesc = re.sub(r">[\s]*","",todayDesc)
	todayDesc = re.sub(r" ","-",todayDesc)
	todayObj = datetime.strptime(todayDesc, "%d-%b-%Y")

	date_desc_array = page.find(id="fnd").tr.find_all("td")

	forcast_desc_array = page.find(id="forecast_desc").find_all("div")
	for i in range(len(forcast_desc_array)):
		temp = (forcast_desc_array[i].get_text())
		temp = re.sub(r"\r\n\t", "" , temp )
		temp = re.sub(r"\t", "" , temp )
		forcast_desc_array[i] = temp
        
		#create formatted date and store in array
		temp = todayObj + timedelta(days=i)
		temp = temp.strftime("%d-%m-%Y")
		date_desc_array[i] = temp

#	jsonResult= json.dumps( [{'dateDesc': dateDesc, 'forcast' : forcast} for dateDesc, forcast in zip(date_desc_array, forcast_desc_array)] )
	jsonResult= json.dumps({
		'today' : todayDesc, 
		'forcastData' : [{'dateDesc': dateDesc, 'forcast' : forcast} for dateDesc, forcast in zip(date_desc_array, forcast_desc_array)]
	})
	return jsonResult
