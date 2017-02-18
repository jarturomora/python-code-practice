def array_left_rotation(a, n, k):    
    tmp = [0 for item in a]    
    for i in xrange(n):        
        tmp[i - k] = a[i]
    return tmp

n, k = map(int, "5 4".split(' '))
a = map(int, '1 2 3 4 5'.split(' '))
print "n:%r, k:%r, a:%r \n" % (n, k, a)
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))