# ZADANIE
#
# Napisz funkcję enclosing_function, która z podanego cytatu (quote) pobierze drugie zdanie ('But life is the great teacher')
#
# Następnie w funkcji enclosing_function zdefiniuj inną funkcję (np. get_k_word_from_second_sentence), która ze zdania
# pobranego przez enclosing function ('But life is the great teacher'), wybierze słowo na wskazanym miejscu k.
#
# Np. Jeśli wywołasz funkcję z argumentem 0 (get_k_word_from_second_sentence(1)), powinieneś zwrócić słow 'But'.
# Jeśli wywołasz z argumentem (3), powinieneś zwrócić słowo 'is'
#
# Napisz kod w taki sposób, aby uniknąć mozliwości wystąpienia błędu IndexError: list index out of range,
# jeśli wywołasz funkcję z argumentem przekraczającym ilość słów w zdaniu (np. get_k_word_from_second_sentence(10))
#
# Zwróć z funkcji get_k_word_from_second_sentence słowo na miejscu k, a z funkcji enclosing_function wynik wywołania get_k_word_from_second_sentence
#
# Na końcu wypisz odnalezione słowo
#
# Oczekiwany wynik:
# wywołanie funkcji enclosing_function zwracającej wynik wywołania get_k_word_from_second_sentence(3) powinno zwrócić słowo 'is',
# które powinno być wypisane na ekranie
#
#
# DODATKOWE PYTANIA:
# 1.W jakim zakresie jest zdefiniowana zmienna quote? Czy aby operować na niej w funkcji enclosing function,
#   musisz wykonać jakieś dodatkowe czynności?
# 2. W jakim zakresie znajduje się drugie zdanie, które zostało pobrane z cytatu w funkcji enclosing_function względem:
#    -funkcji enclosing_function
#    -funkcji get_k_word_from_second_sentence(k)


quote = 'To learn one must be humble. But life is the great teacher.'

# Tu napisz kod

print(enclosing_function()) # jeśli wewnątrz funkcji enclosing_function wywołasz get_k_word_from_second_sentence(3),
                            # ta linijka powinna wypisać na ekranie słowo 'is'
