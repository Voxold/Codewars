# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# Method (1)
def litres(time):
    return int(time / 2)

print(litres(3))
print(litres(6.7))
print(litres(11.8))

print('-' * 10)

# Method (2)
def litres(time):
    return time // 2

print(litres(3))
print(litres(6.7))
print(litres(11.8))