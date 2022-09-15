# EXAMPLE 1
print('#EXAMPLE 1')
for x in range(0, 3):
    if x == 3:
        break
else:
    print('Blok else')

# EXAMPLE 1 - Przebieg algorytmu:
#
# 1. Do x przypisz wartość z zakresu <0, 3) - x = 0
# 2. Sprawdź czy x jest równie 4 - nie, nie jest równe
# ... wykonuj kroki 1, 2 do samego końca, przypisując w kadej iteracji kolejne liczby z zakresu range
# 3. Wykonaj blok else wypisując na ekran napis 'Blok else' - zaden x z zakresu nie był równy 3, więc instrukcja break nie wykonała się
#    i mozna wykonać blok else dla pętli
#  (jak wspominano wcześniej funkcja range(x, y) zwraca przedział prawostronnie otwarty, tj. zakres do liczby y, ale bez liczby y, lub mniejsze od y)
#
# Wynik algorytmu EXAMPLE 1:
#
# 'Blok else'


# EXAMPLE 2
print('#EXAMPLE 2')
for x in range(0, 3):
    if x == 1:
        break
else:
    print('Blok else nie wykona się')
print('blok else nie wykonał się')

# EXAMPLE 2 - Przebieg algorytmu:
#
# 1. Do x przypisz wartość z zakresu <0, 3) - x = 0
# 2. Sprawdź czy x jest równie 1 - nie, nie jest równe
# 3. Weź kolejną liczbę z zakresu range - x = 1
# 4. Sprawdź, czy x jest równe 1 - tak, jest równe 1
# 5. Wykonaj instrukcję break, natychmiast przerywając działanie pętli - napotkanie instrukcji break w pętli powoduje pominięcie bloku else dla pętli
# 6. Wypisz na ekranie napis 'blok else nie wykonał się'
#
# Wynik algorytmu EXAMPLE 2:
#
# 'blok else nie wykonał się'


# EXAMPLE 3
print('#EXAMPLE 3')
x = [1, 2, 3]
while x:
    number = x.pop() # funkcja pop zdejmuje element z końca listy, zwraca go i usuwa z listy,
                     # po operacji pop() lista x jest równa [1, 2], number = 3
    if number == 4:
        break
    print(number)
else:
    print('Blok else')

# EXAMPLE 3 - przebieg algorytmu
#
# 1. Przypisz do x listę cyfr 1, 2, 3
# 2. Sprawdź, czy lista x nie jest pusta - nie, nie jest pusta. Wejdź do bloku pętli
# 3. Pobierz ostatni element z listy (pop()), usuń go z listy i przypisz do nazwy number (number = 3, x = [1, 2])
# 4. Jeśli wartość przechowywana pod number jest równa 4, wykonaj instrukcję break
# 5. Wypisz wartość number (3) na ekran
# ... wykonuj kroki 2, 3, 4, 5 az do samego końca (dopóki lista nie będzie pusta, czyli az warunek pętli nie będzie spełniony
#     aby warunek pętli nie był spełniony, x musi być pustą listą: x = [], pusta lista przy teście logicznym zwraca False, wówczas
#     pętla while nie wykona się)
# 6. Wejdź do bloku else pętli i wypisz na ekran napis 'Blok else' (nie wykonaliśmy instrukcji break w trakcie wykonywania pętli
#    poniewaz zadna z wartości number nie była równa 4)
#
# Wynik algorytmu EXAMPLE 3:
# 3
# 2
# 1
# Blok else


# EXAMPLE 4
print('#EXAMPLE 4')
x = [1, 2, 3]
while x:
    number = x.pop()
    if number == 1:
        break
    print(number)
else:
    print('Blok else nie wykona się')
print('Blok else pętli nie wykonał się')

# EXAMPLE 3 - przebieg algorytmu
#
# 1. Przypisz do x listę cyfr 1, 2, 3
# 2. Sprawdź, czy lista x nie jest pusta - nie, nie jest pusta. Wejdź do bloku pętli
# 3. Pobierz ostatni element z listy (pop()), usuń go z listy i przypisz do nazwy number (number = 3, x = [1, 2])
# 4. Jeśli wartość przechowywana pod number jest równa 1, wykonaj instrukcję break
# 5. Wypisz wartość number (3) na ekran
# 6. Sprawdź, czy lista x nie jest pusta - nie, nie jest pusta. Wejdź do bloku pętli
# 7. Pobierz ostatni element z listy (pop()), usuń go z listy i przypisz do nazwy number (number = 2, x = [1])
# 8. Jeśli wartość przechowywana pod number jest równa 1, wykonaj instrukcję break
# 9. Wypisz wartość number (2) na ekran
# 10. Sprawdź, czy lista x nie jest pusta - nie, nie jest pusta. Wejdź do bloku pętli
# 11. Pobierz ostatni element z listy (pop()), usuń go z listy i przypisz do nazwy number (number = 1, x = [])
# 12. Jeśli wartość przechowywana pod number jest równa 1, wykonaj instrukcję break - tak wartość number jest równa 1, wykonaj break
# 13. WYpisz na ekran napis 'Blok else pętli nie wykonał się'
#
# Wynik algorytmu EXAMPLE 4:
#
# 3
# 2
# 'Blok else pętli nie wykonał się'
