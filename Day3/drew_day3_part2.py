#Day 3 of AoC 2024
import re
def findValidString(inputstr,validStr,multiply):
	regex2 = r"do\(\)"
	regex3 = r"don\'t\(\)"
	# print("Should we multiply?", multiply)
	# print("inputstr: %s"%inputstr)
	# print()
	# print("validStr: %s"%validStr)
	# print()
	# print()

	#we reached the end, just return our valid string.
	if len(inputstr) == 0:
		print("returning: %s"%validStr)
		return validStr, multiply

	dontMatch = re.search(regex3, inputstr)
	doMatch = re.search(regex2, inputstr)

	#If multiply is true, the start of the string until the first don't is valid
	#take that portion and pass it along
	if multiply and dontMatch:
		validStr += inputstr[:dontMatch.start()]
		returnStr, returnMult = findValidString(inputstr[dontMatch.end():], validStr, False)
	#If multiply is not true, the start of the string until the first do should be thrown away
	#remove everything up until the first do
	elif not multiply and doMatch:
		#print("We had a do match")
		returnStr, returnMult = findValidString(inputstr[doMatch.end():], validStr, True)

	#If we should ignore the string and there isn't any more "do()", return what we have because we can ignore the rest
	if not multiply and not doMatch:
		return validStr, multiply
	#If we should use the string and there isn't any more "don't()", return our valid string as well as the rest of the string
	elif multiply and not dontMatch:
		validStr += inputstr
		return validStr, multiply

	return returnStr, returnMult

with open("day3_input.txt", "r") as f:

	regex = r"mul\((\d+,\d+)\)"
	total = 0
	multiply = True
	for line in f:
		#227067189 too high
		validStr, multiply = findValidString(line,"",multiply)
		#print("final valid str: %s" %validStr)
		#print("Do we multiply the next?", multiply)
		#print()
		x = re.findall(regex,validStr)
		for values in x:
			value1,value2 = values.split(",")
			total += int(value1) * int(value2)

print(total)





#If we are able to multiply, find the str from start of string to first don't
#If we aren't able to multiply, find the str from start of string to first do
#If at the end we aren't able to multiply, return an empty string