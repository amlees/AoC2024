#Day 10 of Aoc 2024
import pprint

matrixSize = 45
matrix = [[0 for x in range(matrixSize)] for y in range(matrixSize)]
startingSpots = []

def walk(currY, currX):
  #Change from list to set() for part1
	totalTops = []
	mountainStack = []
	mountainStack.append((currY,currX))

	while len(mountainStack) > 0:
		currY,currX = mountainStack.pop()
		#North
		try:
			if (currY-1 >= 0) and matrix[currY-1][currX].isdigit() and int(matrix[currY-1][currX]) == int(matrix[currY][currX])+1:
				#Don't need to append the tops of the mountains to our stack
				if matrix[currY-1][currX] == '9':
					totalTops.append((currY-1,currX))
				else:
					#print("appending to the north")
					mountainStack.append((currY-1,currX))
		except:
			pass
		#South
		try:
			if (currY+1) < matrixSize and matrix[currY+1][currX].isdigit() and int(matrix[currY+1][currX]) == int(matrix[currY][currX])+1:
				if matrix[currY+1][currX] == '9':
					totalTops.append((currY+1,currX))
				else:
					#print("appending to the South")
					mountainStack.append((currY+1,currX))
		except:
			pass
		#West
		try:
			if (currX-1 >= 0) and matrix[currY][currX-1].isdigit() and int(matrix[currY][currX-1]) == int(matrix[currY][currX])+1:
				if matrix[currY][currX-1] == '9':
					totalTops.append((currY,currX-1))
				else:
					#print("appending to the West")
					mountainStack.append((currY,currX-1))
		except:
			pass
		#East
		try:
			if (currX+1) < matrixSize and matrix[currY][currX+1].isdigit() and int(matrix[currY][currX+1]) == int(matrix[currY][currX])+1:
				if matrix[currY][currX+1] == '9':
					totalTops.append((currY,currX+1))
				else:
					#print("appending to the East")
					mountainStack.append((currY,currX+1))
		except:
			pass
	return (len(totalTops))


with open("day10_intput.txt", "r") as f:
	y = 0
	for line in f:
		x = 0
		line = line.strip("\n")
		while x < len(line):
			#I did this backwards because my brain was not working for some reason.
			matrix[y][x] = line[x].strip("\n")
			#print("Putting %s in x: %s and y %s"%(line[x].strip("\n"),x,y))
			if line[x].strip("\n") == '0':
				startingSpots.append((y,x))
			x += 1
		y += 1
totalScore = 0
for y,x in startingSpots:
	totalScore += walk(y,x)
print(totalScore)
