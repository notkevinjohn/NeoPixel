import neopixel
import board
import time
import random

NUMPIXELS = 40
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)
colors = [
	[255, 0, 0],
	[0, 255, 0],
	[0, 0, 255],
	[0, 255, 255],
	[255, 0, 255],
	[255, 255, 0],
]

while True:
	randomIndex = random.randint(0,len(colors))
	print (randomIndex)

	for i in range(0, NUMPIXELS):
		pixels[i] = colors[0]
	pixels.show()
	time.sleep(1)
	for i in range(0, NUMPIXELS):
		pixels[i] = [0,0,0]
	pixels.show()
	time.sleep(1)
	pixels.show()




