import sys, os, zulip
sys.path.insert(0,os.getcwd())
import smtplib
def send_email(bot_handler,*params)->str:
	sender_name = params[0][0]
	sender_aadhar = params[0][1]
	lost_name = params[0][2]
	lost_aadhar = params[0][3]
	subject = "***URGENT-MISSING PERSON***"
	content="Sender's name:" + sender_name + "\nSender's aadhar number:" + sender_aadhar +"\nMissing person's name:" + lost_name +"\nMissing person's aadhar number:" + lost_aadhar;
	message = 'Subject: {}\n\n{}'.format(subject, content)
	mail=smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login('sjagwani31@gmail.com','swiss@cake1234')
	receiver="ria1000@gmail.com"
	mail.sendmail('sjagwani31@gmail.com',receiver,message)
	mail.close()
	return "Noted dear user!"
	
	
	
	
	
	
