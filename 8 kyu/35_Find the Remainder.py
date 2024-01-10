# Find the Remainder

def remainder(a,b):
    try:
        return max(a,b) % min(a,b)
    except:
        return None

print(remainder(17,5)) 
print(remainder(1,0)) 
print(remainder(-1,0)) 