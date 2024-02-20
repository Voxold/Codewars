# Rick wants a faster way to get the product of the largest pair in an array.

# Slow Method
def max_product(a):
	list = sorted(a)
	return list[-1] * list[-2]

print(max_product([2, 1, 5, 0, 4, 3]))
print(max_product([7, 8, 9]))           
print(max_product([33, 231, 454, 11, 9, 99, 57]))

# Fast Method
def max_product(a):
	max1 = max(a)
	a.remove(max1)
	max2 = max(a)
	a.remove(max2)
	return max1 * max2

print(max_product([2, 1, 5, 0, 4, 3]))
print(max_product([7, 8, 9]))           
print(max_product([33, 231, 454, 11, 9, 99, 57]))