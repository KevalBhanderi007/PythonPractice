
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)


phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)


dict = {
    "i love you": "tane prem karu chhu",
    "banana" : "kelu",
    "grapes": "draksh"
}

print(dict)

for name , names in dict.items():
    print(f"angreji me kahete ke {name} gujarati ma bolu {names}")

del dict ["banana"]
dict.pop("grapes")
dict["mobile"] = "machine"

print(dict)

if "mobile" in dict:  
    print("mobile is listed in the dict.")
    