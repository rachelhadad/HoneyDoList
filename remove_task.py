# TODO add approve task complete/remove task from todo list
import sqlite3
from sqlalchemy import Column, String, Boolean, Date
from main import db, Todo

con = sqlite3.connect('todolist.db')
cur = con.cursor()
cur.execute("DELETE FROM todo WHERE name = 'Move couch'")
db.session.commit()

tables = cur.execute("SELECT * FROM todo")
table = tables.fetchall()
print(table)

con.commit()
con.close()