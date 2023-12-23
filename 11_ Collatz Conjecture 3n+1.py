# The Collatz conjecture (also known as 3n+1 conjecture) is a conjecture that 
# applying the following algorithm to any number we will always eventually reach one

def hotpo(n):
    i = 0
    if n <= 0 :
        return False
    else :
        while n != 1:
            if n % 2 == 0:
                n = n/2
                i += 1
            else:
                n = (n*3) + 1
                i += 1
    return i

print(hotpo(1))
print(hotpo(5))
print(hotpo(6))
print(hotpo(0))