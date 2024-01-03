# Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
    positif = []
    negatif = []
    if len(arr) == 0 :
        return []
    for number in arr :
        if number > 0 :
            positif.append(number)
        elif number < 0 :
            negatif.append(number) 
    return [len(positif),sum(negatif)]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 0]))
print(count_positives_sum_negatives([]))