
# 1 - covert string to list
# 2 - reverse the list
# 3- convert the reversed list to string

def reverse_words (s):

    the_list = s.split(' ')
    revers_list = the_list[::-1]
    convert = ' '.join(revers_list)

    return convert

print(reverse_words("The greatest victory is that which requires no battle"))
    
# ------------------- Short Solution -------------

def reverse_words (s):

    #the_list = s.split(' ')
    #revers_list = the_list[::-1]
    #convert = ' '.join(revers_list)

    return ' '.join(s.split(' ')[::-1])

print(reverse_words("The greatest victory is that which requires no battle"))