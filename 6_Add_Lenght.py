# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

def add_length(str_):
    result = []
    my_list = str_.split()
    for word in my_list:
        result.append(word + ' ' + str(len(word)) )
    return result

print(add_length("Python is the most popular language"))
