import sys, os, zulip
sys.path.insert(0,os.getcwd())

from wit import Wit
from typing import Any, Dict

from twilio.rest import Client

def makeCall(bot_handler: Any) -> str:
	TWILIO_PHONE_NUMBER = "<AUTHORITY's PHONE NUMBER>"
	TWIML_INSTRUCTIONS_URL = "http://static.fullstackpython.com/phone-calls-python.xml"
	client = Client("ACf5b930654138baf8e316f85ef29b5867", "cbb5df96000281b64b3ad55c19c0cdad")

	numbers_list=["+917347824123",]
	for number in numbers_list:
        	print("Dialing " + number)
        	client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")
	return "Phone call made successfully"

