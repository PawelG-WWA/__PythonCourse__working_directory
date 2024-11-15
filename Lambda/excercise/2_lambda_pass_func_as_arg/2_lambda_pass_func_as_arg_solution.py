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
import json

def write_to_file(user_data):
    with open(os.path.realpath('Lambda/excercise/2_lambda_pass_func_as_arg/Assets/database.txt'), 'w') as db_file:
        db_file.write(user_data)


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

encoding_function = lambda data: ''.join([str(ord(c)) + ' ' for c in data])

save(user_data, encoding_function)

# WYJAŚNIENIE
#
# Do przekonwertowania słownika na ciąg znaków w formacie json uzyliśmy funkcji dumps z modulu json.
#
# Funkcja dumps konwertuje słownik do ciągu znaków. Funkcja dump zapisuje dane w formacie json do pliku.
#
# Następnie tworzymy funkcję encoding_function wykorzystując wyrazenie lambda
#
# Wyrazenie to przyjmuje jako parametr zmienną data. Ciało wyrazenia lambda jest następujące:
# -Wykorzystując wyrazenie list składanych, dla kazdego znaku w ciągu zapisanym pod zmienną data
#  wywoływana jest funkcja ord konwertująca znak do wartości liczbowej.
# -Kazda wartość liczbowa jest zamieniana na następnie na typ string za pomocą wbudowanej funkcji str. Powodem
#  jest konieczność dodania białego znaku - operator '+' nie zadziałałby dla liczby oraz jednoelementowego ciągu znaków,
#  jakim jest ' '.
# -na samym końcu wywoływana jest funkcja join. Do pustego ciągu znaków '' dodawane są kolejne elementy listy
#  stworzonej za pomocą wyrazenia list składanych. Elementy tej listy to - jak juz wiesz - kody liczbowe znaków
#  uzyskane dzięki wywołaniu ord(c)
#
# Następnie funkcja ta zapisywana jest pod zmienną encoding_function
#
# Wywołujemy 'save', przekazując uzyskany wcześniej dzięki wywołaniu json.dumps ciąg znaków reprezentujący dane uzytkownika
# w formacie json, a takze napisaną wcześniej za pomocą wyrazenia lambda funkcję kodującą
#
# W funkcji save wywołujemy write_to_file przekazując wynik działania wywołania funkcji encoding_function na obiekcie
# user_data. Oznacza to, ze funkcję napisaną za pomocą wyrazenia lambda wywołujemy dopiero w tym momencie na przekazanym obiekcie.
#
# To właśnie teraz zostanie uruchomiony algorytm wykorzystujący wyrazenie list składanych, który dla kazdego elementu kolekcji
# (ciągu znaków) przekonwertuje kazdy znak na wartośc liczbową i doda do niego biały znak (spację).
#
# Na samym końcu przekonwertowane znaki zostaną zapisane w pliku database.txt