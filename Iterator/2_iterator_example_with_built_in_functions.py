numbers = [1, 2, 3]

numbers_iterator = iter(numbers)
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))

# Przebieg algorytmu
#
# 1. Do zmiennej o nazwie numbers przypisz listę cyfr 1, 2, 3 - numbers = [1, 2, 3]
# 2. Z listy numbers pobierz iterator i przypisz go do zmiennej o nazwie numbers_iterator
# 3. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (1) z listy i wypisz ten element na ekranie
# 4. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (2) z listy i wypisz ten element na ekranie
# 5. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (3) z listy i wypisz ten element na ekranie
#
# Dodatkowe wyjaśnienie
#
# Powyzszy kod wykorzystuje wbudowane funkcje Pythona zarówno do pobrania obiektu iteratora listy (iter()),
# jak i do samej iteracji (next()). Funkcje te wywołują odpowiednio funkcje __iter__() na liście, oraz funkcję
# __next__() na iteratorze.
#
# powyzszy przykład jest więc równowazny z przykladem z pliku iterator_basic_example.py