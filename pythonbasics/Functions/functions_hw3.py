number = int(input("Введіть число"))

def print_numbers(number):
    digit = 0
    while (digit<=number):
        print(digit)
        digit = digit + 2

print_numbers(number)