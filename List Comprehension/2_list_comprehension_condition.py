words = ['apple', 'pineapple', 'watermelon', 'peach', 'cocumber', 'aeroplane', 'ball', 'glass', 'zone', 'water']

words_longer_than_five = [w for w in words if len(w) > 5]

words_with_c_character = [w for w in words if 'c' in w]

words_starting_with_a = [w for w in words if w.startswith('a')]

words_longer_than_four_capitalized = [w.upper() for w in words if len(w) > 4]

words_without_first_letter_if_they_start_with_p = [w[1:len(w)] for w in words if w.startswith('p')]

words_from_second_half_of_the_list_with_OK_suffix_if_they_start_with_a_and_end_with_e = [w + '-OK' for w in words[len(words)//2:len(words)] if w.startswith('a') and w.endswith('e')]

print('words_longer_than_five: %s' % words_longer_than_five)
print('words_with_c_character: %s' % words_with_c_character)
print('words_starting_with_a: %s' % words_starting_with_a)
print('words_longer_than_four_capitalized: %s' % words_longer_than_four_capitalized)
print('words_without_first_letter_if_they_start_with_p: %s' % words_without_first_letter_if_they_start_with_p)
print('words_from_second_half_of_the_list_with_OK_suffix_if_they_start_with_a_and_end_with_e: %s' % words_from_second_half_of_the_list_with_OK_suffix_if_they_start_with_a_and_end_with_e)

# Wyjaśnienie
#
# Jako, ze przykładów jest bardzo duzo, nie będę opisywał przebiegu algorytmu kazdego z nich.
#
# Kazdy przykład działa bowiem wg tego samego schematu:
# 1. Pobierz elementy iterowalnego obiektu - w naszym przypadku listy words
# 2. Sprawdź, czy dla danego elementu jest spełniony warunek zdefiniowany przez if
# 3. Przypisz element do zmiennej o nazwie w
# 4. Wykonaj na tym elemencie wyrazenie zdefiniowane po lewej stronie for
# 5. Dodaj element do nowej kolekcji
# 6. Wykonuj kroki 1-5 az do przetworzenia wszystkich elementow kolekcji
# 7. Zwróć listę utworzoną w wyniki iteracji listę i przypisz ją do zmiennej wskazanej po lewej stronie znaku równości
# 8. Na samym końcu wypisz wszystkie listy
#
# words_longer_than_five - warunek if filtruje wszystkie słowa dłuzsze niz 5 znaków
# words_with_c_character - warunek if filtruje wszystkie słowa zawierające literę c
# words_starting_with_a - warunek if filtruje wszystkie słowa zaczynające się od litery a
# words_longer_than_four_capitalized - warunek if filtruje wszystkie słowa dłuzsze niz 4 znaki i kazde z takich słów zamienia na słowo pisane wielkimi literami
# words_without_first_letter_if_they_start_with_p - warunek if filtruje wszystkie słowa zaczynające się od litery p, a następnie kazde takie słowo jest pozbawiane pierwszej litery
# words_from_second_half_of_the_list_with_OK_suffix_if_they_start_with_a_and_end_with_e - Spośród słów znajdujących się od połowy do końca listy words,
#                                                                                         warunek if filtruje wszystkie słowa zaczynające się od litery a i
#                                                                                         kończące się literą e,  a następnie do kazdego takie słowa dodaje napis "-OK"
#
# Jak widzisz, instrukcje list kładanych mogą być proste i zwięzłe, a takze skomplikowane i trudne do odczytania za pierwszym razem.
#
# Nigdy nie powinieneś się obawiać nazywania zmiennych tak jak w powyzszym przykładzie - opisowymi słowami. Podejrzewam jednak,
# ze niektóre z tych nazw, jak i instrukcji, wprawiają Cię w zakłopotanie - mnie równiez. Kazda lista składana moze być przepisana
# na pętlę for, która nie jest tak zwięzła, ale z pewnością bardziej czytelna.
#
# Warto zastanowić się, czy nie lepiej czasami postawić na czytelność za cenę zwięzłości.
#
# Ostatni z przykładów wydaje się być świetnym kandydatek do zastosowania pętli for zamiast instrukcji listy składanej
#
# Kazdy z powyzszych przykładów jest równowazny z:
#
# res = []
# for w in words:
#     if warunek:
#         res.append(wyrazenie)
#
# Dla przykładu
# words_longer_than_five = [w for w in words if len(w) > 5]:
#
# words_longer_than_five = []
# for w in words:
#     if len(w) > 5:
#         words_longer_than_five.append(w)
#
#
# Dla przykładu
# words_without_first_letter_if_they_start_with_p = [w[1:len(w)] for w in words if w.startswith('p')]
#
# words_without_first_letter_if_they_start_with_p = []
# for w in words:
#     if w.startswith('p'):
#         words_without_first_letter_if_they_start_with_p.append(w[1:len(w)])