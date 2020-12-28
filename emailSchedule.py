import schedule
import time
import smtplib
from email.message import EmailMessage
from datetime import date


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#turn on gmail 3rd party script permissions.
server.login('sa718987@gmail.com', 'BahriaUniICC123')

def sendMail():
    #setting smtp server with TLS port (SSL port wasn't working)
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.starttls()
    # #turn on gmail 3rd party script permissions.
    # server.login('sa718987@gmail.com', 'BahriaUniICC123')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = "siffatahmed7@gmail.com"
    email['Subject'] = "Scheduled Class"
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    email.set_content("Your class is about to begin. {}".format(current_time))
    server.send_message(email)

schedule.every().monday.at("11:25").do(sendMail)
schedule.every().monday.at("14:25").do(sendMail)
schedule.every().monday.at("16:25").do(sendMail)
schedule.every().tuesday.at("15:25").do(sendMail)
schedule.every().wednesday.at("09:25").do(sendMail)
schedule.every().wednesday.at("11:25").do(sendMail)
schedule.every().wednesday.at("12:25").do(sendMail)
schedule.every().wednesday.at("13:25").do(sendMail)
schedule.every().thursday.at("09:25").do(sendMail)
schedule.every().thursday.at("12:25").do(sendMail)
schedule.every().thursday.at("09:25").do(sendMail)

#this last schedule is for test only.
schedule.every(1).minutes.do(sendMail)


while True:
    schedule.run_pending()
    time.sleep(1)