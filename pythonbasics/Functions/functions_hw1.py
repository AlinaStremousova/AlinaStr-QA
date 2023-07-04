miles = float(input("Введіть кількість миль"))

def convert_miles_to_km(miles):
    miles = miles*1.6
    round(miles,2)
    return miles
    
print(convert_miles_to_km(miles))