import time
import board
import neopixel
import random

NUMPIXELS = 300
MaxBright = 50
MaxWalk = 1
pixels = neopixel.NeoPixel(board.D18, NUMPIXELS, auto_write=False)

def randWalk(value):
	value += random.randint(-MaxWalk,MaxWalk)
	if (value>MaxBright):
		value = MaxBright
	if (value<0):
		value = 0
	return value

randR = random.randint(0,MaxBright)
randG = random.randint(0,MaxBright)
randB = random.randint(0,MaxBright)

for i in range(0,NUMPIXELS):
	pixels[i] = [randR, randB, randB]
	randR = randWalk(randR)
	randG = randWalk(randG)
	randB = randWalk(randB)
pixels.show()

while True:
	for i in range(0, NUMPIXELS):
		pixels[i] = (randWalk(pixels[i][0]), randWalk(pixels[i][1]),randWalk(pixels[i][2]))
	pixels.show()
	time.sleep(0.25)
