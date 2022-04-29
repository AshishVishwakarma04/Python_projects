# Extract top news from HackerNews and send it as email

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

# email content placeholder

content = ''

#extracting Hacker News Stories

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<b>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('tg',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+'::'+tag.text+"\n" + '<br>')if tag.text!='More' else '')
    return(cnt)    


cnt = extract_news('https://news.vcombinator.com/')
content += cnt
content += ('<br>------</br>')
content += ('<br><br>End of Message')

#Lets send the email

print('Composing Email...')

# update your email credentails

SERVER = 'smtp.gmail.com' #"your smtp server"
PORT = 587 # your port number
FROM = '' # "your from email id"
TO = '' # "your to email id" "can be list"
PASSWORD = '' #your email id's password"

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automates Email]' + '' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['from'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM, PASSWORD)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent...')

server.quit()