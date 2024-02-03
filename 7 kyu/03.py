# Your task is to write a function which returns the sum of a sequence of integers.

def sequence_sum(begin_number, end_number, step):

    if begin_number > end_number :
        return 0
    return sum(range(begin_number,end_number + 1,step))

print(sequence_sum(2,2,2))
print(sequence_sum(2,6,2))
print(sequence_sum(1,5,1))
print(sequence_sum(8,5,1))
