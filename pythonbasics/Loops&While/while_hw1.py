number = int(input("Введіть число"))

result = 0
while (result<=number):
    if result%2==0 :
        newresult = result**2
        print(newresult)
        result = result + 1
    else:
        print(result)
        result = result + 1