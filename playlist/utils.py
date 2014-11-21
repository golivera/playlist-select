import argparse
import vlc

instance = vlc.Instance()
mediaplayer = instance.media_player_new()

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Input music directory")
    parser.add_argument("-u", "--update", action='store_true', help="Run database update")
    return parser.parse_args()


def get_available_songs():
    # TODO: Query DB for songs
    songs = [(n,"song-{}".format(n),) for n in range(10)]
    return songs


def setup_song_db(music_dir=None):
    print "Updating song DB..."

    if not music_dir:
        music_dir = "test_music"

    for root, dirs, files in os.walk(music_dir):
        for cur_file in files:
            file_path = os.path.abspath(os.path.join(root, cur_file))
            # TODO: Error checking for correct music formats
            # TODO: Insert Song into DB


# VLC Utility Methods
def play_song():
    # TODO: Check File Exists
    filepath = ""
    # TODO: Get top of song queue
    media = instance.media_new(unicode(filepath))
    mediaplayer.set_media(media)
    mediaplayer.play()


def pause_song():
    mediaplayer.pause()


def stop_song():
    mediaplayer.stop()

