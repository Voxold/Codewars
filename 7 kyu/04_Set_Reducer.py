# Set Reducer

def set_reducer(inp):
    while len(inp) > 1:
        list = []
        i = 0
        while i < len(inp):
            count = 1
            while i + count < len(inp) and inp [i + count] == inp[i]:
                count+=1
            if count > 1:
                list.append(count)
            else:
                list.append(1)
            i+=count
        inp = list
    return inp[0]

print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))
print(set_reducer([8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]))