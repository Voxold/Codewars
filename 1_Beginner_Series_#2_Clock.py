#Clock shows h hours, m minutes and s seconds after midnight.
#Your task is to write a function which returns the time since midnight in milliseconds.

def past(h, m, s): 
    return 1000 * ((3600*h) + (60*m) + (s))

# we use *100 to convert seconds to milliseconds

print(past(0, 1, 1))