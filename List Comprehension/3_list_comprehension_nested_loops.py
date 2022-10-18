letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
pairs = [letter + str(number) for letter in letters for number in numbers]
print(pairs)

# Przebieg algorytmu:
#
# 1. Do zmiennej o nazwie letters przypisz listę trzech elementów [a, b, c]
# 2. Do zmiennej o nazwie numbers przypisz listę trzech elementów [1, 2, 3]
# 3. Pobierz element z listy letters i przypisz go do zmiennej letter: letter = a
# 4. Pobierz element z listy numbers i przypisz go do zmiennej number: number = 1
# 5. Zamień number, które jest typem liczby całkowitej (int) na napis (typ stringv - funkcja str())
# 6. Wykonaj konkatenację (złączenie - znak '+') dwóch napisów jednoelementowych 'a' i '1'
# 7. Dodaj rezultat ('a1') do listy wynikowej
# 8. Pobierz element z listy numbers i przypisz go do zmiennej number: number = 2
# 9. Zamień number, które jest typem liczby całkowitej (int) na napis (typ stringv - funkcja str())
# 10. Wykonaj konkatenację (złączenie - znak '+') dwóch napisów jednoelementowych 'a' i '2'
# 11. Dodaj rezultat ('a2') do listy wynikowej
# 12. Pobierz element z listy numbers i przypisz go do zmiennej number: number = 3
# 13. Zamień number, które jest typem liczby całkowitej (int) na napis (typ stringv - funkcja str())
# 14. Wykonaj konkatenację (złączenie - znak '+') dwóch napisów jednoelementowych 'a' i '3'
# 15. Dodaj rezultat ('a3') do listy wynikowej
# ... wykonaj kroki 3 - 15 dla kolejnych elementów listy letters: b oraz c
# 16. Przypisz listę wynikową do zmiennej o nazwie pairs
# 17. Wypisz na ekran listę wynikową pairs = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
#
#
# Dodatkowe wyjaśnienie
#
# Powyzszy algorytm jest równowazny z:
# pairs = []
# for letter in letters:
#     for number in numbers:
#         pairs.append(letter + str(number))