import sys, os, zulip
sys.path.insert(0,os.getcwd())

from wit import Wit
from typing import Any, Dict
from googletrans import Translator
translator=Translator()
client = Wit('Ci5mwK5Ip8uOJ1Kk1ce3QGgFdJMHH4iP')
import events,emergency,train,weather,lost,playSong,location,news,msg,help,phone
class KumbhBot(object):
    def usage(self):
        return "Build withZulip chat api and python, KumbhBot works as a savior for people visiting The Popular Ritual People Gathering KUMBH"
    def handle_message(self,message: Dict[str,str],bot_handler:Any) -> None:
        ans=[]
        question=""
        print(message["content"])
        #if message["content"] == "" or message["content"] == "help":
            #ans.append(help.HELP_MESSAGE(bot_handler))
        data=message["content"].split()
        if(data[0] != "Kumbh"):
                data.insert(0,"Kumbh")
                message["content"] = "Kumbh " + message["content"]
        if len(data) >=2:
        	question = data[1]        
        print("Question here:")
        print(question)
        flag=0   
        if question == "weather":
            ans.append(weather.forecast_weather(bot_handler))
        elif question == "hello":
        	state="Hello User! Welcome to Kumbh Bot.Hope you are enjoying Kumbh\n"
        	translated=translator.translate("Hello User! Welcome to Kumbh Bot.Hope you are enjoying Kumbh\n",dest="hi")
        	
        	final_ans=state + translated.text
        	ans.append(final_ans)
        elif question == "liveStation":
                station = data[2::]
                ans.append(train.train_enquiry(bot_handler,station))
        elif question == "findRoute":
            TrainNo = data[2]
            ans.append(train.train_route(bot_handler,TrainNo))
        elif question == "trainAtAllahabad":
            trainNumber = data[2]
            print(trainNumber)
            ans.append(train.live_station(bot_handler,trainNumber))
        elif question == "bath":
            ans.append(events.bath(bot_handler))
        elif question == "hospital":
            ans.append(emergency.hospital(bot_handler))
        elif question == "restaurant":
            ans.append(location.restaurant(bot_handler))
        elif question == "emergencyContact":
            ans.append(emergency.contacts(bot_handler))
        elif question == "police":
            ans.append(emergency.police(bot_handler))
        
        elif question == "help":
            ans.append(help.HELP_MESSAGE(bot_handler))
        elif question == "trainFromTo":
            first = data[2::]
            print(first)
            
            ans.append(train.train_between(bot_handler, first))
        elif question == "lost":
        	tosend = data[2::]
        	ans.append(lost.send_email(bot_handler,tosend))
        elif question == "bhajan":
        	ans.append(playSong.bhajan(bot_handler))
        elif question == "hotel":
        	ans.append(location.hotel(bot_handler))
        elif question == "news":
        	ans.append(news.getHeadline(bot_handler))
        elif question == "iamlost":
        	first = data[2::]
        	ans.append(msg.sendSMS(bot_handler,first))
        elif question =="SOS":
        	ans.append(phone.makeCall(bot_handler))
        else:
            ans.append('Sorry :( I could not understatnd what you want to say.')
            ans.append(' Try "@Kumbh help" to get detailed help ')
            
            
        final_reply=""
        if question == "iamlost":
        	final_reply = "Sms sent successfully!!"
        
       	else:
        	for index, result in enumerate(ans, 1):
                	final_reply += ((str(index)) if len(ans) > 1 else '') + result + '\n'

        bot_handler.send_reply(message, final_reply)
handler_class = KumbhBot
