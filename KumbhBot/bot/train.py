import sys, os, zulip
sys.path.insert(0,os.getcwd())
import codecs
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from googletrans import Translator 
import json
from typing import Any,List,Dict
import datetime
from dateutil.relativedelta import relativedelta
translator= Translator()
def live_station(bot_handler: Any, *params ) -> str:
	#content = message["content"]
	#words = content.split()
	api_key="<YOUR API KEY>" 
	
	train_number=params[0]
	station_code="ALD"
	print(type(params))
	print("train Number : " + str(train_number))
	string = ''.join(params)
	print("string : " + string)
	one_year_from_now = datetime.datetime.now() + relativedelta(years=1)
	current_date = datetime.datetime.now().strftime("%d-%m-%Y")
	#print(current_date)
	base_url = "https://api.railwayapi.com/v2/live/train/"+train_number+"/station/"+station_code+"/date/"+current_date+"/apikey/"+api_key+"/"
	j=uReq(base_url)
	#print(base_url)
	
	reader = codecs.getreader("utf-8")
	data = json.load(reader(j))
	x=data['status']
	ans=""
	ans1 = "Scheduled departure:" + x['schdep'] + "\n" 
	ans2 = "Actual Arrival:"+ x['actarr'] + "\n"
	ans3 = "Scheduled arrival:" +x['scharr'] +"\n" 
	ans4 = "Actual arrival:" +x['actarr'] + "\n"
	translate1=translator.translate(ans1,dest="hi")
	translate2=translator.translate(ans2,dest="hi")
	translate3=translator.translate(ans3,dest="hi")
	translate4=translator.translate(ans4,dest="hi")
	translate5=translator.translate(data['position'],dest="hi")
	translated1=translate1.text
	translated2=translate2.text
	translated3=translate3.text
	translated4=translate4.text
	translated5=translate5.text
	final_translated = translated1 + "\n" + translated2 + "\n" + translated3 + "\n" + translated4 + "\n" + translated5 + "\n" 
	ans= ans1 + "\n" + ans2 + "\n" + ans3 +"\n" + ans4 +"\n" + data['position']+"\n"
	if ans=='':
		final_ans ="Sorry no results found"
	else:
		final_ans= ans + "\n" + final_translated
	return final_ans


#https://api.railwayapi.com/v2/live/train/<train-number>/station/<station-code>/date/<dd-mm-yyyy>/apikey/<apikey>/
def train_route( bot_handler: Any, *params) -> str:
	
	api_key="<YOUR API KEY>" 
	train_number=params[0]
	train_n=''.join(params)
	print("Train number= " + train_n)
	base_url = "https://api.railwayapi.com/v2/route/train/"+train_n+"/apikey/"+api_key+"/"
	j=uReq(base_url)
	print(base_url)
	reader = codecs.getreader("utf-8")
	
	data = json.load(reader(j))
	ans=""
	for station in data['route']:
            s=station['station']	
            ans+=s['name']+"\t"+station['schdep']+"\t"+station['scharr']+"\n"
	translate=translator.translate(ans,dest="hi")
	translated=translate.text
	ans+=(translated + "\n")
	return ans


	

#https://api.railwayapi.com/v2/route/train/<train number>/apikey/<apikey>/

def train_between(bot_handler: Any,*params) -> str:
    
    api_key="<YOUR API KEY>"
    #station = ''.join(params)
    print(params)
    source=params[0][0]
    dest=params[0][1]
    print("Source and destination: " + source + " " + dest) 
    one_year_from_now = datetime.datetime.now() + relativedelta(years=1)
    current_date = one_year_from_now.strftime("%d-%m-%Y")
    base_url = "https://api.railwayapi.com/v2/between/source/"+source+"/dest/"+dest+"/date/"+current_date+"/apikey/"+api_key+"/"
    j=uReq(base_url)
    reader=codecs.getreader("utf-8")
    data = json.load(reader(j))
    print(base_url)
    ans=""
    trains=data['trains']
    for train in trains:
        ans += "Train Number:" + train['number'] + "\nTrain Name:" + train['name'] + "\nTravel Time:" + train['travel_time'] + "\nDeparture time at source station" + train['src_departure_time'] + "\nArrival time at destination station:" + train['dest_arrival_time'] + "\n"
        for day in train['days']:
            ans += day['code'] + "     "
        ans += "\n"
        for day in train['days']:
            ans += day['runs'] + "     "
        
        ans+="\n\n"
            

    translate=translator.translate(ans,dest="hi")
    translated=translate.text
    ans+=(translated + "\n")
    return ans


#https://api.railwayapi.com/v2/between/source/<stn code>/dest/<stn code>/date/<dd-mm-yyyy>/apikey/<apikey>/


def train_enquiry(bot_handler:Any,*params) -> str:

	station_code=params[0][0]
	api_key="01grdocl45" 
	station_hour=str(4)
	base_url = "https://api.railwayapi.com/v2/arrivals/station/"+station_code+"/hours/"+station_hour+"/apikey/"+api_key+"/"
	
	j=uReq(base_url)
	reader = codecs.getreader("utf-8")
	data = json.load(reader(j))

	trains=data['trains']
	ans=""
	for train in trains:
    		ans+="Train number:" + train['number'] +"\n Train name:" + train['name'] +"\nScheduled arrival:"+train['scharr']+"\nExpected 			arrival:"+train['actarr']+"\nScheduled departure:" + train['schdep']+"\nActual departure:"+train['actdep']+"\n\n" 
	translate=translator.translate(ans,dest="hi")
	translated=translate.text
	ans+=(translated + "\n")
	return ans




