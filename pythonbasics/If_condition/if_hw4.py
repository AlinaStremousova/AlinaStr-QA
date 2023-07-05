waterTemperature = int(input("Введіть температуру води:"))
if waterTemperature <= 0:
    text = "Лід"
if waterTemperature >0 and waterTemperature <100:
    text = "Вода"
if waterTemperature >=100:
    text = "Пара"
print(text)