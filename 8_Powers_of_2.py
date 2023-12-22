# Complete the function that takes a non-negative integer n as input, 
# and returns a list of all the powers of 2 with the exponent ranging 
# from 0 to n ( inclusive ).

# method 1 : 'while loop'
def powers_of_two(n):
    result = []
    x = 0
    while x <= n :
        result.append(pow(2,x))
        x += 1
    return result

print(powers_of_two(5))

# method 2 : 'for loop'
def powers_of_two(n):
    result = []
    x = 0
    for x in range(n + 1) :
        result.append(pow(2,x))
    return result

print(powers_of_two(5))
