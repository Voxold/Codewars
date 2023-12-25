# Create a function that takes 2 integers in form of a string as an input,

def sum_str(a, b):
    a = 0 if a == '' else int(a)
    b = 0 if b == '' else int(b)
    return str(a + b)

print(sum_str('5','2'))
print(sum_str('10',''))
print(sum_str('6','8'))