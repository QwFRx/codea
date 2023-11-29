slovar = {"id": 228, 'message': "privet!!"}

import json
filename = "YROK4_smotri.json"

maria = {
    'fio': 'zybenko michail petrovic',
    'ocenki': {
        'matematika': 5,
        'biologia': 5
    },
    'hobby': ['havat', 'est', 'kyshat'],
    'vozrast': 14,
    'friend': {
        'name': 'Alisa',
        'years': 15,
        'hobby': None
    }
}

with open(filename, 'w', encoding= 'utf-8') as file:
    file.write(json.dumps(maria, ensure_ascii = False, indent= 4))

info_2 = []
with open(filename, encoding="utf-8") as file:
   info_2 = json.loads(file.read())
print(info_2)


