import sys, os
sys.path.insert(0,os.getcwd())

 
import wave  
import bleach
import random
from googletrans import Translator
import json
from typing import Any,List,Dict 

def bhajan(bot_handler:Any) -> str:  
	k=random.randint(1,10)
	if k==1:
		Audio="https://www.youtube.com/watch?v=nx5jwMAzPWo&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT";
	elif k==2:
		Audio="https://www.youtube.com/watch?v=rfOUQH5gjbA&index=2&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT";
	elif k==3:
		Audio="https://www.youtube.com/watch?v=HbRqWmHB-fI&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT&index=3";
	elif k==4:
		Audio="https://www.youtube.com/watch?v=Dt-4awRG8VM&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT&index=4";
	elif k==5:
		Audio="https://www.youtube.com/watch?v=Fl1i0zLpio4&index=5&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT";
	elif k==6:
		Audio="https://www.youtube.com/watch?v=qyXCpnJBF1M&index=6&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT";
	elif k==7:
		Audio="https://www.youtube.com/watch?v=MhE2Gyx3f5w&index=7&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT";
	elif k==8:
		Audio="https://www.youtube.com/watch?v=oM-1q3LZ0vQ&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT&index=8";
	elif k==9:
		Audio="https://www.youtube.com/watch?v=DsNfSjaO6Bo&index=9&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT";
	else:
		Audio="https://www.youtube.com/watch?v=Cwt30Z8RmCc&index=10&list=PLyXHXSHxLqKxAFacjq0IRqYHjwkivQyWT";	
		
	html = bleach.linkify(Audio)
	
	return html
