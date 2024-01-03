# Return the average of the given array rounded down to its nearest integer.

def get_average(marks):
    return int(sum(marks) / len(marks))

print(get_average([1,2,3,4,5]))