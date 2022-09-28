numbers = [1, 2, 3]

numbers_iterator = iter(numbers)

try: # otwieramy sekce krytycza, w której moze wystąpić błąd, tzw wyjątek kończący program
    print(next(numbers_iterator))
    print(next(numbers_iterator))
    print(next(numbers_iterator))
    print(next(numbers_iterator))
except StopIteration: # przechwytujemy błąd, obsługujemy go i kontynuujemy działanie programu
    print('Dzięki temu moemy kontynuować program')

print('THE END')

# Przebieg algorytmu
#
# 1. Do zmiennej o nazwie numbers przypisz listę cyfr 1, 2, 3 - numbers = [1, 2, 3]
# 2. Z listy numbers pobierz iterator i przypisz go do zmiennej o nazwie numbers_iterator
# 3. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (1) z listy i wypisz ten element na ekranie
# 4. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (2) z listy i wypisz ten element na ekranie
# 5. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (3) z listy i wypisz ten element na ekranie
# 6. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (3) z listy i wypisz ten element na ekranie
# 7. Wypisz na ekranie napis 'Dzięki temu moemy kontynuować program'
# 8. Wypisz na ekranie napis 'THE END'
#
# Dodatkowe wyjaśnienie:
#
# W liście znajdują się 3 elementy - 1, 2 oraz 3
# 
# Wywolanie funkcji next spowoduje błąd programu. Błąd moze równie wystąpić, jeśli spróbujemy odnieść się do elementu listy
# uzywając indeksu spoza zakresu, np. numbers[4].
#
# W powyzszym kodzie błąd (wyjątek), zostanie zgłoszony po wywołaniu metody next(numbers_iterator) po raz czwarty.
# Jako, ze na liście są tylko 3 elementy, próba iteracji więcej niz 3 razy zgłasza błąd (wyjątek). Błąd (wyjątek) ten
# ten jest typu StopIteration
#
# Sekcja krytyczna otwierana instrukcją try: występuje zawsze w parze z instrukcją except - słuzy ona do wskazania,
# błędy (wyjątki) jakiego typu przechwytujemy. W naszym wypadku próba iteracji więcej razy niz jest to zezwolone
# ze względu na ilość elementów na liście zakończy się zgłoszeniem błędu (wyjątku) typu StopIteration, i taki właśnie
# błąd (wyjątek) przechwytujemy.
#
# Bez przechwycenia i obsługi wyjątku jego zgłoszenie sprawiłoby, e program by się natychmiast zakończył. Blok try:except
# umozliwia poradzenie sobie z taką wyjątkową sytuacją i kontynuowanie wykonania programu.
# 
# Wypisujemy na ekranie napis 'Dzięki temu moemy kontynuować program', a potem napis 'THE END'
#
# powyzszy kod jest równowazny z następującym:
# for x in numbers:
#    print(x)