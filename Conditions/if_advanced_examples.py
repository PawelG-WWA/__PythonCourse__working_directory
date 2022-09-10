# Zalecam najpierw uruchomić skrypt, a potem analizować jego wyniki, poniewa długość instrukcji print
# sprawia, ze skrypt jest trudny do analizy - nie tylko dla początkujących, ale równiez dla bardzo
# zaawansowanych programistów. Najwazniejsze w skrypcie są warunki logiczne występujące po
# instrukcjach if. Spróbuj więc uruchomić skrypt, a następnie zastanowić się, dlaczego daje takie
# a nie inne wyniki, zanim przeczytasz komentarze wyjaśniające

a = 0
b = 1
text = 'Something in the way she moves...'

#TEST 1
print('\n')

if a == 0 or b == 2:
    print('TEST 1 - wartości wyrazeń:\n\ta == 0: %s\n\tb == 2: %s\n\ta == 0 or b == 2: %s' % (a == 0, b == 2, a== 0 or b == 2))
    print('\ta jest równe 0 lub b jest równe 1')

    # TEST 1 - wyjaśnienie
    #
    # operator or zwraca wartosc True (prawdę), jesli ktorekolwiek z wyrazeń po obydwu stronach operatora
    # jest prawdziwe. a == 0 jest Prawdą (True), b == 2 jest Fałszem (False), a więc całe wyrazenie zwraca Prawdą (True)
    # 
    # Tabelka prezentuje wszystkie mozliwe kombinacje wynikow operatora or
    #
    #|---------------------------------------|
    #| lewa strona | prawa strona | wynik or |
    #|-------------|--------------|----------|
    #| Prawda      | Prawda       | Prawda   |
    #|-------------|--------------|----------|
    #| Fałsz       | Prawda       | Prawda   |
    #|-------------|--------------|----------|
    #| Prawda      | Fałsz        | Fałsz    |
    #|-------------|--------------|----------|
    #| Fałsz       | Fałsz        | Fałsz    |
    #----------------------------------------|

#TEST 2
print('\n')

if a == 2 or b == 1:
    print('TEST 2 - wartości wyrazeń:\n\ta == 2: %s\n\tb == 1: %s\n\ta == 2 or b == 1: %s' % (a == 2, b == 1, a == 2 or b == 1))
    print('\ta jest równe 0 lub b jest równe 1')

    # TEST 2 - wyjaśnienie
    #
    # operator or zwraca wartosc True (prawdę), jesli ktorekolwiek z wyrazeń po obydwu stronach operatora
    # jest prawdziwe. a == 2 jest Fałszem (False), b == 1 jest Prawdą (True), a więc całe wyrazenie zwraca Prawdą (True)


#TEST 3
print('\n')

print('TEST 3 - wartości wyrazeń:\n\ta == 2: %s\n\tb == 1: %s\n\ta == 2 and b == 1: %s' % (a == 2, b == 1, a == 2 and b == 1))
print('\tOperator "and" zwraca True wyłącznie, jeśli obydwie strony wyrazenia - lewa i prawa, są zwracają True ')


    # TEST 3 - wyjaśnienie
    #
    # Operator "and" zwraca True wyłącznie wtedy, kiedy wyrazenia po obydwu stronach operatora zwracają Prawdę (True)
    # a == 2 jest Fałszem (False), b == 1 jest Prawdą (True), a więc całe wyrazenie jest Fałszem (False)
    #
    # Tabelka prezentuje wszystkie mozliwe kombinacje wynikow operatora and
    #
    #|----------------------------------------|
    #| lewa strona | prawa strona | wynik and |
    #|-------------|--------------|-----------|
    #| Prawda      | Prawda       | Prawda    |
    #|-------------|--------------|-----------|
    #| Fałsz       | Prawda       | Fałsz     |
    #|-------------|--------------|-----------|
    #| Prawda      | Fałsz        | Fałsz     |
    #|-------------|--------------|-----------|
    #| Fałsz       | Fałsz        | Fałsz     |
    #-----------------------------------------|

#TEST 4
print('\n')

if (a == 2 or b == 1) and 'in the way' in text:
    print('TEST 4 - wartości wyrazeń:\n\ta == 2: %s\n\tb == 1: %s\n\ta == 2 or b == 1: %s\n\t"in the way" in text: %s\n\t(a == 2 or b == 1) and "in the way" in text: %s' 
        % (a == 2, b == 1, a == 2 and b == 1, (a == 2 or b == 1) and 'in the way' in text, (a == 2 or b == 1) and 'in the way' in text))
    print('\tCałe wyrazenie zwraca True, poniewaz część wyrazenia or po lewej stronie "and" jets prawdziwa i warunek po prawej "and" stronie jest prawdziwy')

    #TEST 4 - wyjaśnienie
    #
    # Operator or zwraca Prawdę (True), jeśli którekolwiek z wyrazeń po obydwu stronach operatora jest prawdziwe
    # Wyrazenie (a == 2 or b == 1) zwraca wiec Prawdę (True)
    #
    # Operator in zwraca Prawdę (True), jeśli zadany ciąg znaków znajduje się w wartości umieszczonej pod podaną nazwą
    # Wyrazenie "in the way" in text - zwraca True
    #
    # Operator or zwrocil Prawdę (True), operator in równiez zwrócił Prawdę (True)
    #
    # Operator and zwraca Prawdę (True) jeśli wyrazenia po obydwu stronach operatora są prawdziwe
    # Jak wykazano powyzej, obydwa wyrazenia po obydwu stronach operatora and są prawdziwe
    # 
    # Operator and zwraca więc Prawdę (True)

#TEST 5 - co wypisze na ekran ponizszy kod?
print('\nTEST 5')

if a == 2 or b == 1:
    print('a == 2 lub b == 1')

    if 'Something' in text:
        print('Napis "Something" znajduje się w wartości zmiennej text')
    else:
        print('Napis "Somehting nie znajduje się w wartości zmmiennej tekst"')

    # TEST 5 - wyjaśnienie
    #
    # Operator or zwraca Prawdę (True), jeśli którekolwiek z wyrazeń po obydwu stronach operatora zwraca Prawdę (True)
    # a == 2 zwraca Fałsz (False), b == 1 zwraca Prawdę (True)
    # a == 2 or b == 1 zwraca więc Prawdę (True)
    #
    # Na ekranie wypisywany jest napis "a == 2 lub b == 1"
    #
    # Następnie w tym bloku if występuj einny blok if, sprawdzający, czy napis "Somehting" znajduje się w wartości zapisanej pod nazwą text
    # Tak, napis znajduje się w tej wartości i wypisany na ekran zostaje napis 'Napis "Something" znajduje się w wartości zmiennej text'


#TEST 6 - co wypisze na ekran ponizszy kod?
list_of_attendees = ['John', 'Paul', 'George', 'Richard']
zero = 0

print('\nTEST 6')

if list_of_attendees:
    print(list_of_attendees)

    if text:
        print(text)

        if not zero:
            print('zero nie jest prawdą')

    # TEST 6 - wyjaśnienie
    #
    # Test prawdziwości dla list zwraca Prawdę (True), jeśli lista nie jest pusta (rownowaznik: len(list_of_attendees) != 0)
    #
    # Test prawdziwości dla łańuchów znaków zwraca Prawdę (True), jeśli łańuch znaków nie jest pusty (równowaznik: len(text) != 0 lub text != '' )
    #
    # Liczby są Prawdą (True), jeśli nie są zerem
    #
    # Pierwsza instrukcja if sprawdza prawdziwość wartości pod nazwą list_of_attendees. Lista nie jest pusta, więc zwracana jest Prawda
    # i wypisywane są na ekran elementy listy
    # 
    # Druga, zagniezdzona w pierwszej instrukcja if wykona się tylko wtedy, jeśli pierwszy warunek był prawdą. Był prawdą, więc
    # po wypisaniu elementów listy przechodzimy do analizy drugiego testu prawdziwości
    #
    # text jest prawdą, poniewa nie jest pustym ciągiem znaków. Test zwraca więc prawdę (True) i zezwala na wejście do zagniezdzonego bloku if
    # i wykonania kodu w jego zakresie. Wypisywana jest wartość zapisana pod nazwą text, tj. "Something in the way she moves..."
    #
    # Kazda liczba jest prawdą, jeśli nie jest zerem. Zero jest Fałszem (True).
    # Tutaj jednak mamy do czynienia z zaprzeczeniem fałszu. Test sprawdza, czy prawdziwe jest stwierdzenie, ze nie-zero jest prawdą
    # Tak nie-zero jest prawdą (zaprzeczenie Fałszu, czyli zera). Test zwraca Prawdę i zezwala na wykonanie bloku kodu w zakresie trzeciego
    # ifa
    # 
    # Operator not słuy do sprawdzania zaprzeczeń, np aby sprawdzić, czy prawdą jest, ze jakis tekst nie znajduje się
    # w wartości pod nazwą text, nalezy uzyc operatora not następująco:
    #
    # if "abc" not in text: - to wyrazenie zwroci Prawdę, poniewaz Prawdą jest, ze ciąg znaków abc nie znajduje się w tekście
    # "Something in the way she moves..."

print('\n')
