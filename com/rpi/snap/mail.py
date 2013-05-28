'''
Created on May 14, 2013

@author: ramp
@email: rampberrypi@gmail.com

'''

import poplib
from email import parser
import os
import smtplib

from email import Encoders
from email.mime.image import MIMEImage
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
from email.utils import parseaddr

##########################################
# Checks mail with the given credentials
# and returns a list of from addresses
##########################################
def checkMailBox(user, passwd):

        pop_con = poplib.POP3_SSL('pop.gmail.com')
        pop_con.user(user)
        pop_con.pass_(passwd)

        messages = [pop_con.retr(i) for i in range(1, len(pop_con.list()[1]) + 1)]
        messages = ["\n".join(msg[1]) for msg in messages]
        messages = [parser.Parser().parsestr(msg) for msg in messages]

        result = []
        for message in messages:
                if message['subject'].lower() == 'snap' :
                        fromAndSub = parseAddr(message['from'])
                        result.append(fromAndSub)
                print "From : " , message['from']
                print "Subject : " , message['subject']

        pop_con.quit()
        return result

#########################################################
# Send mail with a specified attachment
# By default, it will pick up the tmp.jpg in current dir.
#########################################################

def sendMail(fromAddr, user, passwd, toAddr, ATTACH='./tmp.jpg'):
        HOST = 'smtp.gmail.com:587'
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = 'SNAPPED'
        msg['Date'] = formatdate(localtime=True)

        # attach
        fp = open(ATTACH, 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)

        server = smtplib.SMTP(HOST)
        server.starttls()
        server.login(user, passwd)
        server.sendmail(fromAddr, toAddr, msg.as_string())
        server.close()

##########################################
# Parse the from addr
##########################################
def parseAddr(addr):
        return  parseaddr(addr)
