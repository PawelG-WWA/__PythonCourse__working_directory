# ZADANIE
#
# Zadanie to jest niewielką modyfikacją poprzedniego.
#
# Polega na napisaniu listy trzech wyrazeń lambda, z których:
# -pierwsze - jak w poprzednim zadaniu - zamieni wszystkie znaki w ciągu na odpowiadające im liczby całkowite
# -drugie zamieni wszystkie znaki w ciągu na liczby w systemie binarnym
# -trzecie zamieni wszystkie znaki w ciągu na liczby w systemie szesnastkowym
#
# Następnie dla kazdego wywołaj funkcję save dla kazdego z tych wyrazeń i sprawdź wynik w pliku
# Assets/database_multiple_encodings.txt

import os
import json

def write_to_file(user_data):
    with open(os.path.realpath('Lambda/excercise/3_lambda_mutiple_functions/Assets/database_multiple_encodings.txt'), 'a') as db_file:
        db_file.write(user_data + '\n')


def save(user_data, encoding_function):
    write_to_file(encoding_function(user_data))


person = {
    'name': 'Pawel',
    'age': 40,
    'sex': 'm',
    'occupation': 'postman',
    'company': 'Main post'
}

user_data = json.dumps(person)

encodings = [
    lambda data: ''.join([str(ord(c)) + ' ' for c in data]),
    lambda data: ''.join([str(bin(ord(c))) + ' ' for c in data]),
    lambda data: ''.join([str(hex(ord(c))) + ' ' for c in data])
]

for encoding in encodings:
    save(user_data, encoding)


# WNIOSKI
#
# Powyzsze zadanie realizuje to samo, co zadanie drugie z tego folderu zadań.
#
# Wniosek jaki płynie jednak z tego zadania jest następujący:
# wyrazenia lambda doskonale nadają się do zapisywania i uzywania prostych, niezaśmiecających kodu funkcji,
# których uzywamy w niewielu miejscach. Choć mozemy zapisać kazdą z tych funkcji za pomocą def, a następnie
# przekazując nazwy tak zdefiniowanych funkcji do listy, kod moze niepotrzebnie się wydłuzyc
#
# To, jakiego rodzaju podejscie zastosujesz, zalezy od preferencji Twoich i Twojego zespolu.
#
# Funkcje lambda i takie ich uzycie w zaden sposób nie jest konieczne ani wymagane