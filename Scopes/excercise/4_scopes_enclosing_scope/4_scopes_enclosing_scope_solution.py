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
#   ODPOWIEDŹ: zakres globalny
#
# 2. W jakim zakresie znajduje się drugie zdanie, które zostało pobrane z cytatu w funkcji enclosing_function względem:
#    -funkcji enclosing_function
#    -funkcji get_k_word_from_second_sentence(k)
#    ODPOWIEDŹ:
#    względem funkcji enclosing_function jest to zakres lokalny
#    względem funkcji get_k_word_from_second_sentence jest to zakres zawierający (enclosing)

quote = 'To learn one must be humble. But life is the great teacher.'

def enclosing_function():
    index_of_first_dot = quote.index('.')
    second_sentence = quote[index_of_first_dot+1:len(quote)].lstrip()
    
    def get_k_word_from_second_sentence(k):
        second_sentence_splitted = second_sentence.split(' ')

        if k-1 >= 0 and k <= len(second_sentence_splitted):
            return second_sentence_splitted[k-1]
        
        return "k is out of array"

    return get_k_word_from_second_sentence(3)


print(enclosing_function())


# Wyjaśnienie
#
# Zmienna o nazwie quote jest stworzona w zakresie globalnym. Oznacza to, ze mozemy tej zmiennej uzywać bez zadnych dodatkowych
# instrukcji w funkcjach (o ile nie będziemy próbowali utworzyć zmiennej o tej samej nazwie, której wartość będzie wyliczana z quote, np. quote = quote...)
#
# Następenie definiujemy funkcję enclosing_function, która nie przyjmuje zadnych argumentów, poniewaz operuje ona na zdefiniowanej
# w zakresie globalnym zmiennej quote.
#
# Pobieramy indeks, na którym znajduje się pierwsza kropka (gdzie kończy się pierwsze zdanie)
#
# Potem korzystamy ze składni listy składanej - do zmiennej o nazwie second_sentence przypisujemy drugie zdanie, które rozpoczyna się
# od indeksu ostatniej kropki + 1, a kończy na długości napisu (len(quote)) przechowywanego pod nazwą quote. Na samym końcu wykonujemy
# na wyniku funkcję lstrip(), która usuwa spacje występujące po lewej stronie otrzymanego napisu (w naszym przykladzie, przed wywołaniem
# lstrip() napis po wykonaniu instrukcji listy składanej wygląda tak: ' But...'. Po uzyciu lstrip() usuwana jest poprzedzająca spacja,
# więc otrzymujemy drugie zdanie zaczynające się od 'But...').
#
# Następnie definiujemy funkcję get_k_word_from_second_sentence, która przyjmuje parametr k, będącym numerem słowa, które chcemy pobrać ze zdania
#
# Zmienna second_sentence jest zmienną lokalną dla funkcji enclosing_function, ale nie jest lokalna dla get_k_word_from_second_sentence -
# w tej funkcji Python będzie poszukiwał tej zmiennej w zakresie zawierającym (a więc w funkcji enclosing_function).
#
# Napis przechowywany pod zmienną second_sentence w funkcji get_k_word_from_second_sentence wykorzystujemy do tego, aby słowa zawarte
# w tym napisie wyodrębnić do listy (funkcja split(' ')).
#
# Następnie sprawdzamy, czy argument k przekazany do funkcji nie jest spoza zakresu listy second_sentence_splitted przechowującej słowa
# drugiego zdania, tzn. czy np. nie przekazano -1 lub numeru słowa, które nie istnieje w napisie.
#
# Jeśli k jest zawarte w liczbie słów drugiego zdania, tzn. z tablicy second_sentence_splitted da się pobrać słowo uzywając parametru k,
# to funkcja get_k_word_from_second_sentence zwróci słowo występujące na k-miejscu (np słowo nr 3).
#
# Jeśli k nie spełnia tego warunku, zostanie wypisany komunikat 'k is out of array'
#
# W kolejnej linii funkcja enclosing_function wywołuje get_k_word_from_second_sentence(3) i zwraca wynik. Oznacza to, ze funkcja 
# enclosing_function zwróci wynik zwrócony przez wewnętrzną funkcję get_k_word_from_second_sentence(3).
#
# Ten wynik zostanie uzyty na samym końcu w funkcji print, dzięki czemu po wykonaniu programu zobaczymy na ekranie słowo 'is'