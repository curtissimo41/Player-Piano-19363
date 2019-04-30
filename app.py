# Importing controllers
from controllers.main import homepage
from controllers.playsong import playsong

import os
from flask import Flask, request
from flask.json import jsonify
from flask.json import JSONEncoder

# import libraries
import libraries.get_midis as gm


app = Flask(__name__)

app.register_blueprint(homepage, url_prefix='/')
app.register_blueprint(playsong, url_prefix='/playsong')


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@app.route("/getMIDIs", methods=["GET", "POST"])
def get_midis():
	songlist = gm.get_midi_names()
	print(songlist)
	serializable = MyEncoder().encode(songlist)
	return jsonify({'items': serializable})


if __name__ == "__main__":
	host = os.getenv("IP", "0.0.0.0")
	port = os.getenv("PORT", 8080)
	app.secret_key = 'teststring'
	app.run(host, port)
