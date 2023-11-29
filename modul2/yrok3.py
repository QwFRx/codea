'''
a = open("text.txt", 'a+')
a.write('\n21341')
a.close()
a = open("text.txt", 'r')
print(a.read())
a.close()


import os
os.rename('../teeyrok3mod2', 'ddd')

'''

file = open('dela.txt', 'w')
kolichestvo = int(input('Введите количество дел: '))
for i in range(kolichestvo):
    delo = input(f"Введите {i+1} дело: ")
    file.write(f'\n {i+1} delo: {delo}')
file.close()
