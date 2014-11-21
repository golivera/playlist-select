from flask import Flask, session, request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    session.available_songs = [(n,"song-{}".format(n),) for n in range(10)]
    return render_template('index.html')

@app.route('/add-song', methods=['POST'])
def add_song():
    song_id = request.form['songId']
    return "added song {}".format(song_id)

if __name__ == '__main__':
    app.debug = True
    app.run()
