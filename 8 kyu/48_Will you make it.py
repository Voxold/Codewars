# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    result = mpg * fuel_left
    if result >= distance_to_pump:
        return True
    else:
        return False
    
print(zero_fuel(50, 25, 2)) # True
print(zero_fuel(100, 50, 1)) # False