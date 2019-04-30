import mido


def get_song_info(song_name):
	mid = mido.MidiFile('midifiles/' + song_name)

	songLength = mid.length
	min, sec = divmod(songLength, 60)
	songLengthDisp = '{:02d}:{:02d}'.format(int(min), int(sec))
	trackList = []
	trackDict = {}

	for msg in mid:
		# print(msg)

		# find tempo of the song
		if msg.is_meta and msg.type == 'set_tempo':
			bpm = int(mido.tempo2bpm(msg.tempo))

		# find track names, their channel, and amount of notes
		elif msg.is_meta and msg.type == 'track_name':
			trackList.append([msg.name, 0])
		elif msg.type is 'note_on' or msg.type is 'note_off':
			trackList[msg.channel][1] += 1

	trackCounter = 0
	for track in trackList:
		# if track[1] is not 0: - add in to remove tracks w/ 0 notes played
		trackDict[trackCounter] = [track[0], track[1]]
		trackCounter += 1

	songInfo = {'length': songLength,
	            'length_disp': songLengthDisp,
	            'BPM': bpm,
	            'track_dict': trackDict}

	return songInfo
