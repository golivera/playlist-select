import sqlite3
from contextlib import closing


def connect_db():
    return sqlite3.connect('/tmp/music.db')


def insert_song(title, path):
    query = "INSERT INTO track (title, path) VALUES ('{}','{}')".format(title,path)

    with closing(connect_db()) as db:
        db.cursor().execute(query)
        db.commit()


def get_song_titles():
    query = "SELECT * FROM track"
    song_list = []

    with closing(connect_db()) as db:
        results = db.cursor().execute(query)
        for song_id, song_name, _ in results:
            song_list.append({'id': song_id, 'name': song_name})

    return song_list


#returns dict {id : field }
def get_data(ids, field):
    results = {}
    query = "SELECT {} FROM track WHERE".format(field)

    for song_id in ids:
        query.join(" track.id={} OR".format(song_id))
    query = query[:-3]

    with closing(connect_db()) as db:
        cur = db.cursor.execute(query)
        for result in cur:
            song_id = result[0]
            data = result[1]
            results.update({song_id : data})

    return results


def get_song_data(song_id):
    query = "SELECT * FROM track WHERE track.id={}".format(song_id)

    with closing(connect_db()) as db:
        results = db.cursor().execute(query)
        for result in results:
            song_title, song_path = result[1], result[2]
        return {'name': song_title,
                'file_path': song_path}


def display_database():
    query = "SELECT * FROM track"

    with closing(connect_db()) as db:
        results = db.cursor().execute(query)
        for t_id, t_name, t_path in results:
            print('{} {} {}'.format(t_id, t_name, t_path))


def init_db(app):
    print "Initializing db..."
    with connect_db() as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())

    db.commit()


def delete_db(app):
    with closing(connect_db()) as db:
        query = "DROP TABLE IF EXISTS music.track"
        db.cursor().execute(query)
        db.commit()
    print 'table deleted'
    init_db()
