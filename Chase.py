import neopixel
import board
import time

NUMPIXELS = 30
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)
color = [255, 0, 255]

while True:
	for j in range(0, NUMPIXELS):
		for i in range(0, NUMPIXELS):
			if i==j:
				pixels[i] = color
			else:
				pixels[i] = [0,0,0]
		pixels.show()
		time.sleep(0.1)
