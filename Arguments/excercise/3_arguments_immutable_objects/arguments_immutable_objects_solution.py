# ZADANIE
#
# W zakresie globalnym stwórz zmienną number z przypisaną dowolną wartością
#
# Wypisz na ekranie jej id oraz wartość
#
# Napisz funkcję immutable_test, która przyjmuje jako argument liczbę (np. nazwa number),
# a następnie wypisze na ekranie jej id oraz wartość
#
# Następnie wewnątrz funkcji immutable_test przypisz do zmiennej number nową wartość i ponownie wypisz jej
# id oraz wartość
# 
# Wywołaj funkcję immutable_test
#
# Po wywołaniu funkcji immutable_test ponownie wypisz id oraz wartość zmiennej number z zakresu globalnego
#
# Porównaj wyniki i opisz swoje wnioski

def immutable_test(number):
    print('immutable_test - id: %s, number value: %s' % (id(number), number))
    number = number + 1
    print('immutable_test - id: %s, number value: %s' % (id(number), number))

number = 10
print('id: %s, number value: %s' % (id(number), number))

immutable_test(number)

print('id: %s, number value: %s' % (id(number), number))

# WNIOSKI
#
# UWAGA - NA TWOIM KOMPUTERZE WARTOŚCI WYPISANE PRZEZ FUNKCJĘ id(number)
# PRAWDOPODOBNIE BĘDĄ SIĘ RÓZNIĆ!
#
# Zmienna number w zakresie globalnym ma wartość 10, id tej zmiennej jest równe:
# id(number) = 140374161156688
#
# Przekazujemy do funkcji immutable_test zmienną number z zakresu globalnego,
# a więc number wewnątrz immutable_test będzie równe number z zakresu globalnego,
# poniewaz zmienne w pythonie są przekazywane do funkcji poprzez referencję.
#
# Dlatego tez wywołanie funkcji immutable_test(number) spowoduje wypisanie najpierw linii:
# immmutable_test - id: 140374161156688, number value: 10
#
# Zwróc uwagę, ze id zmiennej number wewnątrz immutable_test jest takie samo jak id zmiennej
# number poza wywołaniem funkcji! To właśnie dzięki temu, ze zmienne są przekazywane przez referencje,
# co oznacza, ze wewnątrz immutable_test posługujemy się tą samą zmienną, co na zewnątrz immutable_test!
#
# Wiemy jednak, ze liczby całkowite są typem niemutowalnym
#
# Zmieńmy więc wartość number wewnątrz funkcji immutable_test na przykład na number = number + 1
#
# Wypisujemy ponownie id i wartość zmiennej number, na której operujemy wewnątrz funkcji immutable_test:
# immutable_test - id: 140634946202224, number value: 11
#
# id zmiennej number zmieniło się, tak jak jej wartość!
#
# Stało się tak dlatego, ze liczby są niemutowalnym typem danych
#
# Oznacza to, ze wywołanie:
# number = number + 1
# wewnątrz funkcji immutable_test nie zmienia oryginalnej wartości number z zakresu globalnego, ale tworzy
# nową zmienną typu liczbowego przechowywaną pod innym adresem, na który wskazuje nazwa number dostępna w
# zakresie lokalnym funkcji immutable_test!
#
# Na końcu, po wywołaniu immutable_test wywołujemy jeszcze raz:
# print('id: %s, number value: %s' % (id(number), number))
#
# co daje wynik:
# id: 140374161156688, number value: 10
#
# a więc dokładnie taki sam, jak za pierwszym razem, przed wywołaniem immutable_test i przypisaniem do
# lokalnego number wewnątrz immutable_test nowej wartości!
#
# Wniosek - dopóki nie przypiszemy do przekazanej jako argument zmiennej nowej wartości (a w zasadzie, dopóki
# do lokalnej zmiennej - w tym wypadku argumentu funkcji nie przypiszemy nowej wartości), argument ten
# wskazuje na ten sam obiekt, co przekazana i przypisana do niego referencja
#
# Mówiąc krótko, o ile wewnątrz funkcji nie nastąpi przypisanie do argumentu który jest lokalną zmienną funkcji,
# to - jak w powyzszym przykładzie - lokalny argument (number) jest równy (jest tą samą referencją) zmiennej
# number z zakresu globalnego