import time
import board
import neopixel
import random

NUMPIXELS = 40
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)

Palette = [
	[255,0,0],
	[0,255,0],
	[0,0,255],
	[128,128,0],
	[0,128,128],
	[128,0,128]
]

buffer = [0]*2*NUMPIXELS

def gradient(i):
	r = Color_1[0]*(NUMPIXELS-i)/NUMPIXELS + Color_2[0]*i/NUMPIXELS
	g = Color_1[1]*(NUMPIXELS-i)/NUMPIXELS + Color_2[1]*i/NUMPIXELS
	b = Color_1[2]*(NUMPIXELS-i)/NUMPIXELS + Color_2[2]*i/NUMPIXELS
	return [r,g,b]

def randColor(excludes=[]):
	color = random.choice(Palette)
	while color in excludes:
		color = random. choice(Palette)
	return color


Color_1 = randColor()
Color_2 = randColor([Color_1])

for i in range(0, NUMPIXELS):
	buffer[i] = gradient(i)

index = NUMPIXELS-1

while True:
	if index%(NUMPIXELS-1) == 0:
		Color_1 = Color_2
		Color_2 = randColor([Color_1])

		for i in range(0, NUMPIXELS):
			buffer[NUMPIXELS+i] = gradient(i)
		index =0
		print (len(buffer))

	for i in range(0, NUMPIXELS):
		pixels[i] = buffer[i]
	for i in range(0, len(buffer)-1):
		buffer[i] = buffer[i+1]
	pixels.show()
	time.sleep(0.25)
	index += 1

