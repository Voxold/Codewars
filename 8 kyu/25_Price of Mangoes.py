# Price of Mangoes

def mango(quantity, price):
    list = []
    for i in range(1, quantity + 1):
        if i % 3 != 0:
            list.append(i)
    return len(list) * price

print(mango(2, 3)) 
print(mango(3, 3)) 
print(mango(5, 3))
print(mango(9, 5))