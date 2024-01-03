# Calculate BMI


def bmi(weight, height):
    
    bmi = weight / pow(height,2)

    if bmi <= 18.5 :
        return "Underweight"
    elif bmi <= 25.0 :
        return "Normal"
    elif bmi <= 30.0 :
        return "Overweight"
    else :
        return "Obese"
    
print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(110, 1.80))
print(bmi(50, 1.50))