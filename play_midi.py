import mido
import json
import time
from math import floor

import board
import busio
import digitalio
import adafruit_tlc5947

def reset_key():
    SCK = board.SCK
    MOSI = board.MOSI
    LATCH = digitalio.DigitalInOut(board.D5)

    # Initialize SPI bus.
    spi = busio.SPI(clock=SCK, MOSI=MOSI)

    # Initialize TLC5947
    tlc5947 = adafruit_tlc5947.TLC5947(spi, LATCH, auto_write=False,
                                       num_drivers=4)
    for x in range(88):
        tlc5947[x] = 0
    tlc5947.write()

def playMidi(song_name):
    mid = mido.MidiFile('midifiles/' + song_name)

    notesDict = {'songName': 'testname', 'bpm': 999, 'notes': []}
    tempo = 0
    length = 0
    notesArray = [[]]
    tickLength = 0
    VOLUME = 4
    MIN = 800

    SCK = board.SCK
    MOSI = board.MOSI
    LATCH = digitalio.DigitalInOut(board.D5)

    # Initialize SPI bus.
    spi = busio.SPI(clock=SCK, MOSI=MOSI)

    # Initialize TLC5947
    tlc5947 = adafruit_tlc5947.TLC5947(spi, LATCH, auto_write=False,
                                       num_drivers=4)
    for x in range(88):
        tlc5947[x] = 0
    tlc5947.write()

    for msg in mid:
        if msg.is_meta and msg.type == 'set_tempo':
            tempo = int(msg.tempo)
            length = int(floor(mido.second2tick(mid.length,
                                                mid.ticks_per_beat,
                                                tempo)))
            tickLength = mido.tick2second(1, mid.ticks_per_beat, tempo)
            break

    print('Tick length: ' + str(tickLength))
    currentTick = 0
    notesArray[0] = [0 for x in range(89)]
    lineIncrement = 0
    for msg in mid:
        #print(msg)
        if msg.type is 'note_on' or msg.type is 'note_off':
            delayAfter = int(floor(mido.second2tick(msg.time, mid.ticks_per_beat, tempo)))
            if delayAfter == 0:
                if msg.note < 89:
                    notesArray[lineIncrement][msg.note - 12] = msg.velocity
            else:
                notesArray[lineIncrement][88] = delayAfter
                notesArray.append([0 for x in range(89)])
                for y in range(88) :
                    notesArray[lineIncrement+1][y] = notesArray[lineIncrement][y]
                #notesArray.append(notesArray[lineIncrement])
                lineIncrement += 1
                notesArray[lineIncrement][88] = 0
                if msg.note < 89:
                    notesArray[lineIncrement][msg.note - 12] = msg.velocity
                    
                notesArray.append([0 for x in range(89)])
                for y in range(88) :
                    notesArray[lineIncrement+1][y] = notesArray[lineIncrement][y]
                lineIncrement += 1                
                
                
                
            """ Old code:
                for x in range (newNote['delayAfter']):
                    if x != 0:
                        notesArray[x+currentTick] = notesArray[x+currentTick-1]
                currentTick += newNote['delayAfter']
                
            notesArray[currentTick][newNote['note'] - 1] = newNote['velocity']
            # tlc5947.write()
            notesDict['notes'].append(newNote)
            """
            
    """
    with open('notes.json', 'w') as outfile:
        json.dump(notesDict, outfile)
    """
    
    startTime = time.time()
    tlc5947.write()
    time.sleep(3)
    for z in range(0, len(notesArray)-1, 2):
        line = notesArray[z]
        """
        tlc5947[27] = 900
        tlc5947[68] = 4000
        tlc5947.write()
        time.sleep(2)
        tlc5947[27] = 0
        tlc5947[68] = 0
        tlc5947.write()
        time.sleep(2)
        """
        
        #print(line)
        # send array to PWM IC
        for x in range(len(line) - 1):
            if line[x] != 0:
                if x == 56:
                    tlc5947[x] = MIN+200
                elif x== 46:
                    tlc5947[x] = 600
                elif line[x]*VOLUME < MIN:
                    tlc5947[x] = MIN
                else:
                   # tlc5947[x] = line[x] * VOLUME
                   tlc5947[x] = MIN
            else:
                tlc5947[x] = 0
        tlc5947.write()
        # time.sleep(tickLength)
        
        time.sleep(mido.tick2second(line[88], mid.ticks_per_beat, tempo) * 0.7)
        
        for x in range(88):
            tlc5947[x] = notesArray[z+1][x]
        tlc5947.write()
        
        time.sleep(mido.tick2second(line[88], mid.ticks_per_beat, tempo) * 0.3)
        
    for x in range(88):
        tlc5947[x] = 0
    tlc5947.write()

reset_key()
#playMidi('bumble_bee.mid')
#playMidi('for_elise_by_beethoven.mid')
# playMidi('debussy_clair_de_lune.mid')
#playMidi('Maple_Leaf_Rag_MIDI.mid')
#playMidi('jules_mad_world.mid')
#playMidi('Pinkfong-Babyshark-Anonymous-20190203093900-nonstop2k.com.mid')
#playMidi('080-Finale.mid')
#playMidi('gwyn_by_nitro.mid')
playMidi('Westworld_Theme.mid')
#playMidi('Smash_Mouth.mid')
#playMidi('vangelis_-_chariots_of_fire_ost_bryus_vsemogushchiy.mid')
#playMidi('GameofThrones.mid')
#playMidi('Welcome_to_Jurassic_World.mid')
#playMidi('Games_of_Thrones_piano_cover_by_Lisztlovers.MID')
#playMidi('Sonic.mid')
#playMidi('Moana.mid')
#playMidi('HesaPirate.mid')
#playMidi('ChamberOfSecrets-HedwigsTheme.mid')
#playMidi('DuelOfTheFates.mid')
#playMidi('Star-Wars-Imperial-March.mid')
#playMidi('PianoMan.mid')
#playMidi('the_entertainer.mid')
#playMidi('chopin_minute.mid')