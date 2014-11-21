import sqlite3
from flask import Flask, session, render_template
from contextlib import closing

# config for database
DATABASE = '/tmp/music.db'
DEBUG = True
SECRET_Key = '123456'
USERNAME = 'Admin'
PASSWORD = 'Admin'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    init_db()
    print 'database initalized'
    session.available_songs = ["song-{}".format(n) for n in range(10)]
    return render_template('index.html')

@app.route('/add-song')
def add_song():
    return "asdfasdf"

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with connect_db() as db:
	with app.open_resource('schema.sql', mode='r') as f:
	     db.cursor().executescript(f.read())
	db.commit()

		

if __name__ == '__main__':
    app.debug = True
    app.run()
