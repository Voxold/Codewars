# Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, 
# your task is to find the sum of the minimum values in each row.

def sum_of_minimums(numbers):
    return min(numbers)
    
print(sum_of_minimums([ 1, 2, 3, 4, 5 ]))       #  minimum value of row is 1
print(sum_of_minimums([ 5, 6, 7, 8, 9 ]))       #  minimum value of row is 5
print(sum_of_minimums([ 20, 21, 34, 56, 100 ])) #  minimum value of row is 20
