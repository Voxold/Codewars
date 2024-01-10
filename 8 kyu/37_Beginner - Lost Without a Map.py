# Given an array of integers, return a new array with each value doubled.

def maps(a):
    L = []
    for i in a :
        L.append(i * 2)
    return L

print(maps([1,2,3]))
print(maps([4,5,6]))
print(maps([10,20,30]))