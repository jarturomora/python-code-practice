# This is a code for testing the use of yield as a generator.
# I found a great reference here:
# http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()
print(mygenerator)
for i in mygenerator:
    print(i)