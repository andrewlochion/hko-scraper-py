#hko-scraper-py

hko-scraper-py is an open source project to scrape useful data from Hong Kong Observatory. 

Hong Kong Observatory provides useful weather data in HTML, and RSS. However, it does not provide the data in JSON format, which is widely used for data transfer in mobile apps, and website.

The script runs on both python 2 and python 3. This project uses BeautifulSoup library to scrape webpage from Hong Kong Observatory, and uses regular expression to extract data. 


##hko_current.py

to execute the script, simply use 
```bash
$python hko_current.py
```
This script scrapes data from [Hong Kong Observatory] (http://www.hko.gov.hk/textonly/v2/forecast/text_readings_e.htm), and return json format for the following: air temperature in Celsius, maximum temperature, minimum temperature, hudimity


###Example data
```perl
[
{"stn": "Chek Lap Kok", "airTemp": "22.4", "humidity": "39", "maxTemp": "23.3", "minTemp": "16.6"}, 
{"stn": "Cheung Chau", "airTemp": "18.8", "humidity": "62", "maxTemp": "20.9", "minTemp": "15.6"}, 
{"stn": "Happy Valley", "airTemp": "20.9", "humidity": "N/A", "maxTemp": "21.3", "minTemp": "16.2"}, 
{"stn": "HK Observatory", "airTemp": "18.9", "humidity": "65", "maxTemp": "19.4", "minTemp": "16.2"}, 
{"stn": "HK Park", "airTemp": "19.6", "humidity": "N/A", "maxTemp": "20.7", "minTemp": "16.2"}, 
{"stn": "Kai Tak Runway Park", "airTemp": "18.9", "humidity": "N/A", "maxTemp": "20.0", "minTemp": "16.6"},
{"stn": "Kau Sai Chau", "airTemp": "19.2", "humidity": "59", "maxTemp": "20.7", "minTemp": "14.5"}, 
{"stn": "King's Park", "airTemp": "19.9", "humidity": "56", "maxTemp": "20.8", "minTemp": "16.1"}, 
{"stn": "Kowloon City", "airTemp": "22.0", "humidity": "N/A", "maxTemp": "22.1", "minTemp": "15.6"}, 
{"stn": "Kwun Tong", "airTemp": "18.7", "humidity": "N/A", "maxTemp": "19.5", "minTemp": "15.5"}, 
{"stn": "Lau Fau Shan", "airTemp": "23.4", "humidity": "46", "maxTemp": "23.7", "minTemp": "13.7"}, 
{"stn": "Ngong Ping", "airTemp": "16.4", "humidity": "N/A", "maxTemp": "17.3", "minTemp": "11.1"}, 
{"stn": "Pak Tam Chung", "airTemp": "19.8", "humidity": "N/A", "maxTemp": "21.2", "minTemp": "12.4"}, 
{"stn": "Peng Chau", "airTemp": "N/A", "humidity": "N/A", "maxTemp": "19.6", "minTemp": "16.1"}, 
{"stn": "Sai Kung", "airTemp": "18.2", "humidity": "69", "maxTemp": "19.2", "minTemp": "16.0"}, 
{"stn": "Sha Tin", "airTemp": "20.7", "humidity": "57", "maxTemp": "21.5", "minTemp": "15.9"}, 
{"stn": "Sham Shui Po", "airTemp": "21.7", "humidity": "N/A", "maxTemp": "22.9", "minTemp": "16.3"}, 
{"stn": "Shau Kei Wan", "airTemp": "18.0", "humidity": "N/A", "maxTemp": "19.3", "minTemp": "15.8"}, 
{"stn": "Shek Kong", "airTemp": "22.2", "humidity": "45", "maxTemp": "22.5", "minTemp": "15.9"}, 
{"stn": "Sheung Shui", "airTemp": "22.1", "humidity": "50", "maxTemp": "22.9", "minTemp": "15.1"}, 
{"stn": "Stanley", "airTemp": "17.7", "humidity": "N/A", "maxTemp": "19.2", "minTemp": "16.0"}, 
{"stn": "Ta Kwu Ling", "airTemp": "22.2", "humidity": "41", "maxTemp": "23.3", "minTemp": "13.8"}, 
{"stn": "Tai Mei Tuk", "airTemp": "19.9", "humidity": "N/A", "maxTemp": "21.3", "minTemp": "14.9"}, 
{"stn": "Tai Mo Shan", "airTemp": "13.4", "humidity": "N/A", "maxTemp": "15.1", "minTemp": "8.2"}, 
{"stn": "Tai Po", "airTemp": "19.7", "humidity": "64", "maxTemp": "20.7", "minTemp": "16.4"}, 
{"stn": "Tate's Cairn", "airTemp": "13.3", "humidity": "N/A", "maxTemp": "14.4", "minTemp": "10.5"}, 
{"stn": "The Peak", "airTemp": "16.9", "humidity": "N/A", "maxTemp": "17.4", "minTemp": "12.7"}, 
{"stn": "Tseung Kwan O", "airTemp": "19.8", "humidity": "61", "maxTemp": "21.0", "minTemp": "15.7"}, 
{"stn": "Tsing Yi", "airTemp": "21.9", "humidity": "40", "maxTemp": "22.0", "minTemp": "16.4"}, 
{"stn": "Tsuen Wan Ho Koon", "airTemp": "22.2", "humidity": "47", "maxTemp": "22.6", "minTemp": "14.1"}, 
{"stn": "Tsuen Wan Shing Mun Valley", "airTemp": "22.4", "humidity": "47", "maxTemp": "23.1", "minTemp": "15.6"}, 
{"stn": "Tuen Mun", "airTemp": "21.3", "humidity": "50", "maxTemp": "24.1", "minTemp": "14.5"}, 
{"stn": "Waglan Island", "airTemp": "N/A", "humidity": "N/A", "maxTemp": "N/A", "minTemp": "N/A"}, 
{"stn": "Wetland Park", "airTemp": "22.1", "humidity": "40", "maxTemp": "22.3", "minTemp": "13.3"}, 
{"stn": "Wong Chuk Hang", "airTemp": "20.7", "humidity": "47", "maxTemp": "21.4", "minTemp": "16.1"}, 
{"stn": "Wong Tai Sin", "airTemp": "20.5", "humidity": "N/A", "maxTemp": "21.6", "minTemp": "15.9"}, 
{"stn": "Yuen Long Park", "airTemp": "23.1", "humidity": "N/A", "maxTemp": "23.5", "minTemp": "14.4"}
]
```
##hko_9day.py
to execute the script, simply use 
```bash
$python hko_9day.py
```
This script scrapes data from [Hong Kong Observatory] (http://www.hko.gov.hk/wxinfo/currwx/fnd.htm), and return json format for the following: Date, forcast
```perl
[
  {"forcast": "Cloudy. One or two light rain patches later.", "dateDesc": "27-12-2017"}, 
  {"forcast": "Mainly fine.", "dateDesc": "28-12-2017"}, 
  {"forcast": "Mainly fine.", "dateDesc": "29-12-2017"}, 
  {"forcast": "Fine and dry. Cool in the morning.", "dateDesc": "30-12-2017"}, 
  {"forcast": "Mainly fine. Cool in the morning. Dry during the day.", "dateDesc": "31-12-2017"}, 
  {"forcast": "Sunny periods.", "dateDesc": "01-01-2018"}, 
  {"forcast": "Sunny intervals.", "dateDesc": "02-01-2018"}, 
  {"forcast": "Mainly cloudy with sunny intervals.", "dateDesc": "03-01-2018"}, 
  {"forcast": "Cloudy. Cool in the morning.", "dateDesc": "04-01-2018"}
]
```


This project is intended for personal use and educational purpose, I am not liable for any misuse of the scripts. 
