import numpy as np
import re

with open("day3_input.txt", "r") as fptr:
    data = str(fptr.readlines())

substring_list = re.findall("mul\(\d+,\d+\)", data)
result = 0
for substring in substring_list:
    x, y = substring[4:-1].split(",")
    result += int(x) * int(y)

print(f"Part One Answer: {result}")

do_index_array = np.array([0] + [x.start(0) for x in re.finditer("do\(\)", data)])
dont_index_array = np.array([x.start(0) for x in re.finditer("don't\(\)", data)])
substring_match_list = [[x.start(0), x.group()[4:-1].split(",")] for x in re.finditer("mul\(\d+,\d+\)", data)]

substring_list = re.findall("mul\(\d+,\d+\)", data)

result = 0
for substring_match in substring_match_list:
    do_value = substring_match[0] - do_index_array
    do_value = np.min(do_value[do_value>0])

    dont_value = substring_match[0] - dont_index_array
    if any(dont_value > 0):
        dont_value = np.min(dont_value[dont_value>0])
        use_value = do_value < dont_value
    else:
        use_value = True

    if use_value:
        result += int(substring_match[1][0]) * int(substring_match[1][1])

print(f"Part Two Answer: {result}")
