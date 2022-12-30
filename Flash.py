import time
import board
import neopixel

NUMPIXELS = 3000
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)
color = [255, 255, 255]

while True:
	for i in range(0, NUMPIXELS):
		pixels[i] = color
	pixels.show()
	for i in range(0, NUMPIXELS):
		pixels[i] = [0,0,0]
	pixels.show()
