number = int(input("Введіть число"))

def is_even_or_odd(number):
    if number%2==0:
        number = f"число {number} парне"
    else:
        number = f"число {number} непарне"
    return(number)

print(is_even_or_odd(number))