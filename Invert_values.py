# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.



def invert(lst):
    inverted_list = []
    for n in lst :
        inverted_list.append(-n)
    return inverted_list

print(invert([1,2,3,4,5]))
print(invert([1,-2,3,-4,5]))
print(invert([]))