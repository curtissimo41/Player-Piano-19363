import pygame
import mido


def playMidiFake(song_name):
	pygame.mixer.init()
	pygame.mixer.music.load('midifiles/' + song_name)
	pygame.mixer.music.play(loops = 0, start = 0.0)


def pauseMidiFake():
	if pygame.mixer.music.get_busy():
		print("Made it inside pause function.")
		pygame.mixer.music.pause()


def stopMidiFake():
	if pygame.mixer.music.get_busy():
		pygame.mixer.music.stop()
