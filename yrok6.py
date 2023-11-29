word = input("Введите слово на немецком: ").capitalize()

deutch = {'Ich': "Я", "Du": "Ты", "Er": "Он", "Schmetterling": "Бабочка"}

def translate(word):
    return deutch.get(word)

print(translate(word))

