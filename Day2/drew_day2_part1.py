#Day 2 of AoC2024

with open("day2_input.txt", "r") as f:
	safeSum = 0
	for line in f:
		print(line)
		#print("Entering a new line")
		#We have our list of numbers, iterate through them checking for constant increase/decrease
		#or differences > 2

		safe = True
		increase = None
		index = 0
		oldValue = 0
		currValue = 0
		line = line.split(" ")
		while index < len(line):
			currValue = int(line[index].strip().strip("\n"))
			#print(currValue)
			
			#skip our first value
			if index == 0:
				oldValue = currValue
				index += 1
				continue
			
			index += 1

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
				print("We were not safe - we didn't move")
				safe = False
				break
			elif increase and result < 0:
				print("We were not safe - went down instead of up")
				safe = False
				break
			#if we should be moving down but didn't move or went up
			elif not increase and result > 0:
				print("We were not safe - went up instead of down")
				safe = False
				break

			#if we jumped more than 2, its unsafe. Mark it as such and break.
			if abs(result) > 3:
				print("Jump too big")
				safe = False
				break
			
		if safe:
			print("We are safe")
			safeSum += 1
			

print(safeSum)
