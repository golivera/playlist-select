from flask import Flask, session, render_template, request

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
    session.available_songs = utils.get_available_songs()
    return render_template('index.html')

@app.route('/add-song', methods=['POST'])
def add_song():
    song_id = request.form['songId']
    return "added song {}".format(song_id)

@app.route('/media-action', methods=['POST'])
def process_media_action():
    action = request.form['action']

    if action == "play":
        utils.play_song()
    elif action == "pause":
        utils.pause_song()
    elif action == "stop":
        utils.stop_song()

    return "{}".format(action)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    print "Initializing db..."
    with connect_db() as db:
	    with app.open_resource('schema.sql', mode='r') as f:
	        db.cursor().executescript(f.read())
    db.commit()

if __name__ == '__main__':
    args = utils.init_parser()

    print args.update
    if args.update:
        utils.setup_song_db(app, args.path)

    app.debug = True
    app.run()

