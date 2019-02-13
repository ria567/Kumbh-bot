from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from googletrans import Translator
from typing import Any

def forecast_weather(bot_handler: Any)->str:
	my_url="https://www.weather-forecast.com/locations/Allahabad/forecasts/latest"
	uClient=uReq(my_url)
	page_html=uClient.read()
	uClient.close()
	translator= Translator()

	page_soup=soup(page_html,"html.parser")

	containers=page_soup.findAll("p",{"class":"b-forecast__table-description-content"})
	content=containers[0]
	final = content.text

	translate=translator.translate(final,dest="hi")
	translated=translate.text
	return (final + "\n" +translated)
