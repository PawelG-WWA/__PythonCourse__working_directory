import os #import modułu os do uzycia poprawnych ściezek do pliku

# otwarcie pliku z folderu Assets
# niezaleznie od miejsca, w którym mamy zapisane repozytorium kodu

file_data = open(os.path.realpath('Loops/Else with loops/Assets/example_log_file.txt'))
#file_data = open(os.path.realpath('Loops/Else with loops/Assets/example_log_file_no_errors.txt')) 

is_error = False

for line in file_data: # dane pliku są iterowalne, jak lista, odczytujemy linię po linii
    if 'error' in line.lower():
        is_error = True
        break
else:
    print('no errors')

file_data.close()

if is_error:
    print(line)

# Przebieg algorytmu (plik example_log_file.txt):
#
# 1. Otwarcie pliku file.txt z folderu Assets w trynie do odczytu (tryb domyślny)
# 2. Przypisanie do nazwy is_error wartości False
# 3. Weź linię z pliku file_data i przypisz wartość tej linii (łańcuch znaków) do nazwy line
# 4. Sprawdź, czy napis error znajduje się w wartości przechowywanej pod nazwą line
# ... powtarzaj kroki 3, 4
# 5. Wartość przechowywana pod nazwą line posiada napis 'error'
# 6. Przypisz do nazwy is_error wartość True
# 7. Wykonaj instrukcję break, natychmiast przerywając pętlę
# 8. Zakończ pracę z plikiem wywołując funkcję clse(), zwalniając tym samym zasoby związane z plikiem
# 9. Sprawdź, czy zmienna is_error posiada wartość True
# 10. Tak, zmienna is_error posiada wartość True
# 11. Wypisz na ekran wartość przechowywaną pod nazwą line (informację o błędzie z pliku)
#
# Wynik algorytmu:
#
# ERROR - coś poszło nie tak, kod błędu: 123, godzina wystąpienia: 11:12:59.786


# Przebieg algorytmu (plik example_log_file_no_errors.txt) - nalezy zakomentować linię 6 poprzez poprzedzenie jej znakiem # i odkomentować linię 7 poprzez usunięcie znaku #
#
# 1. Otwarcie pliku file.txt z folderu Assets w trynie do odczytu (tryb domyślny)
# 2. Przypisanie do nazwy is_error wartości False
# 3. Weź linię z pliku file_data i przypisz wartość tej linii (łańcuch znaków) do nazwy line
# 4. Sprawdź, czy napis error znajduje się w wartości przechowywanej pod nazwą line
# ... powtarzaj kroki 3, 4 az do przetworzenia całości pliku (wszystkich linii)
# 5. Wypisz na ekran napis 'no errors' z bloku else pętli for
# 6. Zakończ pracę z plikiem wywołując funkcję clse(), zwalniając tym samym zasoby związane z plikiem
# 7. Sprawdź, czy zmienna is_error posiada wartość True
# 8. Nie, zmienna is_error posiada wartość False
#
# Wynik algorytmu:
#
# no errors