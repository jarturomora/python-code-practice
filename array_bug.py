class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []        
        for i in xrange(len(a)-1):
            print "i: %d, p: %d" % (i, (i + b) % len(a))
            ret.append(a[(i + b) % len(a)])        
        return ret


A = [ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ]
B = 56
# 35 14 5 14 34 42 63 17 25 39 61 97 55 33 96 62 32 98 77 

# A = [1, 2, 3, 4, 5, 6]
# B = 1
# [2 3 4 5 6 1]


x = Solution()
print x.rotateArray(A, B)