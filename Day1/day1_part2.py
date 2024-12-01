#Day 1 of AoC 2024


f=open("Day1input.txt","r")

firstList = []
secondList = {}
for line in f:
	value1,value2=line.strip("\n").split("   ")
	firstList.append(int(value1))
	if int(value2) not in secondList:
		secondList[int(value2)] = 1
	else:
		secondList[int(value2)] += 1


similarityScore = 0

for x in firstList:
	tempSimScore = 0
	if x in secondList:
		multiplier = secondList[x]
	else:
		multiplier = 0
	tempSimScore = x * multiplier
	similarityScore += tempSimScore

print(similarityScore)