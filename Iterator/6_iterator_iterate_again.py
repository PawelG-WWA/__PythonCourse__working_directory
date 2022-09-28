numbers = [1, 2]

numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))

numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))

print('THE END')

# Przebieg algorytmu:
#
# 1. Do zmiennej o nazwie numbers przypisz listę cyfr 1, 2 - numbers = [1, 2]
# 2. Z listy numbers pobierz iterator i przypisz go do zmiennej o nazwie numbers_iterator
# 3. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (1) z listy i wypisz ten element na ekranie
# 4. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (2) z listy i wypisz ten element na ekranie
# 5. Z listy numbers pobierz iterator i przypisz go do zmiennej o nazwie numbers_iterator
# 6. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (1) z listy i wypisz ten element na ekranie
# 7. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (2) z listy i wypisz ten element na ekranie
# 8. Wypisz na ekranie napis 'THE END'
#
# Dodatkowe wyjaśnienie
#
# Lista numbers zawiera dwa elementy 1 oraz 2, a więc mozemy przeiterować po niej dwa razy (dwukrotne wywołanie funkcji next na iteratorze
# pozyskanym z listy numbers)
#
# Jak wiemy, kolejne wywołanie next zakończy się zgłoszeniem błędu (wyjątku) StopIteration.
#
# Aby móc iterować po tej samej liście od nowa, nalezy wywołać po raz kolejny funkcję iter na obiekcie listy
# i przypisać zwrócony obiekt iteratora do zmiennej
#
# następnie, ponowne wywołania next(numbers_iterator) będą pobierać kolejne elementy listy numbers
# tyle razy ile jej uzyjemy, o ile nie wystąpi wyjątek StopIteration wskazujący,
# ze nie mozna juz dalej iterować po elementach listy, poniewaz przeiterowano juz całą listę