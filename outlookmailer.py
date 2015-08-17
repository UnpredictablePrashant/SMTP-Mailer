#Author: Prashant Kumar Dey
#Code name: Unpredictable
#Send Email using your own email
#If you have a suggestion or query feel free to contact me at prashantsavior@gmail.com
#Visit My Blog at www.kiitsolution.blogspot.in
#---------------------------------------------------------

import time;
import os;
import smtplib;
import getpass;

print ('\n --------Welcome to the Microsoft Live email sender Script----------------- \n\n')
localtime = time.asctime(time.localtime(time.time()))
print ('Date & Time: ', localtime)
print ('\n\n')


#Microsoft Live server
server_live = smtplib.SMTP('smtp.live.com', 25)

#Logging into your account
sender = input("Enter your email: ")
pas = getpass.getpass("Enter Your Password: ")
print ("Server is logging in... Please wait!")
server = server_live
server.ehlo()
server.starttls()
server.ehlo
server.login(sender, pas)
os.system('cls')
print ("You are logged in. Welcome ", sender)

kilo = input("Enter the email address of the recepient: ")
TO = [kilo]
SUBJECT = input("Enter the subject: ")
TEXT = input("Enter the text to be send: ")

#Message content
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (sender, ", ".join(TO), SUBJECT, TEXT)



try:
	server.sendmail(sender, [TO], message)
	print ('Message sent Successfully!!!')
except:
	print ('Error, cannot connect to mail server')
	
k=1

while k==1:
	p = input("do you want send more mails:0/1 ")
	if p==1:
		k=1
		hecto = input("Enter the email address of the recepient: ")
		TOW = [hecto]
		SUJECTW = input("Enter the subject: ") 
		TEXTW = input("Enter the text to be send: ")
		msg = """\
			From: %s
			To: %s
			Subject: %s
			%s
			""" % (sender, ", ".join(TOW), SUBJECTW, TEXTW)
		try:
			server.sendmail(sender, [TOW], msg)
			print ('Message sent Successfully!!!')
		except:
			print ('Error, cannot connect to mail server')
	else : 
		k=0

server.quit()
