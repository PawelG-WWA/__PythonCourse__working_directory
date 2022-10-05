# Zadanie
#
# Macierz to tablica tablic, znana tez jako tablica wielowymiarowa (lub lista list znana jako lista wielowymiarowa)
#
# Macierz dwuwymiarowa to macierz zawierająca x wierszy oraz y kolumn, wyglądem przypomina tabelę
#
# Poniej znajduje się przykład macierzy dwuwymiarowej:
# |------|
# | 1  2 |
# | 3  4 |
# |------|
#
# Macierz posiada dwa wiesz i dwie kolumny.
# W pierwszym wierszu w kolumniej pierwszej znajduje się wartość 1, a w kolumnie drugiej wartość 2
# W drugim wiereszu w kolumnie pierwszej znajduje się wartoś 3, a w kolumnie drugiej wartość 4
#
# Jako, ze macierz to po prostu lista list, definiujemy ją jako listę, której elementy to listy.
#
# Powyzsza macierz w Pythonie moze zostać zapisana następująco:
# matrix = [[1, 2], [3, 4]]
#
# Przejdź przez podaną macierz klasyczną pętlą for tak, aby otrzymać na ekranie następujący wynik:
# 1 2
# 3 4
#
# Następnie przejdź przez podaną macierz uzywając wyłącznie pobranych z list iteratorow i metody next, aby otrzymać na ekranie następujący wynik:
# 1 2
# 3 4
#
# mozesz uzyc dowolnej metody, albo wbudowanych metod iter i next, albo metod __iter__ i __next__ nalezących do listy i iteratora

matrix = [[1, 2],
          [3, 4]]

for row in matrix:
    for y in row:
        print(y, end=' ')
    print()

print()

# MANUALNE ITEROWANIE
matrix_row_iterator = iter(matrix)
matrix_column_iterator = iter(next(matrix_row_iterator))

# powyzsza linijka jest równowazna z:
#
# row = next(matrix_row_iterator) - pobranie iteratora
# matrix_column_iterator = iter(row) - pobranie iteratora elementów wiersza
#
# wywołanie funkcji w funkcji sprawia, ze najpierw wywołuje się najbardziej zagniezdzona funkcja, potem funkcja ją obejmująca itd.

print(next(matrix_column_iterator), end=' ')
print(next(matrix_column_iterator), end='\n')

matrix_column_iterator = iter(next(matrix_row_iterator))
print(next(matrix_column_iterator), end=' ')
print(next(matrix_column_iterator), end='\n')

# ALTERNATYWNE ROZWIAZANIE
print()

matrix_row_iterator = matrix.__iter__()
matrix_column_iterator = matrix_row_iterator.__next__().__iter__()

print(matrix_column_iterator.__next__(), end=' ')
print(matrix_column_iterator.__next__(), end='\n')

matrix_column_iterator = matrix_row_iterator.__next__().__iter__()
print(matrix_column_iterator.__next__(), end=' ')
print(matrix_column_iterator.__next__(), end='\n')


# WYJAŚNIENIE
#
# A: Sekcja z pętlą for row in matrix:
#
# Jak napisano we wstępie, macierz to lista list. Musimy więc napisać pętlę przechodzącą po wierszach macierzy.
# Pętla ta jest pętlą zewnętrzną, for row in matrix:, która do zmiennej o nazwie row przypisuje
# kolejne elementy listy matrix:
# -element pierwszy to lista [1, 2]
# -element drugi to lista [3, 4]
#
# Zewnętrzna pętla przeiteruje więc wierszach macierzy - elementach, które są listami
#
# Następnie w wewnętrznej pętli iterujemy po kolumnach macierzy, tj. po elementach wiersza.
#
# Elementy pierwszego wiersza (pierwszej listy, lub pierwszego elementu listy matrix) to 1 oraz 2
# Elementy drugiego wiersza (drugiej listy, lub drugiego elementu listy matrix) to 3 oraz 4
# 
# Wewnętrzna pętla do przechodzenia wierszy będzie więc uzywała iteratora listy przypisanej do zmiennej o nazwie row,
# a więc np. jeśli pierwsza iteracja zewnętrznej pętli pobierze pierwszy element listy matrix, to do row zostanie przypisana lista [1, 2],
# wobec czego wewnętrzna pętla przeiteruje po elementach 1 oraz 2
#
# Kiedy nie będzie juz więcej elementów do przetworzenia w wewnętrznej pętli, pętla zakończy się,
# zostanie wywołana funkcja print() (przejście do kolejnej linii), po czym iterator zewnętrznej zwróći kolejny element listy matrix,
# jakim jest lista [3, 4] i do zmiennej o nazwie row zostanie przypisana taka lista
#
# Zostanie uruchomiona wewnętrzna pętla, tym razem przetwarzająca elementy z kolejnego, przypisanego do row wiersza, tj. [3, 4]
# Elementy tego wiersza zostaną wypisane, i gdy pętla nie będzie miała więcej elementów do przetworzenia, zostanie wywołana funkcja print()
#
# Zewnętrzna pętla równiez nie będzie miała juz więcej elementów do zwrócenia i zakończy swoje działanie
#
#
# B: Sekcja z manualnym iterowaniem
#
# Najpierw pobieramy iterator z listy matrix i przypisujemy go do zmiennej matrix_row_iterator. Ten iterator
# będzie słuzył nam do iterowania po elementach listy matrix, czyli po wierszach macierzy: [1, 2] oraz [3, 4]
#
# Następnie pobieramy iterator kolumn wiersza i przypisujemy go do zmiennej o nazwie matrix_column_iterator.
#
# Zwróc uwagę, ze aby pobrać iterator kolumn wiersza, najpierw musimy pobrać sam wiersz.
# Zapis: iter(next(matrix_row_iterator)) działa w następujący sposób:
# -najpierw wywoływana jest funkcja next(matrix_row_iterator), która zwraca kolejny element z iteratora matrix_row_iterator. Będzie to
#  pierwszy element listy matrix, a więc lista [1, 2]
# -następnie na zwróconym elemencie jest wywoływana funkcja iter, czyli funkcja pobierająca iterator dla listy [1, 2]
#
# Ponizszy zapis jest równowazny:
# matrix_row_iterator = iter(matrix) - pobiera iterator listy matrix
# row = next(matrix_row_iterator) - pobiera kolejny element z iterarora matrix_row_iterator, a więc element [1, 2]
# matrix_column_iterator = iter(row) - pobiera iterator listy [1, 2]
#
# Linie:
# print(next(matrix_column_iterator), end=' ')
# print(next(matrix_column_iterator), end='\n')
# wypisują elementy zwracane przez matrix_column_iterator, czyli najpierw 1, potem dwa, czego rezultatem jest wiersz:
# 1 2
#
# Następnie pobieramy kolejny element z iteratora matrix_row_iterator oraz iterator tego elementu:
# matrix_column_iterator = iter(next(matrix_row_iterator))
# 
# W powyzszym zapisie najpierw zostanie wywoałana funkcja next(matrix_row_iterator), która zwraca listę [3, 4] ,
# a potem funkcja iter wywołana na zwróconym elemencie zwróci iterator listy [3, 4]
#
# Dzięki temu do zmiennej o nazwie matrix_column_iterator zostanie przypisany iterator listy [3, 4]
#
# Wywołując metodę next na tym iteratorze dostaniemy kolejne elementy listy [3, 4], a dzięki metodzie print wypiszemy te elementy na ekran,
# czego rezultatem będzie widoczna na ekranie macierz w ponizszej postaci:
# 1 2
# 3 4
#
# Alternatywne rozwiązanie ma dokładnie taką samą mechanikę, ale funkcje next wbudowane w Pythona zostały zamienione na funkcje __next__
# dostępne w iteratorach, a wbudowana funkcja iter została zamieniona na funkcję __iter__ dostępną dla listy