# input is an unsorted list of 3 positive integers
# return True if it is possible to form a Pythagorean triple with the 3 integers
# return False if it is not possible

# Method 1 :
def pythagorean_triple(integers):
    sorted_list = sorted(integers)
    A = sorted_list[0]
    B = sorted_list[1]
    C = sorted_list[2]
    if pow(A,2) + pow(B,2) == pow(C,2):
        return True
    else:
        return False

print(pythagorean_triple([5, 3, 4]))
print(pythagorean_triple([3, 4, 5])) 
print(pythagorean_triple([13, 12, 5]))
print(pythagorean_triple([100, 3, 999]))

# Method 2 :
def pythagorean_triple(integers):
    return pow(sorted(integers)[0],2) + pow(sorted(integers)[1],2) == pow(sorted(integers)[2],2)

print(pythagorean_triple([5, 3, 4]))
print(pythagorean_triple([3, 4, 5])) 
print(pythagorean_triple([13, 12, 5]))
print(pythagorean_triple([100, 3, 999]))
