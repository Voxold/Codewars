# Training JS #7: if..else and ternary operator

# Method 1 :
def sale_hotdogs(n):
    if n <5 :
        return n * 100
    elif n >= 5 and n < 10 :
        return n * 95
    else:
        return n * 90

print(sale_hotdogs(2))
print(sale_hotdogs(7))
print(sale_hotdogs(11))

print("=" * 10)
# Method 2 :
def sale_hotdogs(n):
    return n*100 if n<5 else n*95 if n >= 5 and n < 10 else n*90 

print(sale_hotdogs(2))
print(sale_hotdogs(7))
print(sale_hotdogs(11))