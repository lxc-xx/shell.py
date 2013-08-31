#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText

server_account = 'monitor.py@gmail.com'
server_pwd = 'monitor@google'
server_smtp_address = 'smtp.gmail.com'
server_smtp_port = 465


msg = MIMEText("Hello")

def get_mail_server(smtp_address, smtp_port, account, pwd): 
    server = smtplib.SMTP_SSL(smtp_address, smtp_port) 
    server.login(account, pwd) 
    return server

def send_mail(server, from_address, destination_address, subject = '', content = '', attachments = []):
    mail = MIMEMultipart() 
    mail.attach(MIMEText(content))

    for file_name, content in attachments: 
        attachment = MIMEText(content)
        attachment.add_header('Content-Disposition', 'attachment', filename=file_name) 
        mail.attach(attachment) 

    mail['From'] = from_address 
    mail['To'] = destination_address 
    mail['Subject'] = subject
    
    server.sendmail(from_address, [destination_address], mail.as_string()) 
    return 0;

import sys
import os
import uuid
import datetime
import socket
from subprocess import Popen, PIPE

def main(argv):
    if len(argv) < 2:
        print "Usage: monitor.py mail_address command [arg]*"
        sys.exit(1)

    mail_address = argv[0]
    job_argv = argv[1:]
    job_id = uuid.uuid1().hex

    try: 
        server = get_mail_server(server_smtp_address, server_smtp_port, server_account, server_pwd)
    except Error:
        print "Error: Failed to connect to mail server"


    process = Popen( job_argv, stderr = PIPE, stdout = PIPE )
    current_time = datetime.datetime.now().ctime()

    command = ' '.join(job_argv)
    subject = "[monitor.py] JOB: " + command + ' ID: ' + job_id
    content = '''
    Job ID: %(id)s
    Job PID: %(pid)s
    Job command: %(command)s
    Host name: %(hostname)s
    Begun execution.
    Time: %(time)s
    '''% {
            "id":job_id, 
            "pid":process.pid,
            "command":command,
            "hostname":socket.gethostname(),
            "time":current_time}
    
    try: 
        send_mail(server, server_account, 'me@xuanchong.li', subject, content, [])
    except Error:
        print "Error: Failed to send start mail"

    return_code = process.wait()
    current_time = datetime.datetime.now().ctime()

    stdout = process.stdout.read()
    stderr = process.stderr.read()

    content = '''
    Job ID: %(id)s
    Job PID: %(pid)s
    Job command: %(command)s
    Host name: %(hostname)s
    Return Code: %(return_code)s
    Time: %(time)s
    '''% {
            "id":job_id, 
            "pid":process.pid,
            "command":command,
            "hostname":socket.gethostname(),
            "return_code":str(return_code),
            "time":current_time}
    try: 
        send_mail(server, server_account, 'me@xuanchong.li', subject, content, [('stdout.txt',stdout), ('stderr',stderr)])
    except Error:
        print "Error: Failed to send the end mail"

    try: 
        server.quit()
    except Error:
        print "Error: Failed to quit the mail server"

    return 0

if __name__ == '__main__':
    main(sys.argv[1:])
