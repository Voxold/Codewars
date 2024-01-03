# return to which quarter of the year it belongs as an integer number.

def quarter_of(month):
    from math import ceil
    return ceil(month / 3)

print(quarter_of(1))
print(quarter_of(2))
print(quarter_of(3))
print(quarter_of(4))
print(quarter_of(5))
print(quarter_of(6))
print(quarter_of(7))
print(quarter_of(8))
print(quarter_of(9))
print(quarter_of(10))
print(quarter_of(11))
print(quarter_of(12))