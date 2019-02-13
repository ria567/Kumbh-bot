

import sys, os, zulip
sys.path.insert(0,os.getcwd())



from wit import Wit
from typing import Any, Dict

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from googletrans import Translator

def getHeadline(bot_handler: Any)->str:
	news_url="https://news.google.com/news/rss"
	Client=urlopen(news_url)
	xml_page=Client.read()
	Client.close()
	translator= Translator()
	soup_page=soup(xml_page,"xml")
	news_list=soup_page.findAll("item")
	ans=""
	trans=""
	for news in news_list:
		title=news.title.text
		link=news.link.text
		pubDate=news.pubDate.text
		tran_title=translator.translate(title,dest="hi")
		trans_title=tran_title.text
		tran_link=translator.translate(link,dest="hi")
		trans_link=tran_link.text
		tran_pubDate=translator.translate(pubDate,dest="hi")
		trans_pubDate=tran_pubDate.text
		ans+=title+"\n"+link+"\n"+pubDate+"\n"
		trans+=trans_title+"\n"+trans_link+"\n"+trans_pubDate+"\n"
	      
		

	final=ans+"\n"+trans
	return final
		
		
		
		
		
		
		
		
