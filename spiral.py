# create array of numbers spiralling outwards, clockwise

import numpy as np

# only odd number matrices to keep 1 in center

N = 7

a = np.zeros((N, N))

a[N // 2, N // 2] = 1

box_length = 1

while box_length < N:

    box_length += 2

    offset = box_length // 2 - 1

    center = N // 2

    M = box_length // 2

    col = np.arange(-M, M + 1, 1)
    row = np.arange(-M, M + 1, 1)

    print(center)

    start = (box_length - 2) * (box_length - 2) + 1
    stop = box_length * box_length

    numbers = [i for i in range(start, stop + 1)]

    n_digits = box_length - 1

    a[center - offset:center + M + 1, center + M] = np.array(numbers[:box_length - 1])

    a[center + M, center - M:center + M] = np.array(numbers[box_length - 1:2 * (box_length - 1)][::-1])

    a[center - M:center + M, center - M] = np.array(numbers[2 * (box_length - 1):3 * (box_length - 1)][::-1])

    a[center - M, center - M:center + M + 1] = np.array(numbers[3 * (box_length - 1) - 1:])


print(a)
