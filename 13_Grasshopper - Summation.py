# Write a program that finds the summation of every number from 1 to num.

# Method 1 :
def summation(num): 
    result = 0
    for i in range(1, num + 1):
        result += i
    return result
    
print(summation(2))
print(summation(8))
print(summation(4))

# Method 2 :
def summation(num): 
    return sum(range(1, num + 1 ))
    
print(summation(2))
print(summation(8))
print(summation(4))