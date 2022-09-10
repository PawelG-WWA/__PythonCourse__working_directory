# EXAMPLE 1

x = 3

if x % 2: # równowazny zapis: if x % 2 > 0
    print('#EXAMPLE 1: reszta dzielenia x przez 2 nie jest równa zero')

# Wyjaśnienie:
#
# x = 3, zatem reszta z dzielenia x / 2 = 1. Wyrazenie x % 2 zwraca 1, a jeden jest wartością Prawdy (True),
# tote x % 2 zwraca True, a więc zostanie wypisany napis 'reszta x nie jest równa zero'


# EXAMPLE 2

x = 'Napis'

if 'api' in x:
    print('#EXAMPLE 2: Słowo "api" znajduje się w słowie Napis')

# Wyjaśnienie
#
# operator in słuzy do sprawdzania, czy dany element znajduje się w kolekcji. Łańcuch znaków to uporządkowana kolekcja znaków,
# a zatem operator "in" sprawdza, czy ciąg znaków api występuje w ciągu znaków "Napis" - występuje, opeartor "in" zwraca Prawdę (True),
# więc na ekranie wyświetlany jest napis 'Słowo "api" znajduje się w słowie Napis'


#EXAMPLE 3

x = "Dłuzszy ciąg znaków"

if "api" not in x:
    print('#EXAMPLE 3: Słowo "api" NIE znajduje się w łańcuchu znaków przechowywanym pod nazwą x')

# Wyjaśnienie
#
# Operator not słuzy do sprawdzania, czy coś czymś nie jest, a nie czy coś nie jest czemuś równe.
# Łańcuch znaków "api" nie jest podciągiem (ang substring) łańcucha znaków przechowywanego pod nazwą x "Dłuszy ciąg znaków"


# EXAMPLE 4
x = input("Wpisz jakieś słowo: ")

if not len(x) % 2: # równowazny zapis: if len(x) % 2 > 0
    print("#EXAMPLE 4: Liczba znaków wpisanego słowa jest podzielna przez 2")
else:
    print("#EXAMPLE 4: Liczba znaków wpisanego słowa NIE jest podzielna przez 2") 


# EXAMPLE 5
car_features = ['OLED display', 'LED lights', 'Winter seats', 'Premium speakers']
selected_feature_number = input('Podaj numer zetawu:\n1: OLED display\n2: LED lights\n3: Winter seats\n4: Premium speakers\n')
user_selected_features = []
selected_feature = None

if selected_feature_number.isnumeric() and int(selected_feature_number) > 0 and int(selected_feature_number) <= len(car_features):
    selected_feature = car_features[int(selected_feature_number)-1]

    # jeśli podana przez uytkownika nazwa zestawu znajduje sie na liscie car_features
    user_selected_features.append(selected_feature)

    if selected_feature is 'Winter seats' or selected_feature is 'OLED display':
        # jeśli uzytkownik dodał zestaw "Winter seats" lub "OLED display", obowiązkowo dodaj tez zestaw "LED lights"
        user_selected_features.append('LED lights')
else:
    print('Nieznany numer zestawu')

print(user_selected_features)

# Wyjaśnienie
#
# Prosimy uzytkownika o podanie numeru zestawu. Jeśli podana przez uzytkownika wartość nie jest liczbą, czyli jest np.
# ciągiem znaków "kot", wypisujemy napis 'Nieznany numer zestawu'. Równie, jeśli wpisany przez uytkownika numer zestawu
# jest spoza zakresu listy, wypisujemy napis 'Nieznany numer zestawu.
#
# Lista indeksuje elementy od 0 w górę. Mamy więc 4 elementy w liście pod indeksami kolejno 0, 1, 2 i 3.
# 0 - OLED display
# 1 - LED lights
# 2 - Winter seats
# 3 - Premium speakers
#
# z pespektywy uzytkownika naturalnym jest liczenie od 1, dlatego prosimy o podanie cyfry od 1 do 4 i sprawdzamy w pierwszy warunku, czy
# uzytkownik rzeczywiście wpisał cyfrę większą od zera i menijszą lub równą 4
#
# następnie przypisujemy do zmiennej selected_feature wybrany zestaw przez uzytkownika, poprzez pobranie elementu z listy car_features
# na pozycji o indeksie równym wpisaną cyfrę - 1. Jeśli uzytkownik wpisał 1, to chcemy pobrać element pierwszy z listy, który znajduje się
# na indeksie 0. Jeśli wpisał cyfrę 4, to chcemy pobrać element ostatni z listy, a więc w pamięcy przechowywany pod indeksem 3.
# 
# Wstawiamy wybrany element na listę wybranych przez uzytkownika zestawów
# 
# Następnie sprawdzamy, czy wybrany element jest tosamy z "Winter seats" LUB "OLED display" i jeśli tak,
# to obowiązkowo dodajemy do samochodu uytkownika światła LED ('LED lights')
#
# Na końcu wypisujemy wszystkie zestawy, jakie uytkownik dodał do swojego samochodu