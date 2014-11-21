import sqlite3
from contextlib import closing

def connect_db():
    return sqlite3.connect('/tmp/music.db')

def insert_song(title,path):
    query = "INSERT INTO tracks (title, path) VALUES ('{}','{}')".format(title,path)

    with closing(connect_db()) as db:
        db.cursor().execute(query)
        db.commit()

def get_song_titles():
    query = "SELECT * FROM tracks"
    song_list = []

    with closing(connect_db()) as db:
        results = db.cursor().execute(query)
        for song_id, song_name, _ in results:
            song_list.append((song_id, song_name))

    return song_list

def get_song_data(song_id):
    query = "SELECT * FROM tracks WHERE {} = table.song_id".format(song_id)

    with closing(connect_db()) as db:
        results = db.cursor().execute(query)
        song_title, song_path = results[1], results[2]
        return {'title' : song_title,
                'file_path' : song_path}

def display_database():
    query = "SELECT * FROM tracks"

    with closing(connect_db()) as db:
        results = db.cursor().execute(query)
        for t_id, t_name, t_path in results:
            print('{} {} {}'.format(t_id,t_name,t_path))

def init_db(app):
    print "Initializing db..."
    with connect_db() as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())

    db.commit()

def delete_db(app):
    with closing(connect_db()) as db:
        query = "DROP TABLE IF EXISTS music.tracks"
        db.cursor().execute(query)
        db.commit()
    print 'table deleted'
    init_db()

