from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
heroku = Heroku(app)

db = SQLAlchemy(app)

class Users(db.Model):
	__tablename__="Users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40))
	password = db.Column(db.String(40))
db.create_all()

@app.route('/')
def index():
	return render_template('home.html')


@app.route("/fanfictions")
def fanfiction():
	return render_template('fanfictions.html')

@app.route("/facts")
def facts():
	return render_template('facts.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/login", methods=["GET","POST"])
def login():
	if request.method=="GET":

		return render_template('login.html')

	elif request.method=="POST":
		return render_template('home.html')
if __name__ == "__main__":
    app.run()	