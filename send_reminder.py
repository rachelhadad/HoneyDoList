import smtplib
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Setup db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("sqlite_todo_db")
# Silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    due_date = db.Column(db.Date)
    pending_completion = db.Column(db.Boolean)
    complete = db.Column(db.Boolean)

gmail_address = os.environ.get("coding_email")
gmail_password = os.environ.get("gmail_pw")
# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(gmail_address, gmail_password)

all_todos = Todo.query.all()
todos_string='\n'.join([todo.name for todo in all_todos])

def send_reminder(list_of_todos):
    to_number = os.environ.get("seabass_phone")
    body = list_of_todos
    text_msg = ("From: %s\r\n" % gmail_address + "To: %s\r\n" % to_number + "Subject: %s\r\n" % 'You need to:' + "\r\n" + body)
    server.sendmail(gmail_address, to_number, text_msg)

send_reminder(todos_string)