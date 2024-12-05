#Day 5 of AoC 2024

from collections import defaultdict
import math
rulesDict = defaultdict(list)
nextData = False
total = 0
goodBooks = []
with open("day5_input.txt", "r") as f:

	for line in f:

		if line == "\n":
			nextData = True
			continue

		#Create a dict where the key is value is a list of numbers that must've come before the key.

		if not nextData:
			value,key = line.split("|")
			value = int(value.strip().strip("\n"))
			key = int(key.strip().strip("\n"))

			rulesDict[key].append(value)
		else:
			book = line.split(",")
			book = [int(s.strip()) for s in book]
			x = 0
			badBook = False
			#Maintain two pointers, one to our current value, one to the rest of the values to check against our rules
			#As we find a number in our list, we know it's to the right of our current value (the key), swap them and start evaluating our rules over again
			while x < len(book):
				y = x
				currVal = book[x]
				while y < len(book):
					if book[y] in rulesDict[currVal]:
						badBook = True
						break
					y += 1
				x += 1
				if badBook:
					break
			if not badBook:
				goodBooks.append(book)

for book in goodBooks:
	middleIndex = math.ceil(len(book)/2)
	total += book[middleIndex-1]


print(total)
