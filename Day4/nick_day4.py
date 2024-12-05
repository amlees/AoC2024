import numpy as np

from scipy.signal import convolve2d, correlate

data_list = []
with open("day4_test.txt", "r") as fptr:
    while line := fptr.readline():
        current_line = np.array([ord(x) for x in line.strip("\n")])
        data_list.append(current_line)
data_array = np.array(data_list)

def compute_matches(data_list, kernel):
    match_value = np.max(correlate(kernel, kernel, mode="same"))
    x = correlate(data_list, kernel, mode="full", method="fft")
    return np.sum(np.isclose(x, match_value))

# Non-Diagonal Kernels
kernel = np.zeros(data_array.shape)
kernel[0:4, 0] = np.array([ord(x) for x in "XMAS"])
number_of_matches = sum([compute_matches(data_list, np.rot90(kernel, x)) for x in range(4)])

# Diagonal Kernels
kernel = np.zeros(data_array.shape)
kernel[0, 0] = ord("X")
kernel[1, 1] = ord("M")
kernel[2, 2] = ord("A")
kernel[3, 3] = ord("S")
number_of_matches += sum([compute_matches(data_list, np.rot90(kernel, x)) for x in range(4)])

print(f"Part One Answer: {number_of_matches}")

# Part Two
kernel = np.zeros(data_array.shape)
kernel[0, 0] = ord("M")
kernel[1, 1] = ord("A")
kernel[2, 2] = ord("S")
kernel[0, 2] = ord("M")
kernel[2, 0] = ord("S")
number_of_matches = sum([compute_matches(data_list, np.rot90(kernel, x)) for x in range(4)])

print(f"Part Two Answer: {number_of_matches}")
