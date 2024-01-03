#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

# Method 1 :
def repeat_str(repeat, string):
    return repeat * string

print(repeat_str(10,"Bilal"))

print('-' * 50)
# Method 1 :

def repeat_str(repeat, string):
    #return repeat * string

    repeated = ""
    for i in range(repeat) :
        repeated += string
    return repeated

print(repeat_str(10,"Bilal"))