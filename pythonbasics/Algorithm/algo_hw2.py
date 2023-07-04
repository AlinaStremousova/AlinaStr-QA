exchangeRate = float(input("Введіть курс євро до гривні: "))
sumUAH = int(input("Введіть суму в гривнях, яку зібрали волонтери: "))
banderaCarCost = 6500 * exchangeRate
banderaCarAmount = sumUAH / banderaCarCost
print(int(banderaCarAmount))
