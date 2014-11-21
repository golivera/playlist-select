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
    song_id = request.form['song_id']
    return "added song {}".format(song_id)

if __name__ == '__main__':
    args = utils.init_parser()

    print args.update
    if args.update:
        utils.setup_song_db(app, args.path)

    app.debug = True
    app.run()

