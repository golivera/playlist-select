import utils
import json

from flask import Flask, session, render_template, request


# config for database
DATABASE = '/tmp/music.db'
DEBUG = True
SECRET_Key = '123456'
USERNAME = 'Admin'
PASSWORD = 'Admin'

app = Flask(__name__)
app.config.from_object(__name__)
app.static_path = '/static'
queue = []


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-song', methods=['POST'])
def add_song():
    song_id = request.get_json().get('songId', None)
    if not song_id:
        return json.dumps({'status': 'error', 'msg': 'no id provided'})
    queue.append(song_id)
    return json.dumps({ 'status': 'success', 'songId': song_id });

@app.route('/all-songs')
def get_all_songs():
    available_songs = utils.get_available_songs()
    return json.dumps(available_songs)

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

    if args.dev:
        print "Running in Debug Mode"
        from flaskext.lesscss import lesscss
        lesscss(app)
        app.debug = True
    app.run()

