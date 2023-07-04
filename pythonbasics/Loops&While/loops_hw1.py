number = int(input("Введіть шуканий член арифметичної прогресії "))

n = 5
for i in range(1, number):
    number = number + 1
    n = n + 3
print(n)