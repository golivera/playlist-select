import sqlite3
import os
import argparse

from flask import Flask, session, render_template, request
from contextlib import closing

import utils

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
    session.available_songs = [(n,"song-{}".format(n),) for n in range(10)]
    return render_template('index.html')

@app.route('/add-song', methods=['POST'])
def add_song():
    song_id = request.form['songId']
    return "added song {}".format(song_id)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    print "Initializing db..."
    with connect_db() as db:
	    with app.open_resource('schema.sql', mode='r') as f:
	        db.cursor().executescript(f.read())
    db.commit()

def setup_song_db(music_dir=None):
    print "Updating song DB..."

    if not music_dir:
        music_dir = "test_music"

    for root, dirs, files in os.walk(music_dir):
        for cur_file in files:
            file_path = os.path.abspath(os.path.join(root, cur_file))
            # TODO: Error checking for correct music formats
            # TODO: Insert Song into DB

if __name__ == '__main__':
    args = utils.init_parser()

    if args.update:
        setup_song_db(args.path)

    app.debug = True
    app.run()

