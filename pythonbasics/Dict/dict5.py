user = {
    "name": "Alina",
    "age": 100500,
    "profession": "dentist",
    "country":"Ukraine"
}

if "name" in user:
    print(user["name"])
else:
    print("Ключа name немає в словнику")

if "country" in user:
    print(user["country"])
else:
    print("Ключа country немає в словнику")