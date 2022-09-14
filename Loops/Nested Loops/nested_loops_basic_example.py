numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in numbers:
    for y in multipliers:
        print(x*y, end =' ')
    print('\n')

# Przebieg algorytmu
#
# 1. do nazwy numbers przypisz listę liczb od 1 do 10
# 2. do nazwy multipliers przypisz listę liczb od 1 do 10
# 3. z listy numbers pobierz element i przypisz go do x. X = 1
# 4. z listy multipliers pobierz element i przypisz go do y. Y = 1
# 5. wykonaj mnozenie x * y (1 * 1) i wypisz wynik na ekran (1)
# ... wykonaj kroki 4, 5 az pobrane będą wszystkie elementy z listy multipliers (y od 1 do 10)
# 6. wyjdź z pętli for y in multipliers i napisz na ekranie nową linię
# 7. pobierz element z listy numbers i przypisz go do x. X = 2
# ... wykonaj kroki 3,4,5,6 az pobrane będą wszystkie lementy z listy numbers (x od 1 do 10)

# Dodatkowe wyjaśnienie
#
# Program tworzy tabliczkę mnozenia w zakresie 100. Aby stworzyć tabliczkę mnozenia, nalezy
# pomnozyc przez siebie wszystkie liczby z dwóch kolekcji zawierających liczby od 0 do 10