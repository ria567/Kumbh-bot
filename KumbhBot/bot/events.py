

import sys
import os
sys.path.insert(0, os.getcwd())

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from googletrans import Translator
import requests
import json
from typing import Any, Dict, List

def bath(bot_handler: Any)->str:
    my_url="https://www.tourmyindia.com/kumbhmela/bathing-dates.html"
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    translator= Translator()

    page_soup=soup(page_html,"html.parser")
    containers=page_soup.findAll("div",{"class":"dates-details"})
    #print(len(containers))

    ans=""
    int_trans=""
    translated=""
    occ_containers=containers[0].findAll("span",{"class":"kumbh-details"})
    date_containers=containers[0].findAll("span",{"class":"kumbh-details-date"})
    zipped=zip(occ_containers,date_containers)
    for a,b in zipped:
        occ=a.text
        date=b.text
        final = occ + "-" + date
        trans = translator.translate(final,dest="hi")
        int_trans=trans.text
        translated += int_trans + "\n"
        ans += final + "\n" 
    
    ans += translated
    return ans
    
    
