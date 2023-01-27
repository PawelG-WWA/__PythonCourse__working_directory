# ZADANIE
#
# Wiesz juz, ze zmienne przekazywane sa do funkcji przez referencje. Oznaczqa to, ze przekazanie typow mutowalnych spowoduje,
# ze przypisanie wartosci do elementow - np do elementu listy - spowoduje zmianę tego elementu rowniez w liscie przekazanej do funkcji
# w zakresie globalnym
#
# Czasami jednak chcemy, aby zmiany dokonywane na zmiennych wewnątrz funkcji nie miały efektu na zmienne przekazane
# z zakresu globalnego jako te argumenty
#
# Napisz funkcję modify_copy, która przyjmie trzy argumenty - the_list, the_dict oraz the_set. Następnie napisz ciało
# funkcji w taki sposób, aby zmiany dokonywane na przekazanej liście nie miały wpływu na zmienne z zakresu
# globalnego, które zostały przekazane do funkcji modify_copy jako argument. Następnie dokonaj jakichś zmian
# na argumentach wewnątrz funkcji modify_copy i wypisz na ekran co przechowują zmienne the_list, the_dict oraz the_set
#
# Wywołaj funkcję modify_copy przekazując jako argumenty listę, słownik i zbiór stworzone w zakresie globalnym
#
# Po wywołaniu modify_copy wypisz na ekran to, co przechowują zmienne the_list, the_dist oraz the_set w zakresie globalnym
#
# PRZYKŁADOWY WYNIK PROGRAMU:
# ---------------------
# modify_copy():
# ['x', 2, 3]      - w metodzie modify_copy zaktualizowano pierwszy element list na wartość x
# {'x': 0, 'y': 2} - w metodzie modify_copy zaktualizowano wartość klucza 'x' na 0
# {1, 2, 3, 'z'}   - w metodzie modify_copy do zbioru dodano element 'z'
# ---------------------
# main scope
# [1, 2, 3]        -lista z zakresu globalnego nie zmieniła się
# {'x': 1, 'y': 2} -słownik z zakresu globalnego nie zmienił się
# {1, 2, 3}        -zbiór z zakresu globalnego nie zmienił się

the_list = [1, 2, 3]
the_dict = { 'x': 1, 'y': 2 }
the_set = {1, 2, 3}