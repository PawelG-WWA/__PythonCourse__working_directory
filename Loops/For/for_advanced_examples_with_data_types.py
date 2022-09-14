#import modułu decimal w celu poprawnego wykonywania działan na liczbach dziesiętnych

from decimal import Decimal
import decimal
import math

decimal.getcontext().prec = 3 # ustawienie precyzji liczb dziesiętnych

# EXAMPLE 1 - Przetwarzanie słowników
print('#EXAMPLE 1')
prices = { 'potato': Decimal(1.2), 'tomato': Decimal(2.4), 'banana': Decimal(3.6), 'mug': Decimal(10) }

for price in prices:
    print(price) # pętla for iteruje po kluczach słownika

for price in prices:
    prices[price] = prices[price] * Decimal(1.1) # podwyzka ceny o 10%

print(prices)

# EXAMPLE 1 - wyjaśnienie
#
# Podczas przetwarzania pętlą for słowników, pętla domyślnie iteruje po kluczach słownika, a nie po całych elementach par klucz-wartość.
# Dlatego, aby pobrać lub zmodyfikować wartość przechowywaną pod kluczem, nalezy donieść się do tej wartości poprzez klucz jak w drugiej pętli:
# for price in prices:
#     prices[price] = prices[price] * Decimal(1.1)
#
# Zapis
# for price in prices:
#
# jest więc równowazny z zapisem
#
# for price in prices.keys():

print('\n')
# EXAMPLE 2 - krotki
print('#EXAMPLE 2')
some_complex_object = (1, 'title', Decimal(10.78))

for element in some_complex_object:
    print(element)

# EXAMPLE 2 - wyjaśnienie
#
# Przetwarzanie krotek w pętli w taki sposób nie róni się niczym od przetywrzania listy i jej elementów
# elementy są pobierane w kolejność od lewej do prawej i - w powyzszym przypadku - wypisywane na ekran

print('\n')

# EXAMPLE 3 - krotki, przyklad zaawansowany
print('#EXAMPLE 3')
list_of_pairs_of_numbers = [(1, 1), (2, 4), (3, 8)]

for pair in list_of_pairs_of_numbers:
    print(pair)

for (a, b) in list_of_pairs_of_numbers:
    print('a = %s, b = %s' % (a, b))
    print('%s pierwiastkiem kwadratowym %s? %s \n' % (a, b, math.sqrt(b) == a))

# EXAMPLE 3 - wyjaśnienie
#
# Na początku tworzymy listę krotek
#
# Przetwarzanie w pętli for listy krotek, to przetwarzanie elementów listy z których kady pojedynczy jest krotką.
# Oznacza to, ze w pierwszej pętli for kazdy pojedynczy element przypisany do nazwy pair, będzie kolejną parą liczb:
# (1, 1) - przy pierwszej iteracji
# (2, 4) - przy drugiej iteracji
# (3, 8) - przy trzeciej, ostatniej iteracji
#
# Alternatywnie, mozemy pracowac z pojedynczymi elementami kazdej krotki z listy krotek. Zapis:
#
# for (a, b) in list_of_pairs_of_numbers:
#
# nie tylko pobiera element krotki z listy krotek, ale przypisuje wartości krotek od lewej do prawej do nazw a oraz b.
# Przy pierwszym przejściu pętli pętla for pobiera pierwszy element (1, 1) i przypisuje wartość 1 do a i wartość 1 do b,
# z którymi mozemy niezaleznie pracować w ramach insrukcji w zakresie pętli.
# 
# Przy kolejnej iteracji pętli pobierany jest następny element z kolekcji krotek - (2, 4) oraz przypisywane są wartości 2 do a i 4 do b itd.
#
# Druga pętla sprawdza wypisuje poszczególne pary liczb i sprawdza, czy a jest pierwiaskiem kwadratowym b w kazdej z par.