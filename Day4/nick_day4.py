import numpy as np

from scipy.signal import convolve2d, correlate

data_list = []
with open("day4_input.txt", "r") as fptr:
    while line := fptr.readline():
        current_line = np.array([ord(x) for x in line.strip("\n")])
        data_list.append(current_line)
data_array = np.array(data_list)

number_of_matches = 0

def compute_matches(data_list, kernel):
    match_value = np.max(correlate(kernel, kernel, mode="same"))
    x = correlate(data_list, kernel, mode="full", method="fft")
    return np.sum(np.isclose(x, match_value))

# Non-Diagonal Kernels
kernel = np.zeros(data_array.shape)
kernel[0:4, 0] = np.array([ord(x) for x in "XMAS"])
number_of_matches += compute_matches(data_list, kernel) # Vertical
number_of_matches += compute_matches(data_list, np.rot90(kernel, 1)) # Horizontal
number_of_matches += compute_matches(data_list, np.rot90(kernel, 2)) # Reverse Vertical
number_of_matches += compute_matches(data_list, np.rot90(kernel, 3)) # Reverse Horizontal

# Diagonal Kernels
kernel = np.zeros(data_array.shape)
kernel[0, 0] = ord("X")
kernel[1, 1] = ord("M")
kernel[2, 2] = ord("A")
kernel[3, 3] = ord("S")
number_of_matches += compute_matches(data_list, kernel) # TL to BR
number_of_matches += compute_matches(data_list, np.rot90(kernel, 1)) # BL to TR
number_of_matches += compute_matches(data_list, np.rot90(kernel, 2)) # BR to TL
number_of_matches += compute_matches(data_list, np.rot90(kernel, 3)) # TR to BL

print(f"Part One Answer: {number_of_matches}")

# Part Two
number_of_matches = 0
kernel = np.zeros(data_array.shape)
kernel[0, 0] = ord("M")
kernel[1, 1] = ord("A")
kernel[2, 2] = ord("S")
kernel[0, 2] = ord("M")
kernel[2, 0] = ord("S")
number_of_matches += compute_matches(data_list, kernel)
number_of_matches += compute_matches(data_list, np.rot90(kernel, 1))
number_of_matches += compute_matches(data_list, np.rot90(kernel, 2))
number_of_matches += compute_matches(data_list, np.rot90(kernel, 3))

print(f"Part Two Answer: {number_of_matches}")
