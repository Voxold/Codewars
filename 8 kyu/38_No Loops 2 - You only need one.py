# No Loops 2 - You only need one

def check(a, x): 
    return True if x in a else False

print(check([66, 101], 66))
print(check([80, 117, 115, 104, 45, 85, 112, 115], 45))
print(check(['t', 'e', 's', 't'], 'e'))

# test.assert_equals(check([66, 101], 66), True)
# test.assert_equals(check([80, 117, 115, 104, 45, 85, 112, 115], 45), True)
# test.assert_equals(check(['t', 'e', 's', 't'], 'e'), True)