number = int(input("Введіть число"))

startNumber = 2
for i in range(2, number+1, 2):
      result = startNumber**2
      print(result)
      startNumber = startNumber + 2