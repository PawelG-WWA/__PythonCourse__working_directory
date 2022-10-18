numbers = [1, 2, 3]
result = [x * 2 for x in numbers]
print(result)

# Przebieg algorytmu
#
# 1. Do zmiennej o nazwie numbers przypisz listę [1, 2, 3]
# 2. Z listy numbers pobierz element na pozycji 0 i przypisz go do zmiennej x: x = 1
# 3. Pomnóz x razy 2: 1 * 2 = 2
# 4. Z listy numbers pobierz element na pozycji 1 i przypisz go do zmiennej x: x = 2
# 5. Pomnóz x razy 2: 2 * 2 = 4
# 6. Z listy numbers pobierz element na pozycji 2 i przypisz go do zmiennej x: x = 3
# 7. Pomnóz x razy 2: 3 * 2 = 6
# 8. Przypisz wynik wykonania instrukcji listy składanej do zmiennej result
# 9. Wypisz na ekranie listę result.
#
# Wynik:
# [2, 4, 6]
#
#
# Dodatkowe wyjaśnienie:
#
# Zapis listy składanej result = [x * 2 for x in numbers] jest równowazny z ponizszym algorytmem pętli for:
# 
# result = []
# for x in numbers:
#     result.append(x + 1)
