number = int(input("Введіть число:"))
rest = number % 2
if rest == 0:
    text = "Введене число - парне"
if rest != 0:
    text = "Введене число - непарне"
print(text)