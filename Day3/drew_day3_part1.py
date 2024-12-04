#Day 3 of AoC 2024
import re
with open("day3_input.txt", "r") as f:

	regex = r"mul\((\d+,\d+)\)"
	total = 0
	for line in f:
		x = re.findall(regex,line)
		for values in x:
			value1,value2 = values.split(",")
			total += int(value1) * int(value2)
print(total)
