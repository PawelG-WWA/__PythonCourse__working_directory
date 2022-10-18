letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
pairs = [letter + str(number) for letter in letters if letter == 'a' for number in numbers if number % 2 == 0]
print(pairs)

# Przebieg algorytmu:
#
# 1. Do zmiennej o nazwie letters przypisz listę trzech elementów [a, b, c]
# 2. Do zmiennej o nazwie numbers przypisz listę trzech elementów [1, 2, 3]
# 3. Pobierz element z listy letters i przypisz go do zmiennej letter: letter = a
# 4. Sprawdź, czy element przypisany do zmiennej o nazwie letter jest równy znakowi 'a'
# 5. Jeśli nie jest równym przejdź do kroku 12. Tak, jest równy. Pobierz element z listy numbers i przypisz go do zmiennej number: number = 1
# 6. Sprawdź, czy element przypisany do zmiennej o nazwie number podzielony przez 2 daje resztę z dzielenia równą 0
# 7. Nie, pobierz kolejny element z listy numbers i przypisz go do zmiennej o nazwie number: number = 2
# 6. Sprawdź, czy element przypisany do zmiennej o nazwie number podzielony przez 2 daje resztę z dzielenia równą 0
# 8. Tak, Dodaj element zapisany pod zmienną o nazwie number do listy pairs
# 9. Pobierz kolejny element z listy numbers i przypisz go do zmiennej o nazwie number: number = 3
# 10. Sprawdź, czy element przypisany do zmiennej o nazwie number podzielony przez 2 daje resztę z dzielenia równą 0
# 11. Nie, zakończ wykonywanie iteracji po liście numbers.
# 12. Pobierz element z listy letters i przypisz go do zmiennej letter: letter = b
# ... wykonaj kroki 4 - 11 dla elementu b oraz c
# 13. Wypisz na ekranie listę pairs: ['a2']
#
#
# Dodatkowe wyjaśnienie
#
# Powyzszy algorytm jest równowazny z:
# pairs = []
# for letter in letters:
#     if letter == 'a':
#         for number in numbers:
#             if number % 2 == 0:
#                 pairs.append(letter + str(number))
#
#
# Jak widzisz, listy skłądane mogą być naprawdę skomplikowane. Zawsze rozwaz, czy na pewno chcesz skorzystać z ich mozliwości.
# 
# Często warto poświęcić zwięzłość zapisu kodu w jednej linijce dla czytelnośći i mozliwości łatwiejszego zrozumienia intencji autora