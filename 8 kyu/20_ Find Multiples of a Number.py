#  Find Multiples of a Number

# 1 - First Method : 
def find_multiples(integer, limit):
    result = []
    x = 1 
    while x <= int(limit /integer):
        result.append(integer * x)
        x += 1
    return result

print(find_multiples(2,6))
print(find_multiples(2,7))
print(find_multiples(5,21))

# 2 - Second Method : 
def find_multiples(integer, limit):
    return list(range(integer,limit + 1, integer))

print(find_multiples(2,6))
print(find_multiples(2,7))
print(find_multiples(5,21))