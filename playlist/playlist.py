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
queue = []


@app.route('/')
def home():
    session.available_songs = utils.get_available_songs()
    return render_template('index.html')

@app.route('/add-song', methods=['POST'])
def add_song():
    song_id = request.form['songId']
    queue.append(song_id)
    return "added song {}".format(song_id)

@app.route('/media-action', methods=['POST'])
def process_media_action():
    action = request.form['action']

    if action == "play":
        utils.play_song(queue)
    elif action == "pause":
        utils.pause_song()
    elif action == "stop":
        utils.stop_song()

    return "{}".format(action)


if __name__ == '__main__':
    args = utils.init_parser()

    if args.update:
        utils.setup_song_db(app, args.path)

    app.debug = True
    app.run()

