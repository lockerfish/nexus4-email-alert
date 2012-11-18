#!/usr/bin/python

from urllib import urlopen
import smtplib
import logging

sender = 'myemail@email.com'
recipients = ['myemail@email.com']
url_8gb = 'https://play.google.com/store/devices/details?id=nexus_4_8gb'
url_16gb = 'https://play.google.com/store/devices/details?id=nexus_4_16gb'
gmail_pwd = 'password'

def sendMailNotification(body):
  message = '\r\n'.join(['From: ' + sender,
  'Subject: Nexus 4 back in stock!',
  'To: ' + ', '.join(recipients),
  'MIME-Version: 1.0',
  'Content-Type: text/html',
  body ])

  #print message

  try:
    session = smtplib.SMTP('smtp.email.com', 587)
    session.ehlo()
    session.starttls()
    session.login(sender, gmail_pwd)
    session.sendmail(sender, recipients, message)
    session.quit()
  except Exception:
    print logging.exception()

def checkIfSoldOut(url):
  contents = urlopen(url).read()
  if contents.find('hardware-sold-out') != -1:
    return True

def main():
  if not checkIfSoldOut(url_8gb):
    print 'Nexus 4 (8GB) available'
    sendMailNotification('Check Google Play Store! - Nexus 4 (8GB) is available\r\n' + url_8gb)
  else:
    print 'Nexus 4 (8GB) sold out'

  if not checkIfSoldOut(url_16gb):
    print 'Nexus 4 (16GB) available'
    sendMailNotification('Check Google Play Store! - Nexus 4 (16GB) is available\r\n' + url_16gb)
  else:
    print 'Nexus 4 (16GB) sold out'


if __name__ == "__main__":
  main()
