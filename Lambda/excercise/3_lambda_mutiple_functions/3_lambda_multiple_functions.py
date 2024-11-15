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

# Tu zapisz listę wyrazeń lambda z treści zadania

# Wywołaj save dla kazdej funkcji zwróconej przez wyrazenie lambda