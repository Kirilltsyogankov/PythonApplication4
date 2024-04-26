import json

json_data = '{"nimi":"Kirill Tsogankov","vanus":17,"prillid":false}'
data = json.loads(json_data)

print(data)
print(data["nimi"])

for key, value in data.items():
    print(key, ":", value)

data2 = {
    "nimi": "Anna",
    "vanus": 55,
    "abielus": True,
    "Lapsed": ("Inna", "Mati"),
    "koduloomad": None,
    "autod": [
        {"muudel": "BMW", "värv": "punane", "joud": 500, "number": "123ABC"},
        {"muudel": "Ford", "värv": "must", "joud": 300, "number": "321CBA"}
    ]
}

print(json.dumps(data2))
print(json.dumps(data2, indent=2, separators=(".", "="), sort_keys=True))

with open("data_file.json", "w") as w_file:
    json.dump(data2, w_file)

print("Andmed failist:")

with open("data_file.json", "r") as r_file:
    data2 = json.load(r_file)

print(data2)
