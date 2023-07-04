user = {
    "name": "Alina",
    "age": 100500,
    "profession": "dentist",
    "country":"Ukraine"
}

key_list = user.keys()
print(key_list)
print("age" in key_list)

del user["age"]
print(key_list)
print("age" in key_list)