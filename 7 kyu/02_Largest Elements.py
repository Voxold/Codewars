# Write a program that outputs the top n elements from a list.

def largest(n, xs):
    """Find the n highest elements in a list"""
    if n == 0:
        return []
    else:
        return sorted(xs)[-n:]


print(largest(2, [7,6,5,4,3,2,1])) # => [6,7]
print(largest(4, [7,6,5,4,3,2,1])) # => [4, 5, 6, 7] 
print(largest(0, [7,6,5,4,3,2,1])) # => []

