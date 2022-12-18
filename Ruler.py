import neopixel
import board

NUMPIXELS = 100
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)

color10 = [255,0,0]
color = [0,0,255]

for i in range(0, NUMPIXELS):
	if i%10 == 0:
		pixels[i] = color10
	else:
		pixels[i] = color
pixels.show()

