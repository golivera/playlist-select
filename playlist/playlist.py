from flask import Flask, session
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    session.available_songs = ["song-{}".format(n) for n in range(10)]
    return render_template('index.html')

@app.route('/add-song')
def add_song():
    return "asdfasdf"

if __name__ == '__main__':
    app.debug = True
    app.run()
