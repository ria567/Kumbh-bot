
import requests
from translate import Translator
from typing import Any, Dict, List
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os



def hospital(bot_handler: Any)->str:
	current_location_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=<ENTER GOOGLE PLACE API KEY> &location='
	translator= Translator(to_lang="hi")
	current_location="  Triveni Sangam Allahabad"
	place = ""
	l = len(current_location)
	i=2
	while (i < l):
	    place += current_location[i] + " "
	    i = i + 1
	#print(place)
	r = requests.get(current_location_url + place + ',+CA&key="Your API KEY"')
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
	    temp = name
	    temp += "\n"    
	    vicinity = i['vicinity']
	    temp += vicinity   
	    temp += "\n\n"
	    ans += temp
	    #int_trans = translator.translate(temp)
	    #translated += int_trans


	if ans == "":
	    ans = "No results"
	    #translated = translator.translate(ans)
	#ans += translated
	return ans
    
def contacts(bot_handler: Any)->str:

	emergency_url="https://kumbh.gov.in/en/emergency-services"
	uClient=uReq(my_url)
	page_html=uClient.read()
	uClient.close()
	translator= Translator(to_lang="hi")

	page_soup=soup(page_html,"html.parser")
	containers=page_soup.findAll("div",{"class":"align-left"})
	container=containers[2]
	p=container.text
	ans = os.linesep.join([s for s in p.splitlines() if s])
	#print(ans)
	#container=containers[0]

	#ans=container.text
	#translated=translator.translate(ans)
	return ans


def police(bot_handler: Any)->str:
	current_location_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4&location='
	translator= Translator(to_lang="hi")
	current_location="  Triveni Sangam Allahabad"
	place = ""
	l = len(current_location)
	i=2
	while (i < l):
		place += current_location[i] + " "
		i = i + 1

	response = requests.get(current_location_url + place + ',+CA&key="YOUR API KEY"')
	res1 = response.json()

	longi = res1["results"][0]["geometry"]["location"]["lat"]
	lati = res1["results"][0]["geometry"]["location"]["lng"]

	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=police'
	response2 = requests.get(temp)
	res2 = response2.json()

	i = 0
	c = 0
	ans=""
	for i in res2['results']:
		name = i['name']
		ans += name
		ans += "\n"
		vicinity = i['vicinity']
		ans += vicinity + "\n\n"

	if ans == "":
		ans = "No results"

	#translated=translator.translate(ans)
	return ans	
def restaurant(bot_handler: Any)->str:
	current_location_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	search_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyDJNoEuLGP2o2PYnRWOx29AvA0kOGQJZO4&location='
	translator= Translator(to_lang="hi")
	current_location="  Triveni Sangam Allahabad"
	place = ""
	l = len(current_location)
	i=2
	while (i < l):
	    place += content[i] + " "
	    i = i + 1
	response = requests.get(url + place + ',+CA&key="YOUR API KEY"')
	res1 = response.json()
	longi = res1["results"][0]["geometry"]["location"]["lat"]
	lati = res1["results"][0]["geometry"]["location"]["lng"]
	temp = search_url + str(longi) + ',' + str(lati) + '&rankby=distance&types=restaurant'
	response2 = requests.get(temp)
	res2 = response2.json()
	print(results2)
	i = 0
	c = 0
	ans=""
	for i in res2['results']:
	    name = i['name']
	    ans += name
	    ans += "\n"
	    #opening_hours = i['opening_hours']
	    #rating = str(i['rating'])
	    vicinity = i['vicinity']
	    ans += vicinity + "\n"
	    #rating = str(i['reviews'])    
	    #ans += rating
	    ans += "\n\n"
	    
		

	if ans == "":
	    ans = "No results"

	#translated=translator.translate(ans)
	return ans

