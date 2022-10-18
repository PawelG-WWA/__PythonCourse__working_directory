# PRZYKŁAD 1 - funkcja bez argumentów

def basic_function_example():
    print('called basic_function_example()')

basic_function_example()

# PRZYKŁAD 1 - Przebieg algorytmu:
#
# 1. Wywołaj funckję basic_function_example()
#     1a. Wypisz na ekranie napis 'called basic_function_example' 


# PZYKŁAD 2 - funkcja z jednym argumentem
def function_with_argument(name):
    print('Witaj ' + name)

function_with_argument('Pawel')

# PRZYKŁAD 2 - Przebieg algorytmu
#
# 1. Wywołaj funkcję function_with_argument
#     1a. przypisz zmiennej o nazwie name wartość 'Pawel', przekazaną jako argument
#         wywołania funkcji function_with_argument
#     1b. Wypisz na ekranie napis 'Witaj Pawel'


# PRZYKŁAD 3 - funkcja z wieloma argumentami

def function_with_many_arguments(name, age, occupation):
    print('%s, wiek: %s, zawód: %s' % (name, age, occupation))

function_with_many_arguments('Pawel', 32, 'programista')

# PRZYKŁAD 3 - Przebieg algorytmu
#
# 1. Wywołaj funkcję function_with_many_arguments
#     1a. przypisz zmiennym o nazwach name, age, occupation wartości przekazane do funkcji
#         function_with_many_arguments w kolejności przekazania - name = 'Pawel', age = 32, occupation = 'programista'
#     1b. Wyświetl na ekranie napis: 'Pawel, wiek: 32, zawód: programista'


# PRZYKŁAD 4 - funkcja zwraca wartość dzięki uyciu return

def function_wich_returns_value(name, age):
    return '%s, wiek: %s' % (name, age)

user_info = function_wich_returns_value('Pawel', 32)

print(user_info)

# PRZYKŁAD 4 - Przebieh algorytmu
#
# 1. Wywołaj funkcję function_wich_returns_value
#     1a. przypisz zmiennym o nazwach name, age wartości przekazane do funkcji
#         function_wich_returns_value w kolejności przekazania - name = 'Pawel', age = 32
#     1b. Stwórz obiekt będący łańcuchem znaków, sformatowanym wg podanego schematu.
#         Stworzony obiekt - 'Pawel, wiek: 32'
#     1c. Zwróc stworzony obiekt do miejsca wywołania funkcji
# 2. Wykonaj przypisanie zwróconego łańcucha znaków do zmiennej o nazwie user_info
# 3. Wypisz wartość przechowywaną pod zmienną o nazwie user_info


# PRZYKŁAD 5 - funkcje bez return zwracają obiekt None typu NoneType

def function_without_return_returns_none():
    print('called function without return')

result = function_without_return_returns_none()
print(result)
print(type(result))

# PRZYKŁAD 5 - przebieg algorytmu
#
# 1. Wywołaj funkcję function_without_returns_none()
#     1a. Wypisz na ekranie napis 'called function without return'
# 2. Wykonaj przypisanie wyniku wywołania funkcji do zmiennej o nazwie result
# 3. Wypisz na ekranie wartość przechowywaną pod result - wynik: None
# 4. Wypisz na ekranie wartość zawróconą przez wywołanie wbudowanej funkcji type z przekazanym parametrem result - wynik <class 'NoneType'>


# PRZYKŁAD 6 - def jest instrukcją tworzącą obiekt function

def example_function():
    print('example_function')

print(example_function)
print(type(example_function))
print(id(example_function))

# PRZYKŁAD 6 - Przebieg algorytmu
#
# 1. Wywołaj funkcję example_function
#     1a. Wypisz na ekranie napis example_function
# 2. Wypisz na ekranie napis '<function example_function at 0x7fee500a6280>' - adres - tj część 0x0x7fee500a6280 moze być u Ciebie inna
# 3. Wypisz na ekranie typ obiektu example_function - wynik: <class 'function'>
# 4. Wypisz na ekranie adres pod którym przechowywany jest obiekt example_function - 140661521801856 - u Ciebie adres moze być inny,
#    ale w wersji dziesiętnej będzie się równał liczbie wyrazonej szsnastkowo w punkcie 2
#
# Dodatkowe wyjaśnienie:
#
# def jest instrukcją, która po napotkaniu przez interpreter Pythona tworzy obiekt funkcji
# i przypisuje go do nazwy example_function. Dzięki temu mozesz wywołać funkcję uzywając
# nazwy, do której obiekt został przypisany. Jak widzisz, obiekt jest typu function i jest przechowywany
# w pamięci komputera pod jakimś adresem


# Przykład 7 - funkcja przed uzyciem musi zostać zdefiniowana

function_defined_later() # spowoduje błąd

def function_defined_later():
    print('called function_dafined_later')

# PRZYKŁAD 7 - Przebieg algorytmu
#
# 1. Wywołaj funkcję function_defined_later
# 2. Wypisz na ekranie informację o błędzie mówiącym, ze funkcja function_defined_later nie została zdefiniowana
#
# Dodatkowe wyjaśnienie:
#
# Python jest językiem interpretowanym, a nie kompilowanym co oznacza, ze kod wykonuje się instrukcja po instrukcji
#
# Interpreter napotyka więc linię wywołującą funkcję o nazwie function_defined_later() i widzi, ze funkcja ta nie
# została jeszcze zdefiniowana przez programistę - nie istnieje obiekt zapisany w pamięci komputera, do którego
# mozna odnieść się po nazwie function_defined_later
#
# Jeśli przeniesiesz wywołanie funkcji ponizej jej definicji, wszystko zadziała, tak jak w poprzednich przykładach,
# poniewaz, interpreter najpierw napotka definicję funkcji, stworzy jej obiekt i referencję do niego o nazwie
# function_defined_later i poprzez uzycie tej nazwy będziesz mógł, jak w poprzednich przykładach, wywołać funkcję

