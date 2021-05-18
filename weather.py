import urllib.request as req
import speech 
import time
import datetime
import json
import sys
from PIL import Image

speech.say("おはようございます。","ja-JP",0.5) 	

dt_now = datetime.datetime.now()

hour=dt_now.hour
minute=dt_now.minute
str1="ただいまの時刻は{}時{}分です。".format(hour,minute)

		
speech.say(str1,"ja-JP",0.5) 
	

url = 'https://weather.tsukumijima.net/api/forecast?city=130010'
filename = 'tenki.json'
req.urlretrieve(url, filename)

json_open = open('tenki.json' , 'r', encoding = 'utf-8')
api_data1 = json.load(json_open)
info1 = api_data1['forecasts'][0]['detail']['weather']
tmp_max=api_data1['forecasts'][0]['temperature']['max']['celsius']

data1 = api_data1['forecasts'][0]['telop']


if "雨" in data1:
	rainy=Image.open('rainy.PNG')
	rainy.show()

elif "晴" in data1:
	sunny=Image.open('sunny.PNG')
	sunny.show()
	
elif "雪" in data1:
	snowy=Image.open('snowy.PNG')
	snowy.show()
	
else:
	cloudy=Image.open('cloudy.PNG')
	cloudy.show()


i = '一時'
j = '所により'
if i in info1:
		info1 = info1.replace('一時', 'ときどき')
if j in info1: 
		info1 = info1.replace('所により', 'ところにより')
	
print('今日の天気は' + info1)
print('今日の最高気温は' + tmp_max + '度です。')
tokyo_w="今日の東京の天気は{}".format(info1)
tokyo_t="最高気温は{}度です。".format(tmp_max)
speech.say(tokyo_w ,"ja-JP",0.5)
time.sleep(0.3)
speech.say(tokyo_t, "ja-JP",0.5)
time.sleep(0.3)

info2 = api_data1['forecasts'][0]['telop']

if "雨" in info1 or "雨" in info2:
	speech.say("傘が必要です。","ja-JP",0.5)

