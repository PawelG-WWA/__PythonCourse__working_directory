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