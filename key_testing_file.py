import board
import busio
import digitalio
import adafruit_tlc5947
import time

keymin = [600,600,600,575,600,300,450,390,375,475,425,275,325,250,550,275,500,475,550,425,500,250,340,300,550,300,350,325,350,275,350,550,300,350,275,350,500,450,325,350,350,325,350,325,250,450,325,550,250,375,275,375,375,300,250,550,700,375,600,250,575,425,525,350,325,375,300,350,600,400,600,350,350,350,400,400,300,550,250,375,575,300,400,300,300,375]
print(len(keymin))
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

def testing():
    SCK = board.SCK
    MOSI = board.MOSI
    LATCH = digitalio.DigitalInOut(board.D5)

    # Initialize SPI bus.
    spi = busio.SPI(clock=SCK, MOSI=MOSI)

    # Initialize TLC5947
    tlc5947 = adafruit_tlc5947.TLC5947(spi, LATCH, auto_write=False,
                                       num_drivers=4)
    
    for x in range(20,26):
        tlc5947[x] = 1000
        tlc5947.write()
        time.sleep(0.5)
        tlc5947[x] = 0
        tlc5947.write()
        time.sleep(0.5)

#    tlc5947[7] = 1000
#    tlc5947.write()
#    time.sleep(0.5)
#    tlc5947[7] = 0
#    tlc5947.write()
#    time.sleep(0.5)
#    tlc5947[28] = 1000
#    tlc5947.write()
#    time.sleep(0.5)
#    tlc5947[28] = 0
#    tlc5947.write()
#    time.sleep(0.5)
#    tlc5947[56] = 1000
#    tlc5947.write()
#    time.sleep(0.5)
#    tlc5947[56] = 0
#    tlc5947.write()
#    time.sleep(0.5)
#    tlc5947[80] = 1000
#    tlc5947.write()
#    time.sleep(0.5)
#    tlc5947[80] = 0
#    tlc5947.write()
#    time.sleep(0.5)

def individual(x, val, iterations):
    SCK = board.SCK
    MOSI = board.MOSI
    LATCH = digitalio.DigitalInOut(board.D5)

    # Initialize SPI bus.
    spi = busio.SPI(clock=SCK, MOSI=MOSI)

    # Initialize TLC5947
    tlc5947 = adafruit_tlc5947.TLC5947(spi, LATCH, auto_write=False,
                                       num_drivers=4)
    for g in range(0, iterations):
        tlc5947[x] = val
        tlc5947.write()
        time.sleep(0.5)
        tlc5947[x] = 0
        tlc5947.write()
        time.sleep(0.5)
  


reset_key()
#for x in range(87):
#    print(x,' ', keymin[x])
#    individual(x, keymin[x], 2)
individual(46, 450, 5)
#testing()