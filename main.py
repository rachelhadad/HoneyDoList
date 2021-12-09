from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from send_text import send_newtask, request_approval

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


# db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    todos = Todo.query.order_by(Todo.due_date).all()
    return render_template("index.html", todos=todos)


@app.route('/add', methods=["POST"])
def add_task():
    get_due_date = request.form["date"]
    due_date = datetime.strptime(get_due_date, "%Y-%m-%d")
    todo = Todo(name=request.form["task"].capitalize(), due_date=due_date, pending_completion=False, complete=False)
    db.session.add(todo)
    db.session.commit()
    send_newtask(todo.name)
    return redirect(url_for('home'))

@app.route('/mark_complete', methods=["POST", "GET"])
def click_complete():
    todo_id = request.args.get("id")
    todo = Todo.query.get(todo_id)
    todo.pending_completion = True
    db.session.commit()
    request_approval(todo.name)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
