from math import sin, tan, pi
import sys

def distance(x1, y1, x2, y2):
	return ((x1 - x2)**2 + (y1 - y2) ** 2)**0.5

def getCenter(x1, y1, x2, y2, x3, y3):
	cx = (x1 ** 2 - x2 ** 2 + y1**2 - y2**2) * (y1 - y3)
	cx -= (x1**2 - x3**2 + y1 ** 2 - y3 ** 2) * (y1 - y2)
	cx /= 2 * ((x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2))

	cy = (x1 ** 2 - x2 ** 2 + y1**2 - y2**2 - 2 * cx * (x1 - x2)) / (2 * (y1 - y2))

	return cx, cy

def getAreas(x1, y1, x2, y2, x3, y3):
	# For each n sided polygon
	cx, cy = getCenter(x1, y1, x2, y2, x3, y3) # Center
	r = distance(x1, y1, cx, cy) # Radius

	areas = []

	for n in range(3, 101):
		theta = pi / n
		a = r * sin(theta) # apothem
		s = 2 * a / tan(theta) # side length
		p = n * s # Perimeter
		area = 0.5 * p * a # Area of n sided polygon
		areas.append(area)
	return areas

def getInput(inputFileName):
	lines = []
	with open(inputFileName, "r") as f:
		lines = f.read().split("\n")

	points = []
	for line in lines: 
		points.extend(line.split(" "))

	points = [float(point) for point in points]

	return points


'''
The program works in the following manner:
1. The center is found by finding the common intersection point of all the circles from each point at an unknown distance.
2. Then the center is used to find the area using the formula for a regular polygon for n sides where n is from 3 to 100.
3. The minimum of all the areas possible is given as the answer.
'''

# The link to the desmos page explaining all the math
# https://www.desmos.com/calculator/smvzh6tij8

defaultFileName = "input.txt"
try:
	fileName = sys.argv[1]
except IndexError:
	fileName = defaultFileName

p = getInput(fileName)
areas = getAreas(*p)

print(min(areas))