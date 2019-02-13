
import requests
from googletrans import Translator
from typing import Any, Dict, List
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os



def hospital(bot_handler: Any)->str:
	current_location_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=<YOUR API KEY>&location='
	translator= Translator()
	current_location="  Triveni Sangam Allahabad"
	place = ""
	l = len(current_location)
	i=2
	while (i < l):
	    place += current_location[i] + " "
	    i = i + 1
	#print(place)
	r = requests.get(current_location_url + place + ',+CA&key=<YOUR API KEY>')
	results = r.json()
	#print(results)
	longi = results["results"][0]["geometry"]["location"]["lat"]
	lati = results["results"][0]["geometry"]["location"]["lng"]

	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=hospital'
	response = requests.get(temp)
	result = response.json()
	#print(result)
	i = 0
	ans=""
	translated=""
	for i in result['results']:
	    name = i['name']
	    ans	+= name
	    ans += "\n"    
	    tran1=translator.translate(name,dest="hi")
	    trans1=tran1.text
	    vicinity = i['vicinity']
	    ans += vicinity   
	    ans += "\n\n"
	    tran2 = translator.translate(vicinity,dest="hi")
	    trans2=tran2.text
	    translated += trans1+"\n"+trans2+"\n\n"


	if ans == "":
	    ans = "No results"
	ans =ans+"\n"+ translated
	return ans
    
def contacts(bot_handler: Any)->str:

	emergency_url="https://kumbh.gov.in/en/emergency-services"
	uClient=uReq(emergency_url)
	page_html=uClient.read()
	uClient.close()
	translator= Translator()

	page_soup=soup(page_html,"html.parser")
	containers=page_soup.findAll("div",{"class":"align-left"})
	container=containers[2]
	p=container.text
	ans = os.linesep.join([s for s in p.splitlines() if s])
	
	translated="कुम्भ हेल्पलाइन नम्बर - 1920 \n महिला और बाल हेल्पलाइन- 1091 \n रोगी वाहन- 108 \n पुलिस- 100 \n  आग- 101"
	return ans+"\n"+translated


def police(bot_handler: Any)->str:
	current_location_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4&location='
	translator= Translator()
	current_location="  Triveni Sangam Allahabad"
	place = ""
	l = len(current_location)
	i=2
	while (i < l):
		place += current_location[i] + " "
		i = i + 1

	response = requests.get(current_location_url + place + ',+CA&key=<YOUR API KEY>')
	res1 = response.json()

	longi = res1["results"][0]["geometry"]["location"]["lat"]
	lati = res1["results"][0]["geometry"]["location"]["lng"]

	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=police'
	response2 = requests.get(temp)
	res2 = response2.json()

	i = 0
	c = 0
	ans=""
	translated=""
	for i in res2['results']:
		name = i['name']
		ans += name
		ans += "\n"
		tran1=translator.translate(name,dest="hi")
		trans1=tran1.text
		vicinity = i['vicinity']
		ans += vicinity + "\n\n"
		tran2=translator.translate(vicinity,dest="hi")
		trans2=tran2.text
		translated+=trans1+"\n"+trans2+"\n\n"
	if ans == "":
		ans = "No results"
		
	ans=ans+"\n"+translated
	return ans	

