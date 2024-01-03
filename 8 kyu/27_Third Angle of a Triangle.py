# You are given two interior angles (in degrees) of a triangle.
# 
# Write a function to return the 3rd.
# 
# Note: only positive integers will be tested.
# 
# https://en.wikipedia.org/wiki/Triangle


def other_angle(a, b):
    return 180 - (a + b)

print(other_angle(60, 30))
print(other_angle(40, 50))
print(other_angle(10, 10))