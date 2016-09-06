# A solution for the "printing a matrix in spiral" problem
# Source: http://stackoverflow.com/questions/726756/print-two-dimensional-array-in-spiral-order
# Algorithm
# 1. Pop top row
# 2. Transpose and flip upside-down (same as rotate 90 degrees counter-clockwise)
# 3. Go to 1


import itertools

arr = [
        [1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7]
    ]

def transpose_and_yield_top(arr):
    while arr:
        yield arr[0]
        arr = list(reversed(zip(*arr[1:])))

print list(itertools.chain(*transpose_and_yield_top(arr)))