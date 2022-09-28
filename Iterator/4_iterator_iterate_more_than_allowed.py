numbers = [1, 2, 3]

numbers_iterator = iter(numbers)

print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))

print('THE END')

# Przebieg algorytmu:
#
# 1. Do zmiennej o nazwie numbers przypisz listę cyfr 1, 2, 3 - numbers = [1, 2, 3]
# 2. Z listy numbers pobierz iterator i przypisz go do zmiennej o nazwie numbers_iterator
# 3. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (1) z listy i wypisz ten element na ekranie
# 4. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (2) z listy i wypisz ten element na ekranie
# 5. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (3) z listy i wypisz ten element na ekranie
# 6. Wykonaj na iteratorze funkcję __next__() wywołując wbudowaną funkcję next(), pobierając kolejny element (?) z listy i wypisz ten element na ekranie
# 7. Zakończ natychmiast program z powodu błędu (wyjątku) StopIteration
#
# Dodatkowe wyjaśnienie
#
# Lista posiada trzy elementy - 1, 2, 3. Mozemy wykonać na niej 3 iteracje, pobierając w kazdej z nich
# kolejne elementy 1, 2 oraz 3. Zostają one wypisane na ekranie.
#
# Gdy nie ma juz więcej elementów do pobrania (nie mozemy juz dalej iterować po elementach listy, poniewaz więcej nie ma),
# a mimo to wykonamy metodę next(numbers_iterator), program zgłosi tzw. wyjątek, który mozemy póki co nazywać błędem.
#
# Wyjątki to po prostu nieoczekiwane, wyjątkowe zdarzenia, które kończą program, o ile się ich nie obsłuzy
#
# Powyzej świadomie nie obsluzyliśmy wyjątku, aby zakończyć działanie programu natychmiast, gdy spróbujemy
# wykonać jedną iterację więcej, niz jest to zezwolone ze względu na ilość elementów listy
#
# Jeśli uruchomisz program zauwazysz, ze po wypisaniu ponizszych cyfr:
# 1
# 2
# 3
#
# zostanie wyświetlona informacja o błędzie:
# Traceback (most recent call last):
#  File "your_path/__PythonCourse__working_directory/Iterator/4_iterator_iterate_more_than_allowed.py", line 8, in <module>
#    print(next(numbers_iterator))
# StopIteration
#
# Zgłoszony przez Pythona błąd (wyjątek) to StopIteration. Błąd ten informuje nas o tym, ze nie mozemy juz więcej iterować
# po elementach listy numbers, poniewaz przeiterowany po wszystkich elementach znajdujących się na liście.
#
# w pliku 5_iterator_finish_iteration.py mozesz zobaczyć, jak poradzić sobie z tą sytuacją