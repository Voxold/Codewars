# Given a non-empty array of integers, return the result of multiplying.
# the values together in order. 

def grow(arr):
    result = 1
    for i in arr :
        result *= i
    return result

print(grow([5,4,3,2,1]))
print(grow([1,2,3,4,5]))