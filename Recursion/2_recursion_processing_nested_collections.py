def calculate_letters(words):
    if len(words) == 0:
        return 0

    result = 0

    for item in words:
        if isinstance(item, list):
            result += calculate_letters(item)
        else:
            result += len(item)
        
    return result


list_of_words = ['one', 'seven', ['apple', 'juice'], ['ball', 'computer', 'candy', ['sport', ['programmer']]]]

print(calculate_letters(list_of_words))

# WYJAŚNIENIE
#
# Funkcja calculate_letters zlicza ilość liter w zagniezdzonych listach
#
# Na początku określamy warunek brzegowy rekurencji - jeśli przekazana lista ma 0 elementów, zwróć 0. Akurat
# w tym przykładzie nie jest to konieczne, jednak zastosowanie tego warunku jest dobrym przyzwyczajeniem
#
# Następnie ustawiamy zmienną result na 0. Przy kazdym wywołaniu rekurencyjnym funkcji calculate_letters, kazde
# z wywołań będzie posiadało własną zmienną result z przypisanym 0 jako wartością startową.
#
# Później przechodzimy po elementach przekazanej listy wyrazów
#
# Jeśli w danej iteracji pętli for aktualnie przetwarzany element jest listą, to do zmiennej result przypisz wynik
# rekurencyjnego wywołania funkcji calculate_letters. Chodzi o to, ze jeśli element item za którymś przejściem pętli for
# okaze się być listą, musimy zliczyć litery słów będących elementami tej listy, a po zakończeniu danego przetwarzania rekurencyjnego
# dodamy do zmiennej result sumaryczny wynik i zwrócimy go, po czym pętla for pobierze kolejny element z oryginalnej listy.
#
# Jeśli więc przetworzymy elementy 'one' (3 litery), a potem 'seven' (5 liter) aktaulny wynik result po dwóch iteracjach
# pętli będzie wynosił 8. Następny element to lista dwuelementowa ['apple', 'juice']. funkcja calculate_letters wywoła samą siebie,
# ale z argumentem będącym dwuelementową listą ['apple', 'juice']. Zmienna result w wywołującej rekurencyjnie samą siebie metodzie
# calculate_letters nadal wynosi 8.
#
# W tym momencie wywołanie calculate_letters(['apple', 'juice']) stworzy swoją zmienną result = 0 i będzie przechodziło po
# elementach listy. Apple zawiera 5 liter, tak samo jak słowo juice. Po przejściu pętli for zmienna result jest równa 10.
# Rekurencyjne wywołanie calculate_letters kończy się, a program wraca do nadrzędnej funkcji calculate_result, która wywołała
# samą siebie z argumentem ['apple', 'juice']. W tej nadrzędnej funkcji result było równe 8. Do 8 więc dodawane jest 10 zwrócone
# z rekurencyjnego wywołania funkcji calculate_letters(['apple', 'juice']), a pętla for przechodzi do kolejnego elementu,
# a więc duzej listy posiadającej zagniezdzone inne listy: ['ball', 'computer', 'candy', ['sport', ['programmer']]] i wykonuje
# algorytm w ten sam sposób