import neopixel
import board
import time

NUMPIXELS = 40
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)
colors = [
	[255, 0, 0],
	[0, 255, 0],
	[0, 0, 255],
	[0, 255, 255],
	[255, 0, 255],
	[255, 255, 0],
	[0,0,0]
]

for color in colors:
	for i in range(0, NUMPIXELS):
		pixels[i] = color
	pixels.show()
	time.sleep(1)



