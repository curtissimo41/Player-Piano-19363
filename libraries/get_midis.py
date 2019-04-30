from os import listdir
from os.path import isfile, join, expanduser


def get_midi_names():
    # function to get MIDI filenames in midifiles directory
    path = expanduser('~') + '/Desktop/Python-Piano/midifiles/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and
                 f[0] is not '.']

    return onlyfiles
