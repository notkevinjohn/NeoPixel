import time
import board
import neopixel
import random

NUMPIXELS = 100
MaxBright = 50
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)
pixels.fill([0,0,0])
index = 0

while True:
	if index%4 == 0:
		color = (random.randint(0,MaxBright),random.randint(0,MaxBright),random.randint(0,MaxBright))
	else:
		color = [0,0,0]
	pixels[0] = color
	pixels.show()
	for i in range(1, NUMPIXELS+1):
			j = NUMPIXELS - i 
			pixels[j] = pixels[j-1]
	index += 1
