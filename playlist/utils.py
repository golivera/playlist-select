import argparse
import vlc
import os
import mydb

instance = vlc.Instance()
mediaplayer = instance.media_player_new()
music_formats = ['.mp3','.flac','.mp4']

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Input music directory")
    parser.add_argument("-u", "--update", action='store_true', help="Run database update")
    parser.add_argument("-d", "--dev", action='store_true', help="Run in development mode")
    return parser.parse_args()

#return list of songs
def get_available_songs():
    return mydb.get_song_titles()


def setup_song_db(app, music_dir=None):
    print "Updating song DB..."
    mydb.init_db(app)

    if not music_dir:
        music_dir = "test_music"

    for root, dirs, files in os.walk(music_dir):
        for cur_file in files:
            file_path = os.path.abspath(os.path.join(root, cur_file))
            file_ext = os.path.splitext(file_path)[-1]
            if file_ext in music_formats:
                mydb.insert_song(cur_file, file_path)


# VLC Utility Methods
def play_song(queue):
    if not queue:
        print "Queue is empty"
        return

    song_id = queue.pop(0)
    print "Preparing to play song with id {}".format(song_id)

    song_data = mydb.get_song_data(song_id)
    if not song_data or not os.path.isfile(song_data['file_path']):
        return

    print "Playing: {}".format(song_data['name'])
    media = instance.media_new(unicode(song_data['file_path']))
    mediaplayer.set_media(media)
    mediaplayer.play()
    return song_data


def pause_song():
    mediaplayer.pause()


def stop_song():
    mediaplayer.stop()
    return None

