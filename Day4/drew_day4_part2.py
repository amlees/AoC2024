import re
#Day 4 of AOC 2024
#valid examples we need to check for
#..XMAS..
#..SAMX..

# S.S
# .A.
# M.M

# M.M
# .A.
# S.S

# S.M
# .A.
# S.M

# M.S
# .A.
# M.S

#good name
oneDirections = [ \
#Sam Down Right, Sam Down Left
(-1,-1,'S'),
(1,-1,'S'),
(-1,1,'M'),
(1,1,'M')
]
twoDirections = [\
#Sam Up Right, Sam Up Left
(-1,-1,'M'),
(1,-1,'M'),
(-1,1,'S'),
(1,1,'S')
]

threeDirections = [\
#Sam Down Right, Sam Up Right
(-1,-1,'S'),
(1,-1,'M'),
(-1,1,'S'),
(1,1,'M')
]

fourDirections = [\
#Sam Down Left, Sam Up Left
(-1,-1,'M'),
(1,-1,'S'),
(-1,1,'M'),
(1,1,'S')
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

		while x < len(line):
			matrix[x][y] = line[x].strip("\n")
			x += 1
		y += 1

	smallYBound = 1
	largeYBound = len(matrix) - 2

	smallXBound = 1
	largeXBound = len(matrix) - 2

	totalOne = 0
	totalTwo = 0
	totalThree = 0
	totalFour = 0

	for x in range(len(matrix)):
		for y in range(len(matrix)):
			
			if matrix[x][y] == "A":
				good = 0
				#downRight
				if x <= largeXBound and y <= largeYBound and x >= smallXBound and y >= smallYBound:
					for xDelta,yDelta,character in oneDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 4:
						totalXmas += 1
						totalOne += 1

					good = 0

					for xDelta,yDelta,character in twoDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 4:
						totalXmas += 1
						totalTwo += 1
						

					good = 0

					for xDelta,yDelta,character in threeDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 4:
						totalXmas += 1
						totalThree += 1
						

					good = 0

					for xDelta,yDelta,character in fourDirections:
						if matrix[x + xDelta][y + yDelta] == character:
							good += 1
					if good == 4:
						totalXmas += 1
						totalFour += 1
						



print("Total: ",totalXmas)
print("totalOne:", totalOne)
print("totalTwo:", totalTwo)
print("totalThree:", totalThree)
print("totalFour:", totalFour)