import smtplib
import os

gmail_address = os.environ.get("coding_email")
gmail_password = os.environ.get("gmail_pw")
# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(gmail_address, gmail_password)

def send_reminder(list_of_todos):
    to_number = os.environ.get("seabass_phone")
    body = list_of_todos
    text_msg = ("From: %s\r\n" % gmail_address + "To: %s\r\n" % to_number + "Subject: %s\r\n" % 'You need to:' + "\r\n" + body)
    server.sendmail(gmail_address, to_number, text_msg)

def request_approval(todo_name):
    to_number = os.environ.get("my_phone")
    body = todo_name
    text_msg = ("From: %s\r\n" % gmail_address + "To: %s\r\n" % to_number + "Subject: %s\r\n" % 'Has ' + body + ' been completed?')
    server.sendmail(gmail_address, to_number, text_msg)