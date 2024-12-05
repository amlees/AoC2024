#Day 5 of AoC 2024

from collections import defaultdict
import math
rulesDict = defaultdict(list)
nextData = False
total = 0
badBooks = []
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
			dontIncrement = False
			#Maintain two pointers, one to our current value, one to the rest of the values to check against our rules
			#As we find a number in our list, we know it's to the right of our current value (the key), swap them and start evaluating our rules over again
			while x < len(book):
				y = x
				currVal = book[x]
				while y < len(book):
					#if the number we're currently looking at is in our dict, it means we're to the right, swap our numbers
					if book[y] in rulesDict[currVal]:
						book[x] = book[y]
						book[y] = currVal
						#after our swap, move back to the start of the list as we may have invalidated other rules
						x = 0
						dontIncrement = True
						badBook = True
						break
					y += 1
				#Probably a better way to do this but when we set x to 0 to be at the beginning it was getting set to 1 immediately. don't do that.
				if dontIncrement == True:
					dontIncrement = False
				else:
					x += 1

			if badBook:
				badBooks.append(book)
for book in badBooks:
	middleIndex = math.ceil(len(book)/2)
	total += book[middleIndex-1]
