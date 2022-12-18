import time
import board
import neopixel
import random

NUMPIXELS = 2500
MaxBright = 50
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)

while True:
	for k in range(0, 40):
		color = (random.randint(0,MaxBright),random.randint(0,MaxBright),random.randint(0,MaxBright))
		for j in range(1,20):
			for i in range(0, NUMPIXELS):
				pixels[i] = (color[0]/j, color[1]/j, color[2]/j)
			pixels.show()
			time.sleep(0.01)
