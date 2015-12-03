#!/usr/bin/env python
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
import ConfigParser
cf = ConfigParser.ConfigParser()
cf.read('/root/ufenqi/db.ini')
sender = cf.get('mail', 'sender')
receiver = ['wubinwei@ufenqi.com']
subject = '[通知]今日作业执行完成'
username = cf.get('mail', 'user')
password = cf.get('mail', 'password')
msg = MIMEText(
    '<html><h1>你好!</h1><h1></h1><h1>今日的作业已经成功执行完成，请知悉。</h1></html>', 'html', 'utf-8')
msg['Subject'] = subject
msg['From'] = sender
smtp = smtplib.SMTP()
smtp.connect('smtp.exmail.qq.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
