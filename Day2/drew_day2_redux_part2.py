#Day 2 of AoC2024
#Day 2, part 2
#Same as part 1 except if a line is unsafe, you need to evaluate if it COULD be safe upon the removal of
#at most 1 element
#fuck using .copy
def valueEval(value1, value2, increase):
	newResult = value2 - value1
	print("VAlue2: %s, Value1: %s, increase: %s"%(value2, value1, increase))
	#if we should be moving up but didn't move or went down
	if newResult == 0:
		print("We were not safe - we didn't move")
		return False
	elif increase and newResult < 0:
		print("We were not safe - went down instead of up")
		return False
	#if we should be moving down but didn't move or went up
	elif not increase and newResult > 0:
		print("We were not safe - went up instead of down")
		return False

	#if we jumped more than 2, its unsafe. Mark it as such and break.
	elif abs(newResult) > 3:
		print("Jump too big")
		return False
	else:
		return True

def safeEval(line):
	increase = None
	index = 0
	oldValue = 0
	currValue = 0
	failCount = 0
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

		#It's possible we didn't increase or decrease so we need to continously check this until
		#we find which direction we're moving in. Can't just check this for the first two values
		if increase is None:
			if result > 0:
				increase = True
			elif result < 0:
				increase = False
		#if our current v alue and next value are Going to faile
		if not valueEval(oldValue,currValue, increase):
			print("We failed")
			failCount += 1
			#If we can look next value + 1 ahead
			if index + 1 < len(line):
				newValue = int(line[index + 1])
				#If our current value and next + 1 value fails
				newResult = newValue - oldValue
				if newResult > 0:
					increase = True
				elif newResult < 0:
					increase = False
				if not valueEval(oldValue,newValue,increase):
					#Even if we removed the one problem value, we would still fail
					return False
				oldValue = newValue
			index += 1
		else:
			oldValue = currValue

		if failCount > 1:
			return False

		index += 1
	return True

with open("day2_input.txt", "r") as f:
	safeSum = 0
	for line in f:
		line = line.split(" ")
		line = ['12', '10', '13', '16', '19', '21', '22\n']

		safe = safeEval(line)
		if safe:
			safeSum += 1
		else:
			print(line)
		break



print(safeSum)
