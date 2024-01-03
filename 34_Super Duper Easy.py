# Super Duper Easy

def problem(a):
    if type(a) is str :
        return 'Error'
    else:
        return ((a*50) + 6)

print(problem(5))
print(problem(10))
print(problem('A'))
print(problem('a'))