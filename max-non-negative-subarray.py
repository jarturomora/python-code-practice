# Max Non Negative SubArray
# Find out the maximum sub-arrays of non negative numbers from an array.
# The sub-arrays should be continuous. That is, a sub-array created by choosing
# the second and fourth element and skipping the third element is invalid.
# You can find more than one sub-array in an array.

# Maximum sub-array is defined in terms of the sum of the elements in the
# sub-array. Sub-array A is greater than sub-array B if `sum(A) > sum(B)`.

# **Example:**

# ```
# A : [1, 2, 5, -7, 2, 3]
# The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3]
# ```

# **NOTE:** `If there is a tie, then compare with segment's length and return
# segment which has maximum length`
# **NOTE 2:** `If there is still a tie, then return the segment with minimum
# starting index`


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        s = []
        temp = []                
        for i in xrange(len(A)):            
            if (A[i] >= 0):
                #print A[i]
                temp.append(A[i])
            else:
                s.append(temp)
                temp = []
        if (temp not in s):
            s.append(temp)
        #print s
        #exit(0)
        s = [e for e in s if len(e) > 0]
        
        if (len(s) > 0):
            maxim = -1
            pos = -1
            for i in xrange(len(s)):
                if (sum(s[i]) > maxim):
                    pos = i
                    maxim = sum(s[i])            
            return s[pos]
        else:
            return s


#A = [1, 2, 5, -7, 2, 3]
#A = [0,0,-1,0]
#A = [ -846930886, -1714636915, 424238335, -1649760492 ]
#A = [1, 2, 5, -7, 2, 5]
#A = [ 336465782, -278722862, -2145174067, 1101513929, 1315634022, -1369133069, 1059961393, 628175011, -1131176229, -859484421 ] #1101513929 1315634022 = 1688136404
#A = [ -1, -1, -1, -1, -1 ]
#A = [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
A = [ 0, 0, -1, 0 ]
x = Solution()
print x.maxset(A)