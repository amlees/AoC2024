import re
#Day 4 of AOC 2024
#valid examples we need to check for
#..XMAS..
#..SAMX..

#X
#.M
#..A
#...S

# S
# .A
# ..M
# ...X

#....S
#...A
#..M
#X

#...X
#..M
#.A
#S


downRightDirections = [ \
#Down to the right
(1,1,'M'),
(2,2,'A'),
(3,3,'S')
]
upLeftDirections = [\
#Up to the left
(-1,-1,'M'),
(-2,-2,'A'),
(-3,-3,'S'),
]

upRightDirections = [\
#Up to the Right
(1,-1,'M'),
(2,-2,'A'),
(3,-3,'S'),
]

downLeftDirections = [\
#Up to the left
(-1,1,'M'),
(-2,2,'A'),
(-3,3,'S'),
]

downDirections = [\
#Just down
(0,1,'M'),
(0,2,'A'),
(0,3,'S'),
]

upDirections = [\
#Just up
(0,-1,'M'),
(0,-2,'A'),
(0,-3,'S'),
]



#there has to be a better way than this - this is dumb
regexSAMX = r"SAMX"
regexXMAS = r"XMAS"

#print(len(match))

y = 0
matrix = [[0 for x in range(140)] for y in range(140)]
#print(matrix)
totalXmas = 0
with open("day4_input.txt", "r") as f:

	for line in f:
		x = 0
		line = line.strip("\n")
		match = re.findall(regexSAMX,line)
		totalXmas += len(match)
		match = re.findall(regexXMAS,line)
		totalXmas += len(match)

		while x < len(line):
			matrix[x][y] = line[x].strip("\n")
			x += 1
		y += 1

	smallYBound = 3
	largeYBound = len(matrix) - 4

	smallXBound = 3
	largeXBound = len(matrix) - 4
	totalDownRight = 0
	totalDownLeft = 0
	totalUpRight = 0
	totalUpLeft = 0
	totalDown = 140
	totalUp = 0
	print("TotalRegex: ", totalXmas)
	for x in range(len(matrix)):
		for y in range(len(matrix)):
			
			if matrix[x][y] == "X":
				good = 0
				#downRight
				if x <= largeXBound and y <= largeYBound:
					for xDelta,yDelta,character in downRightDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 3:
						totalXmas += 1
						totalDownRight += 1

				good = 0
				#downLeft
				if x >= smallXBound and y <= largeYBound:
					for xDelta,yDelta,character in downLeftDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 3:
						totalXmas += 1
						totalDownLeft += 1

				good = 0
				if x >= smallXBound and y >= smallYBound:
				#upLeft
					for xDelta,yDelta,character in upLeftDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 3:
						totalXmas += 1
						totalUpLeft += 1

				good = 0
				if x <= largeXBound and y >= smallYBound:
				#upRight
					for xDelta,yDelta,character in upRightDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 3:
						totalXmas += 1
						totalUpRight += 1

				good = 0
				if y >= smallYBound:
				#Up
					for xDelta,yDelta,character in upDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 3:
						totalXmas += 1
						totalUpLeft += 1

				good = 0

				if y <= largeYBound:
				#Down
					for xDelta,yDelta,character in downDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 3:
						totalXmas += 1
						totalUpRight += 1
print(totalXmas)

print("Total: ",totalXmas)
print("totalUpRight: ", totalUpRight)
print("totalUpLeft: ", totalUpLeft)
print("totalDownLeft: ", totalDownLeft)
print("totalDownRight: ", totalDownRight)