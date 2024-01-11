# Return their respective ages now as [humanYears,catYears,dogYears]

def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    for year in range(1,(human_years+1)):
        if year == 1 :
            catYears += 15
            dogYears += 15
        elif year == 2:
            catYears += 9
            dogYears += 9
        else:
            catYears += 4
            dogYears += 5

    return [human_years,catYears,dogYears]

print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))
print(human_years_cat_years_dog_years(3))

