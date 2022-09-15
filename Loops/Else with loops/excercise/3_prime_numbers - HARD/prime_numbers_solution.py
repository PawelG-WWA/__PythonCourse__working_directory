# ZADANIE 3
#
# Pobierz od uzytkownika ciąg znaków. Uzytkownik powinien podać liczby oddzielone spacją.
# 
# Jeśli w ciągu znaków podanym przez uytkownika nie wszystkie dane oddzielone spacjami sa liczbami,
# wypisz na ekranie komunikat 'Niepoprawne dane: podaj wyłącznie liczby oddzielone spacjami' i nie wykonuj reszty kodu
#
# W przeciwnym przypadku napisz w pętli kod, który będzie przetwarzał kazdą kolejną liczbę
#
# Dla kazdej kolejnej liczby sprawdź czy dana liczba jest liczbą pierwszą (dzielącą się przez 1 i przez samą siebie)
#
# Jeśli dana liczba jest liczbą pierwszą, wypisz na ekranie informację 'Liczba [liczba która jest liczbą pierwszą] jest liczbą pierwszą'
#
# Jeśli dana liczba nie jest liczbą pierwszą przejdź natychmiast do sprawdzania kolejnej liczby 
#
# Pomocne mogą być lekcje:
# -Łańcuchy znaków - konwersje
# -Łańcuchy znaków - operacje zaawansowane
# -Pobieranie danych od uzytkownika


user_data = input('Podaj liczby oddzielone spacjami: ')

user_data_list = user_data.split()

numbers = []

for x in user_data_list:
    if not x.isnumeric():
        print('Niepoprawne dane: podaj wyłącznie liczby oddzielone spacjami')
        break
    numbers.append(int(x))
else:
    for x in numbers:
        if x > 1:
            for divisor in range(2, x): # lepsze rozwiązanie: for divisor in range(2, int(x**0.5) + 1) - mniej dzielników do sprawdzenia
                if x % divisor == 0:
                    break
            else:
                print('Liczba %s jest liczbą pierwszą' % x)

# WYJAŚNIENIE
#
# Na początku pobieramy od uzytkownika listę liczb w postaci np.: 8 6 7 22 5 150 17
# 
# Następnie uzywamy funkcji split, która domyślnie rozdziela łańcuch znaków wg spacji,
# lista przechowywana pod zmienną user_data_list po wykonaniu user_data.split() wygląda następująco:
# user_data_list = [8, 6, 7, 22, 5, 150, 17]
#
# Następnie nazwie zmiennej numbers przypisuje pustą listę
#
# Pierwsza pętla przechodzi po wszystkich elementach listy user_data_list posiadającej dane (pojedyncze słowa) wprowdzone przez uzytkownika.
#
# W pętli sprawdza się, czy kazdy kolejny element listy jest liczbą. Jeśli któryś z nich nie jets liczbą, wypisywany jest na ekran
# napis 'Niepoprawne dane: podaj wyłącznie liczby oddzielone spacjami' i pętla natychmiast kończy swoje działanie,
# a blok else nie jest wykonywany.
#
# W przeciwnym przypadku, do listy numbers dodawana jest liczba wprowadzona przez uzytkownika
# 
# Jeśli wszystkie elementy listy user_data_list są liczbami, pętla nie kończy działania
# poprzez break i wykonywany jest kod w bloku else pętli for x in user_data_list
#
# Następnie nowa pętla pobiera kolejno elementy z listy numbers, czyli liczby
#
# Dla kazdej z tych liczb chcemy sprawdzić, czy posiada ona inne dzielniki niz 1 i samą siebie, dlatego uzywamy funkcji range, która zwraca
# zakres od x do y, bez y. Jeśli sprawdzamy dzielniki liczby 13, range(2, 13) wygeneruje następującą sekwencję:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
#
# Następnie warunek if x % divisor == 0 sprawdza, czy liczba x jest podzielna przez jakiś dzielnik z zakresu <2, 13)
#
# Jeśli jest, wywołujemy break i nie sprawdzamy dalej, poniewaz juz wiemy, ze dana liczba nie jest liczbą pierwszą,
# więc nie ma sensu sprawdzać pozostałych dzielników. Blok else dla pętli for divisor in range(2, x) nie zostanie wykonany
#
# Jeśli warunek if x % divisor == 0 nie zostanie spełniony dla danej liczby x (np. 7),
# to pętla zakończy się normalnie bez wywołania break i zostanie wykonany blok else dla pętli for divisor in range(2, x),
# i zostanie wypisany komunikat np. 'Liczba 7 jest liczbą pierwszą' dla x = 7