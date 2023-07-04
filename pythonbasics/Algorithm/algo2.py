count = float(input("Введіть бажану кількість електроенернії: "))
tariff = 7.80
price = tariff * count
print("Ціна заряджання =",round(price, 2))

cash = float(input("Введіть суму готівки: "))
rest = cash - price

print("Решта =",round(rest,2))