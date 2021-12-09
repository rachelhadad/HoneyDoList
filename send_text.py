import smtplib
import os

gmail_address = os.getenv("coding_email")
gmail_password = os.getenv("gmail_pw")
# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(gmail_address, gmail_password)

def send_newtask(todo_task):
    to_number = os.getenv("seabass_phone")
    body = todo_task
    text_msg = ("From: %s\r\n" % gmail_address + "To: %s\r\n" % to_number + "Subject: %s\r\n" % 'New task added to your to do list:' + "\r\n" + body)
    server.sendmail(gmail_address, to_number, text_msg)

def request_approval(todo_name):
    to_number = os.getenv("my_phone")
    body = todo_name
    text_msg = ("From: %s\r\n" % gmail_address + "To: %s\r\n" % to_number + "Subject: %s\r\n" % 'Has ' + body + ' been completed?')
    server.sendmail(gmail_address, to_number, text_msg)