from flask import Blueprint, render_template, request
from flask.json import jsonify
from flask.json import JSONEncoder

import libraries.get_song_info as gsi
import play_midi as pm # plays MIDIs on Raspberry Pi
# import play_midi_fake as pmfake - plays MIDIs digitally
import tlc5947_test_all_keys as tak


playsong = Blueprint('playsong', __name__, template_folder = 'templates')
songName = ''


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@playsong.route('/', methods=['POST'])
def playsong_view():
    global songName
    songName = request.form['song_name']
    return render_template('playsong.html', song_name = songName)


@playsong.route("/get_song_info", methods=["GET", "POST"])
def getSongInfo():
    songInfo = gsi.get_song_info(songName)
    serializable = MyEncoder().encode(songInfo)
    return jsonify({'items': serializable})


@playsong.route("/play", methods=["GET", "POST"])
def play():
    # Change this code on Pi to:
    pm.playMidi(songName)
    # tak.test_all_keys()
    # pmfake.playMidiFake(songName)
    return 'Playing'


@playsong.route("/pause", methods=["GET", "POST"])
def pause():
    # NEEDS TO BE IMPLEMENTED TO WORK ON PI
    # Change this code on Pi to:
    # pmfake.pauseMidiFake()
    return 'Paused'


@playsong.route("/stop", methods=["GET", "POST"])
def stop():
    # NEEDS TO BE IMPLEMENTED TO WORK ON PI
    # Change this code on Pi to:
    # pmfake.stopMidiFake()
    return 'Stopped'
