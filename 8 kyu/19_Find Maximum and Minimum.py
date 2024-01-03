# max and min, or maximum and minimum, etc., depending on the language 

# Simple Method :
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([-52, 56, 30, 29, -54, 0, -110]))


# Reduce Method :
from functools import reduce

def minimum(arr):
    def m(a, b):
        return a if a < b else b
    result = reduce(m, arr)
    return result


def maximum(arr):
    def m(a, b):
        return a if a > b else b
    result = reduce(m, arr)
    return result

print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([-52, 56, 30, 29, -54, 0, -110]))

