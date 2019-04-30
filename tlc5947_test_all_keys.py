import board
import busio
import digitalio
import time 
import adafruit_tlc5947

maxPwm = 4095
 
# Define pins connected to the TLC5947
SCK = board.SCK
MOSI = board.MOSI
LATCH = digitalio.DigitalInOut(board.D5)
 
# Initialize SPI bus.
spi = busio.SPI(clock=SCK, MOSI=MOSI)
 
# Initialize TLC5947
tlc5947 = adafruit_tlc5947.TLC5947(spi, LATCH, auto_write=False, num_drivers=4)

def test_all_keys():
    val = 4000
    zeroarray = [0] * 88
    for i in range(len(zeroarray)):
        tlc5947[i] = zeroarray[i]
        
    tlc5947.write()

    time.sleep(5)

    while 1:
        time.sleep(.5)
        tlc5947[0] = 2000
        tlc5947.write()
        time.sleep(.5)
        tlc5947[0] = 0
        tlc5947.write()
        tlc5947[1] = 2000
        tlc5947.write()
        time.sleep(.5)
        tlc5947[1] = 0
        tlc5947.write()
        
        
        """
        for i in range(0, 88):
            print(i)
            time.sleep(.3)
            tlc5947[i] = 0
            tlc5947.write()
            time.sleep(.3)
            tlc5947[i+1] = val
            tlc5947.write()
        """

#test_all_keys()