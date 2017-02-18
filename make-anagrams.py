from collections import Counter

def find_diferent_chars(x, y, diferent_chars):	
	for i in xrange(len(x)):
		if x[i] not in y:
			diferent_chars.append(x[i])
		elif x[i] not in diferent_chars and y.count(x[i]) != x.count(x[i]):
			diferent_chars.append(x[i]*(abs(y.count(x[i]) - x.count(x[i]))))				
	return diferent_chars

def number_needed2(a, b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    #print a_sorted
    #print b_sorted
    #exit(0)
    if a_sorted == b_sorted:
    	return 0
    else:
    	diferent_chars = []
    	# not in a
    	diferent_chars = find_diferent_chars(a_sorted, b_sorted, diferent_chars)
    	#print diferent_chars    	
    	# not in b
    	diferent_chars = find_diferent_chars(b_sorted, a_sorted, diferent_chars)
    	#print diferent_chars
    	#exit(0)
    	#print sorted(diferent_chars)
    	return len(diferent_chars)

def number_needed(a, b):
	# https://pymotw.com/2/collections/counter.html
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())
    	
    	

#a = "bacdc"
#b = "dcbac"
#a = "cde"
#b = "abc"
a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

"""
fcrxzwscanmligyxyvym
jxwtrhvujlmrpdoqbisbwhmgpmeoke
30
"""

print number_needed(a, b)