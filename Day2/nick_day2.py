import numpy as np

from copy import deepcopy
from typing import List

def check_report(report: List):
    report_diff = np.diff(report)
    
    is_increasing_decreasing = all(report_diff > 0) or all(report_diff < 0)
    is_differ = all([x >= 1 and x <= 3 for x in np.abs(report_diff)])

    return is_increasing_decreasing and is_differ


def check_report_two(report: List):
    report_diff = np.diff(report)

    is_increasing = list(report_diff > 0)
    is_decreasing = list(report_diff < 0)
    diff_list = is_increasing if sum(is_increasing) > sum(is_decreasing) else is_decreasing

    is_differ = ([x >= 1 and x <= 3 for x in np.abs(report_diff)])

    valid_list = [x and y for x, y in zip(diff_list, is_differ)]
    bad_index_list = [index for index in range(len(valid_list)) if not valid_list[index]]
    if len(bad_index_list) == 0:
        return True
    else:
        problem_dampener_list = []
        for bad_index in bad_index_list:
            temp_report = deepcopy(report)
            temp_report.pop(bad_index)
            problem_dampener_list.append(check_report(temp_report))

            temp_report = deepcopy(report)
            temp_report.pop(bad_index + 1)
            problem_dampener_list.append(check_report(temp_report))

    return any(problem_dampener_list)


report_list = []
with open("day2_input.txt", "r") as fptr:
    while line := fptr.readline():
        report_list.append([int(x) for x in line.strip("\n").split()])

valid_list = [check_report(report) for report in report_list]
print(f"Part One Answer: {sum(valid_list)}")

bad_report_list = [report for index, report in enumerate(report_list) if not valid_list[index]]
problem_dampener_list = [check_report_two(bad_report) for bad_report in bad_report_list]
print(f"Part Two Answer: {sum(valid_list) + sum(problem_dampener_list)}")
