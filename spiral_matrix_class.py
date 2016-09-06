# A solution for the "printing a matrix in spiral" problem
# Source: http://stackoverflow.com/questions/726756/print-two-dimensional-array-in-spiral-order
# Algorithm
# 1. Pop top row
# 2. Transpose and flip upside-down (same as rotate 90 degrees counter-clockwise)
# 3. Go to 1


import itertools

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def transponse_and_yield_top(self, arr):
        while arr:
            yield arr[0]
            arr = list(reversed(zip(*arr[1:])))
    
    def spiralOrder(self, A):
        ## Actual code to populate result
        result = list(itertools.chain(*self.transponse_and_yield_top(A)))
            
        return result

arr = [
        [1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7]
    ]

obj = Solution()
z = obj.spiralOrder(arr)
print z