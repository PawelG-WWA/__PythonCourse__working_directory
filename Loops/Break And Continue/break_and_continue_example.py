# EXAMPLE 1
print('EXAMPLE 1 - break')
for x in range(0, 5):
    if x == 2:
        break
    print(x)
print('KONIEC break')

# EXAMPLE 1 - przebieg algorytmu
#
# 1. Do x przypisz wartość z zakresu (0)
# 2. Sprawdź, czy x jest równe 2
# 3. Nie, x nie jest równe dwa
# 4. Wypisz wartość x na ekran (0)
# 5. Do x przypisz kolejną wartość z zakresu (1)
# 6. Sprawdź czy x jest równe 2
# 7. Nie, x nie jest równe 2
# 8. Wypisz wartość x na ekran (1)
# 9. Do x przypisz kolejną wartość z zakresu (2)
# 10. Sprawdź czy x jest równe 2
# 11. Tak, x jest równe 2
# 12. Natychmiast przerwij wykonanie pętli (instrukcja break)
# 13. Wypisz na ekran napis 'KONIEC break'
# Wynik:
# 0
# 1
# KONIEC break



# EXAMPLE 2
print('EXAMPLE 2 - continue')
for x in range(0, 5):
    if x == 2:
        continue
    print(x)
print('KONIEC continue')


# Przebieg algorytmu:
#
# 1. Do x przypisz wartość z zakresu (0)
# 2. Sprawdź, czy x jest równe 2
# 3. Nie, x nie jest równe dwa
# 4. Wypisz wartość x na ekran (0)
# 5. Do x przypisz kolejną wartość z zakresu (1)
# 6. Sprawdź czy x jest równe 2
# 7. Nie, x nie jest równe 2
# 8. Wypisz wartość x na ekran (1)
# 9. Do x przypisz kolejną wartość z zakresu (2)
# 10. Sprawdź czy x jest równe 2
# 11. Tak, x jest równe 2
# 12. Przejdź do kolejnej iteracji (instrukcja continue)
# ... wykonuj kroki 1, 2, 3, 4 dopóki nie pobrane zostaną wszystkie cyfry z zakre range
# Wypisz na ekran napis 'KONIEC continue'
#
# Wynik:
# 0
# 1
# 3
# 4
# KONIEC continue