# Twice as old

def twice_as_old(dad_years_old, son_years_old):
    """ we use abs to convert negative to positive number if exist """
    return abs(dad_years_old - (son_years_old * 2))

print(twice_as_old(55,30))
print(twice_as_old(42,21))
print(twice_as_old(22,1))
        

#test.assert_equals(twice_as_old(55,30) , 5)
#test.assert_equals(twice_as_old(42,21) , 0)
#test.assert_equals(twice_as_old(22,1) , 20)
#test.assert_equals(twice_as_old(29,0) , 29)
