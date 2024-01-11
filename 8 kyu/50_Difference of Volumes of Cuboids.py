# Your function will be tested with pre-made examples as well as random ones.

# Method 1 :
def find_difference(a, b):
    v1 = 1
    v2 = 1
    for number1 in a :
        v1 *= number1
    for number2 in b :
        v2 *= number2
    
    return abs(v1 - v2)
print(find_difference([3, 2, 5], [1, 4, 4])) # 14
print(find_difference([9, 7, 2], [5, 2, 2])) # 106

# abs method to convert positive to negative