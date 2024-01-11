# Count the number of cubes with paint on

def count_squares(cuts):
    return (6 * (cuts ** 2)) + 2

print(count_squares(2)) # 26
print(count_squares(4)) # 98
