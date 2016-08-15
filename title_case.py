################################################################################
# Kata: Title Clase
#
# A string is considered to be in title case if each word in the string is
# either (a) capitalised (that is, only the first letter of the word is in
# upper case) or (b) considered to be an exception and put entirely into lower
# case unless it is the first word, which is always capitalised.
#
# Write a function that will convert a string into title case, given an optional
# list of exceptions (minor words). The list of minor words will be given as a
# string with each word separated by a space. Your function should ignore the
# case of the minor words string -- it should behave in the same way even if
# the case of the minor word string is changed.
#
# Arguments (Other languages)
#  * First argument (required): the original string to be converted.
#  * Second argument (optional): space-delimited list of minor words that must
#    always be lowercase except for the first word in the string.
#
# Example
# title_case('a clash of KINGS', 'a an the of')
#   should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In')
#   should return: 'The Wind in the Willows'
# title_case('the quick brown fox')
#   should return: 'The Quick Brown Fox'
################################################################################
def title_case(title, minor_words = ''):
    title = title.title()
    if minor_words != '':
        minor_words = minor_words.lower()
        exceptions = minor_words.split()
        input_words = title.split()        
        for index, word in enumerate(input_words):            
            if word.lower() in exceptions and index != 0:
                # print "Exception found: %s" % (word)
                input_words[index] = word.lower()
        title = ' '.join(input_words)        
    return title

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    test(title_case(''), '')
    test(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
    test(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
    test(title_case('the quick brown fox'), 'The Quick Brown Fox')
    
if __name__ == '__main__':
    main()