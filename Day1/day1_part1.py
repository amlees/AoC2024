#Day 1 of AoC 2024

f=open("Day1input.txt","r")

firstList = []
secondList = []
for line in f:
	value1,value2=line.strip("\n").split("   ")
	firstList.append(int(value1))
	secondList.append(int(value2))

firstList.sort()
secondList.sort()

index = 0
sumOfDifferences = 0

while index < len(firstList):
	difference = abs(firstList[index] - secondList[index])
	sumOfDifferences += difference
	index += 1

print(sumOfDifferences)