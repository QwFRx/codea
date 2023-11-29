import csv
filename = 'yrok4_1 smotri.csv'
shoplist = {'kart': [2, 100], 'yab': [3,250]}

with open(filename, 'w', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "weight"], quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for name, values in sorted(shoplist.items()):
        writer.writerow(dict(name=name, weight=values[0]))
rows = []

with open(filename, 'r' ,encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
for row in rows:
    print(row)