import board
import neopixel

NUMPIXELS = 30
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)
color = [255, 255, 255]

for i in range(0, NUMPIXELS):
	pixels[i] = color
pixels.show()
