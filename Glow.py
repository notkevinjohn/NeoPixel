import neopixel
import board
import time
import numpy as np

NUMPIXELS = 40
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)
color = [255, 255, 255]

while True:
	#Fade Up
	for j in range(0, 100):
		for i in range(0, NUMPIXELS):
			pixels[i] = np.array(color)*(j/100)
		pixels.show()
		time.sleep(0.05)

	#Fade Back Down
	for j in range(0, 100):
		for i in range(0, NUMPIXELS):
			pixels[i] = np.array(color)*(1-j/100)
		pixels.show()
		time.sleep(0.05)

