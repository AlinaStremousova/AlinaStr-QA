number = int(input("Введіть число"))

startDigit = 1
sum = 0
while (startDigit<=number):
    sum = sum + startDigit
    startDigit = startDigit + 1
print (sum)