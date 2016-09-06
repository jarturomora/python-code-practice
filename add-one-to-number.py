# Given a non-negative number represented as an array of digits,
# add 1 to the number ( increment the number represented by the digits ).
# The digits are stored such that the most significant digit is at the head
# of the list.

# Example:
# If the vector has [1, 2, 3]
# the returned vector should be [1, 2, 4]
# as 123 + 1 = 124.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        num = int(''.join(str(e) for e in A))
        num = num + 1
        s = str(num)
        res = [int(e) for e in s]
        return res

x = Solution()
print x.plusOne([9,9,9])
#assert x.plusOne([1,2,3]) == [1,2,4]