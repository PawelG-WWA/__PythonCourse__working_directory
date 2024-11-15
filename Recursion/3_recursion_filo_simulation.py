def calculate_letters(words):
    result = 0
    items = list(words)
    while items:
        item = items.pop()
        if isinstance(item, list):
            items.extend(item)
        else:
            result += len(item)
    
    return result
        

list_of_words = ['one', 'seven', ['apple', 'juice'], ['ball', 'computer', 'candy', ['sport', ['programmer']]]]

print(calculate_letters(list_of_words))


# WYJAŚNIENIE
#
# Jak widzisz, w powyzszym przykladzie nie uzylismy funkcji rekurencyjnej, ale osiągnęliśmy taki sam efekt.
#
# Tak naprawdę, działanie funkcji rekurencyjnej zostało zasymulowane.
#
# Funkcja calculate_letters nadal przyjmuje liste wyrazów, która moze być listą zagniezdzonych list wyrazów.
#
# Tworzy zmienną result z wartością początkową 0.
#
# Następnie tworzy kopię pomocniczą listy words i zapisuje ją pod nazwą items
#
# Później wywoływana jest pętla while items: - przypomnieć nalezy, ze za instrukcją while występuje warunek logiczny
# określający zakończenie wywoływania pętli. Pusta lista jest tozsama z wartością logiczną false, a więc while items: oznacza,
# ze pętla while zakończy swoje działanie, jeśli lista items będzie pusta. Zapis while items: jest tozsamy z zapisem:
# while len(items) > 0:
#
# W pętli do nazwy item przypisywany jest wynik metody pop() wykonanej na liście items.
#
# Funkcja pop zwraca element z końca listy, a więc w tym wypadku items.pop() zwróci listę:
# ['ball', 'computer', 'candy', ['sport', ['programmer']]
# zagniezdzoną w liście items i usunie tę listę z items.
#
# Lista items po wykonaniu pop będzie zawierała następujące elementy:
# items = ['one', 'seven', ['apple', 'juice']]
#
# Następnie kod sprawdza, czy zmienna item jest listą. Tak, pod zmienną item przechowujemy listę:
# item = ['ball', 'computer', 'candy', ['sport', ['programmer']]
# poniewaz ten element został zwrocony przez funkcję pop() wykonaną na liście items.
#
# Skoro pod item przechowujemy listę, to rozszerzamy listę items o listę przechowywaną pod item za pomocą funkcji extend.
#
# Funkcja extend sprawia, ze do listy A dołączamy elementy listy B. Na przykład, jeśli:
# A = [1, 2, 3]
# B = [4, 5, 6]
#
# to A.extend(B) sprawi, ze A = [1, 2, 3, 4, 5, 6]
#
# Wobec tego items.extend(item), gdzie:
# items = ['one', 'seven', ['apple', 'juice']]
# item = ['ball', 'computer', 'candy', ['sport', ['programmer']]
#
# sprawi, ze items będzie referencją do następującej listy:
# items = ['one', 'seven', ['apple', 'juice'], 'ball', 'computer', 'candy', ['sport', ['programmer']]]
#
# Pozbyliśmy się tym samym jednego zagniezdzenia i przechodzimy do kolejnej iteracji pętli while
#
# Znowu items.pop() zwraca listę, tym razem: ['sport', ['programmer']]
#
# Ponownie wywołujemy items.extend(item), i lista items przybiera postać:
# items = ['one', 'seven', ['apple', 'juice'], 'ball', 'computer', 'candy', 'sport', ['programmer']]
#
# Przechodzimy do kolejnej iteracji pętli while i ponownie items.pop() zwraca listę, tym razem jednoelementową:
# ['programmer']
#
# items.extend(item) sprawia, ze lista items jest referencją do następującej listy:
# items = ['one', 'seven', ['apple', 'juice'], 'ball', 'computer', 'candy', 'sport', 'programmer']
#
# Następnie iteracja while do item przypisuje słowo 'programmer'. To słowo nie jest listą, więc dodajemy do result
# ilość jego znaków.
#
# Kolejna iteracja zwraca 'sport' i ponownie dodajemy do result ilość znaków
#
# Zmienna result jest powiększana o ilość znaków kolejnych elementów az do momentu, w którym items.pop() zwraca
# listę ['apple', 'juice']. Wywoływana jets funkcja extend: items.extend(item), po czym lista items przybiera postać:
# item = tems = ['one', 'seven', 'apple', 'juice']
#
# Zaden z kolejnych elementów nie jest juz listą, więc wszystkie iteracje az do momentu, w ktorym pop zwróci ostatni element
# listy item czyniąc ją pustą, będą dodawały liczbę znaków kolejnych wyrazów do zmiennej result.
#
# Pętla while zostanie przerwana, poniewaz lista item nie będzie zawierała zadnych elementów, co jest warunkiem zakończenia
# pętli
#
# Wynik result = 50 zostanie zwrócony i wypisany na ekranie
#
# Osiągnęliśmy dokładnie ten sam rezultat, co z wykorzystaniem rekurencji z drugiego przykładu z biezącego folderu.
#
# Tak naprawdę zasymulowaliśmy rekurencję - zanim przejdziemy do zliczania kolejnych liter ze słów,
# wywołujemy algorytm ponownie, jeśli dany element jest listą, a nie słowem.
#
# Rekurencja to skomplikowany proces i moze przyspozyc sporo problemów w trakcie nauki. Nie zrazaj się i spróbuj wykonać ćwiczenia!