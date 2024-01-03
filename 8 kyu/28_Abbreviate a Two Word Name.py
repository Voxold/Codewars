# Write a function to convert a name into initials.

def abbrev_name(name):
    A = []
    B = name.split()
    for i in B :
        A.append(i[0].upper())
    return '.'.join(A) 

print(abbrev_name('Sam Harris'))
print(abbrev_name('patrick feeney'))