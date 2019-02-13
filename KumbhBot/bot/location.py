import requests
from googletrans import Translator
from typing import Any, Dict, List
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os



def restaurant(bot_handler: Any)->str:
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
	response = requests.get(current_location_url + place + ',+CA&key=<YOUR API KEY> ')
	res1 = response.json()
	longi = res1["results"][0]["geometry"]["location"]["lat"]
	lati = res1["results"][0]["geometry"]["location"]["lng"]
	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=restaurant'
	response2 = requests.get(temp)
	res2 = response2.json()
	#print(res2)
	i = 0
	c = 0
	ans=""
	translated=""
	for i in res2['results']:
	    name = i['name']
	    ans += name
	    ans += "\n"
	    tranlate1=translator.translate(name,dest="hi")
	    translate1=tranlate1.text
	    vicinity = i['vicinity']
	    ans += vicinity + "\n\n"
	    tranlate2=translator.translate(vicinity,dest="hi")
	    translate2=tranlate2.text
	    translated+=translate1+"\n"+translate2+"\n\n"
		

	if ans == "":
	    ans = "No results"

	ans+=translated+"\n"
	return ans
	
def hotel(bot_handler: Any)->str:
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
	response = requests.get(current_location_url + place + ',+CA&key=<YOUR API KEY>')
	res1 = response.json()
	longi = res1["results"][0]["geometry"]["location"]["lat"]
	lati = res1["results"][0]["geometry"]["location"]["lng"]
	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=lodging'
	response2 = requests.get(temp)
	res2 = response2.json()
	#print(res2)
	i = 0
	c = 0
	ans=""
	translated=""
	for i in res2['results']:
	    name = i['name']
	    ans += name
	    ans += "\n"
	    translat1=translator.translate(name,dest="hi")
	    translate1=translat1.text
	    vicinity = i['vicinity']
	    ans += vicinity + "\n\n"
	    ranslate2=translator.translate(vicinity,dest="hi")
	    translate2=ranslate2.text
	    translated+=translate1+"\n"+translate2+"\n\n"
	    
		

	if ans == "":
	    ans = "No results"

	ans+="\n"+translated
	return ans

