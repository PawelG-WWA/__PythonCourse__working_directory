numbers = [1, 2, 3]

numbers_iterator = numbers.__iter__()
print(numbers_iterator.__next__())
print(numbers_iterator.__next__())
print(numbers_iterator.__next__())

# Przebieg algorytmu
#
# 1. Do zmiennej o nazwie numbers przypisz listę cyfr 1, 2, 3 - numbers = [1, 2, 3]
# 2. Z listy numbers pobierz iterator i przypisz go do zmiennej o nazwie numbers_iterator
# 3. Wykonaj na iteratorze funkcję __next__(), pobierając kolejny element (1) z listy i wypisz ten element na ekranie
# 4. Wykonaj na iteratorze funkcję __next__(), pobierając kolejny element (2) z listy i wypisz ten element na ekranie
# 5. Wykonaj na iteratorze funkcję __next__(), pobierając kolejny element (3) z listy i wypisz ten element na ekranie

