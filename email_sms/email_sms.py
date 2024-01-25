import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp.ehlo())
print(smtp.starttls())
print(smtp.login('panopticam3@gmail.com','jpghjgpugitsaibl'))

msg = MIMEText('본문')
msg['Subject'] = '제목'

smtp.sendmail('panopticam3@gmail.com','heechanny@gmail.com','Subject: hello\nHi nice to meet you, I am Channy \nThanks,\nChan Lim.')
smtp.sendmail('panopticam3@gmail.com','heechanny@gmail.com',msg.as_string())

print('메일 전송 완료')

'''
from imapclient import IMAPClient
import pprint,imaplib

imaplib._MAXLINE = 10000000


imap = IMAPClient('imap.gmail.com',ssl=True)
imap.login('heechanny@gmail.com','xllbvgvsepttqtkk')
imap.select_folder('INBOX', readonly=True)
i_search = imap.search(['SINCE','01-Jan-2024','BEFORE','09-Jan-2024'])
g_search = imap.gmail_search('hi')
#pprint.pprint(imap.list_folders())

for uid, data in imap.fetch(g_search,['ENVELOPE']).items():
    envelope = data[b'ENVELOPE']
    print('ID #%d: "%s" received %s' % (uid, envelope.subject.decode(), envelope.date))
'''

import openpyxl, smtplib, sys,os

os.chdir('/Users/chanlim/Desktop')

wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb['Sheet1']


for member in range(2,len(sheet['A'])):
    undue = []
    for i in range(3,len(sheet['1'])):
        val = sheet[chr(ord('A')+i)+str(member)].value
        if val == None:
            undue.append(sheet[chr(ord('A')+i)+str(1)].value)
    
    if undue:
        print('sending email to',sheet[chr(ord('A'))+str(member)].value,'email:',sheet[chr(ord('A')+1)+str(member)].value,'\nundue month:',', '.join(undue))
        msg = MIMEText(str('Your undue month: '+', '.join(undue)+'\npayments are undue. Please make the payment.\n\nThanks,\nPeopleHealth'))
        msg['Subject'] = 'Hello '+ sheet[chr(ord('A'))+str(member)].value+', please make undued payments'
        smtp.sendmail('panopticam3@gmail.com',sheet[chr(ord('A')+1)+str(member)].value,msg.as_string())
        print('메일 전송 완료')


smtp.quit()
