import time
import board
import neopixel
import random

NUMPIXELS = 40
MaxBright = 25
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)

while True:
	color = (random.randint(0,MaxBright),random.randint(0,MaxBright),random.randint(0,MaxBright))
	for i in range(0, NUMPIXELS):
		pixels[i] = (color[0]/10, color[1]/10, color[2]/10)


	for k in range(0, 10):
		for j in range(1,20):
			for i in range(0, NUMPIXELS):
				twinkle = random.randint(0,100)
				if twinkle == 100:
					pixels[i] = (color[0], color[1], color[2])
					pixels.show()
					time.sleep(0.01)
					pixels[i] = (color[0]/10, color[1]/10, color[2]/10)

