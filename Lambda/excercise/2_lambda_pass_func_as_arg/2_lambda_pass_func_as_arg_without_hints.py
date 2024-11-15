# ZADANIE
#
# Dane są funkcje:
# write_to_file - funkcja zapisuje dane user_data w pliku z katalogu Assets z biezącego folderu
# save - funkcja przyjmuje dane uzytkownika (user_data) i funkcję kodującą te dane (encoding_function), a
#        jej zadaniem jest przekazanie do funkcji write_to_file zakodowanych danych do zapisania
#
# Dodatkowo podany jest słownik person, zawierający dane uzytkownika
#
# Przekonwertuj obiekt słownika (np. taki jak person) do ciągu znaków
# (podpowiedź - spróbuj sam poszukać informacji nt. konwersji słowników do ciągów znaków za pomocą
# modułu json. Do zdobywania wiedzy spróbuj wykorzystać rózne narzędzia - wyszukiwarkę Google albo ChatGPT)
#
# Następnie napisz wyrazenie lambda, które przekonwertuje znaki przekonwertowanego do ciągu znaków słownika do
# kodów liczbowych tych znaków. Jeśli nie pamiętasz jak przejść listę bez uzywania pętli for, sięgnij do rozdziału List Comprehension
#
# Przekaz do funkcji save przekonwertowany na ciąg znaków obiekt zawierający dane uzytkownika oraz funkcję kodującą znaki
#
# Zapisz do pliku zakodowany funkcją kodującą ciąg znaków repreentujący dane uzytkownika.
#
# W pliku wynikowym z folderu Assets/database.txt powinien znajdować się tekst wyglądający jak ten fragment:
# 123 34 110 97 109 101 34 58 32 34 80 97 119 101 108 34 ...

import os

def write_to_file(user_data):
    with open(os.path.realpath('Lambda/excercise/2_lambda_pass_func_as_arg/Assets/database.txt'), 'w') as db_file:
        db_file.write(user_data)


def save(user_data, encoding_function):
    write_to_file()


person = {
    'name': 'Pawel',
    'age': 40,
    'sex': 'm',
    'occupation': 'postman',
    'company': 'Main post'
}