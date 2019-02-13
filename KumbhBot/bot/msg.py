import sys, os
sys.path.insert(0,os.getcwd())

import time 
from typing import Any
from time import sleep 
from sinchsms import SinchSMS 
import requests
import json
from urllib.request import urlopen,Request
def sendSMS(bot_handler: Any,*paraargs) -> str: 
  
    
    number = paraargs[0][0]
    app_key = '<YOUR API KEY>'
    app_secret = '<YOUR API SECRET>'
    #we are having a lot of bots so send the number of any bot.
    message ="Message sent by a user from bot 1"
    client = SinchSMS(app_key, app_secret) 
    print("Sending '%s' to %s" % (message, number)) 
    
    
    response = client.send_message(number, message) 
    message_id = response['messageId'] 
    response = client.check_status(message_id) 
  
    while response['status'] != 'Successful': 
        print(response['status']) 
        time.sleep(1) 
        response = client.check_status(message_id) 
  
    print(response['status']) 
  
if __name__ == "__main__": 
    sendSMS() 
