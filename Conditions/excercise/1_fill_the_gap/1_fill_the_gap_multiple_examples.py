# EXAMPLE 1

x = 3

if _gap_1:
    print('reszta x nie jest równa zero')


# EXAMPLE 2

x = 'Napis'

if _gap_2:
    print('Słowo "api" znajduje się w słowie Napis')


# EXAMPLE 3

x = "Dłuzszy ciąg znaków"

if _gap_3:
    print('Słowo "api" NIE znajduje się w łańcuchu znaków przechowywanym pod nazwą x')


# EXAMPLE 4

x = input("Wpisz jakieś słowo: ")

if _gap_4_1:
    print("Liczba znaków wpisanego słowa jest podzielna przez 2")
_gap_4_2
    print("Liczba znaków wpisanego słowa NIE jest podzielna przez 2") # ten napis powinien się wyświetlić tylko wtedy, gdy warunek _gap_4_1 NIE jest spełniony


# EXAMPLE 5

car_features = ['OLED display', 'LED lights', 'Winter seats', 'Premium speakers']
selected_feature_number = input('Podaj numer zetawu:\n1: OLED display\n2: LED lights\n3: Winter seats\n4: Premium speakers\n')
user_selected_features = []
selected_feature = None

# jeśli podany przez uzytkownika numer zestawu faktycznie jest liczbą (selected_feature_number.isnumeric())
# i jest numerem w zakresie liczby elementów listy (_gap_5_1)
# wejdź do bloku kodu pod if
if selected_feature_number.isnumeric() _gap_5_1:
    selected_feature = car_features[int(selected_feature_number)-1]

    user_selected_features.append(selected_feature)

    if _gap_5_2:
        # jeśli uzytkownik dodał zestaw "Winter seats" LUB "OLED display", obowiązkowo dodaj tez zestaw "LED lights"
        user_selected_features.append('LED lights')
_gap_5_3
    # Wypisz wtedy i tylko wtedy, gdy wpisany numer zestawu nie jest liczbą i gdy jest liczbą spoza zakresu liczby elementów listy zestawów
    print('Nieznany numer zestawu')

print(user_selected_features)
