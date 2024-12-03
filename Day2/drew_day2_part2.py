#Day 2 of AoC2024
#Day 2, part 2
#Same as part 1 except if a line is unsafe, you need to evaluate if it COULD be safe upon the removal of
#at most 1 element
#fuck using .copy
def safeEval(line):
	increase = None
	index = 0
	oldValue = 0
	currValue = 0
	#print(line)
	while index < len(line):
		currValue = int(line[index].strip().strip("\n"))
		##print(currValue)
		
		#skip our first value
		if index == 0:
			oldValue = currValue
			index += 1
			continue
		
		

		#Need this to check if we're consistently increasing or decreasing
		result = currValue - oldValue
		oldValue = currValue

		#It's possible we didn't increase or decrease so we need to continously check this until
		#we find which direction we're moving in. Can't just check this for the first two values
		if increase is None:
			if result > 0:
				increase = True
			elif result < 0:
				increase = False

		#if we should be moving up but didn't move or went down
		if result == 0:
			#print("We were not safe - we didn't move")
			return False, index
		elif increase and result < 0:
			#print("We were not safe - went down instead of up")
			return False, index
		#if we should be moving down but didn't move or went up
		elif not increase and result > 0:
			#print("We were not safe - went up instead of down")
			return False, index

		#if we jumped more than 2, its unsafe. Mark it as such and break.
		if abs(result) > 3:
			#print("Jump too big")
			return False, index

		index += 1
	return True, 0

with open("day2_input.txt", "r") as f:
	safeSum = 0
	for line in f:
		line = line.split(" ")

		safe, badIndex = safeEval(line)
		if safe:
			#print("We are safe")
			print(line)
			safeSum += 1
		else:
			#None of this makes sense and I just hacked it together until it worked
			#We are not safe, remove the offending element (and every element there on out)
			#to see if we can ever make it safe.
			badLine = line.copy()
			#Try a greedy approach to just delete the index we had a problem with
			del badLine[badIndex]
			#If its now safe, we are good
			safe, badIndex = safeEval(badLine)
			if safe:
				#print("We are now safe by removing the bad index")
				print(badLine)
				safeSum += 1
			else:
				#Our greedy approach didn't work, iterate through the list one index
				#at a time removing each element to see if its every safe
				#print("Greedy solution didn't work, checking every index")
				badIndex2 = 0
				while badIndex2 < len(line) - 1:
					badLine = line.copy()
					del badLine[badIndex2]
					#We found a safe line, break.
					safe, badIndex = safeEval(badLine)
					if safe:
						##print("we are now safe by removing index: %s"%badIndex2)
						print(badLine)
						safeSum += 1
						break
					badIndex2 += 1


print(safeSum)
