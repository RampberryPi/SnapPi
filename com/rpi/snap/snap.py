'''
Created on May 14, 2013

@author: ramp
@email: rampberrypi@gmail.com

'''
from com.rpi.snap import mail
from subprocess import call
import ConfigParser


config = ConfigParser.ConfigParser()

config.read('dat/config.dat')

# Get all the data from cfg
user = config.get('EmailCfg', 'user')
passwd = config.get('EmailCfg', 'passwd')
fromAddr = config.get('EmailCfg', 'fromaddr')
msg = config.get('EmailCfg', 'msg1')

#Now the real action code.

ids =  mail.checkMailBox(user,passwd)
if len(ids) > 0 :
        print "Taking picture.."
        call(["raspistill -o tmp.jpg"], shell=True)
        for i in  ids :
                print "sending mail to : " + i[1]
                print mail.sendMail(fromAddr ,user,passwd ,i[1])
                
