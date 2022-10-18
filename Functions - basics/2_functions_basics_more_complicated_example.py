import os # import modułu os aby mieć dostęp do funkcji ułatwiających odczyt pliku z bieącego katalogu

# Tym razem nie opiszemy przebiegu algorytmu, poniewaz jest zbyt skomplikowany, aby zamieścić zwięzły opis
#
# W funkcjach zauwazysz, ze na samym początku występuje ciąg znaków poprzedzony i zakończony potrójnym cudzysłowem
#
# Jest to tak zwany docstring - łańcuch znaków słuacy do dokumentowania funkcji, a takze innych komponentów, które
# poznasz za jakiś czas. Doscstring nie ma wpływu na działanie funkcji, jest wyłacznie jej opisem, który
# wyjaśnia co robi funkcja, jakie przyjmuje argumenty i co zwraca.
#
# Dzięki zamieszczeniu dokumentacji funkcji w ten sposób, ty lub inny programista moze uzyc wbudowanej funkcji help,
# aby wyświetlić dokumentację/opis twojej metody. Wbudowaną funkcję help mozesz uzyc na dowolnej funkcji wbuowanej
#
# Spróbuj wywołać na przykład help(print)
#
# Umieszczenie docstringa nie jest wymagane - umieszczam je w celach informacyjnych zamiast stosowanego do tej pory
# opisu przebiegu algorytmu.
#
# Myślę tez, ze na tym etapie nauki nie ma juz potrzeby opisywania przebiegu pętli czy warunków logicznych

def read_file_data():
    """
    Funkcja czyta plik example_log.txt
    Return:
        Dane zawarte w pliku example_log.txt
    """
    file_handler = open(os.path.realpath('Functions - basics/Assets/example_log.txt'), 'r')
    file_data = file_handler.readlines()
    file_handler.close()
    return file_data

def write_data_to_file(data):
    """
    Funkcja zapisuje dane do pliku example_log
    Argumenty:
        data - dane, które mają być zapisane w pliku
    """
    file_handler = open(os.path.realpath('Functions - basics/Assets/example_log.txt'), 'a')
    file_handler.write(data)
    file_handler.close()

def find_in_file_data(text, file_data):
    """
    Funkcja przeszukuje dane w pliku linia po linii w celu odszukania wskazanego tekstu
    Argumenty:
        text: fraza do znalezienia w danych z pliku
        file_data: dane odczytanego pliku
    """
    for line in file_data:
        if text in line:
            ('FOUND: %s' % line)
            break
    else:
        print('%s has not been found' % text)


# Odczytujemy dane z pliku i zwracane dane przypisujemy do zmiennej o nazwie file_data
file_data = read_file_data()

# Sprawdzamy czy w danych z pliku przypisanych do zmiennej o nazwie file_data
# znajduje się napis 'ERROR'
find_in_file_data('ERROR', file_data)

# Do pliku zapisujemy - na przykład w wyniku jakichś operacji - kolejne logi
write_data_to_file('LOG: 2022-10-10 12:34:00.123 - Information - Successful request\n')
write_data_to_file('LOG: 2022-10-10 12:34:00.123 - Information - Successful request\n')
write_data_to_file('LOG: 2022-10-10 12:34:00.123 - Information - Successful request\n')

# Ponownie odczytujemy dane z pliku i przypisujemy je do zmiennej file_data
file_data = read_file_data()

# Ponownie poszukujemy napisu 'ERROR' w danych pliku
find_in_file_data('ERROR', file_data)

# Ponownie zapisujemy jakieś logi do pliku
write_data_to_file('LOG: 2022-10-10 12:34:00.123 - ERROR - Application error occured!!!\n')

# Ponownie odczytujemy dane pliku i przypisujemy je do zmiennej o nazwie file_data
file_data = read_file_data()

# Ponownie sprawdzamy, czy w danych odczytanych z pliku znajduje się napis 'ERROR'
find_in_file_data('ERROR', file_data)

# Jeśli nie zmieniałeś danych w pliku przed uruchomieniem programu, jego wykonanie powinno zakończyć się wynikiem:
# ERROR has not been found
# ERROR has not been found
# FOUND: LOG: 2022-10-10 12:34:00.123 - ERROR - Application error occured!!!

# Dodatkowe wyjaśnienie:
#
# Spójrz, jak wiele razy skorzystaliśmy z raz napisanych funkcji. Gdyby nie one, kod, który się w nich zawiera
# musiałby być powtórzony w kazdym miejscu, w którym występują wywołania. Oznacza to, ze na przykład wszędzie, gdzie
# występuje wywołanie funkcji write_data_to_file musiałyby wystąpić instrukcje:
# file_handler = open(os.path.realpath('Functions - basics/Assets/example_log.txt'), 'a')
# file_handler.write(data)
# file_handler.close()
#
# Podowałoby to znaczne wydłuzenie kodu programu, który byłby trudniejszy do zrozumienia a takze modyfikacji
#
# Jeśli zechcemy wprowadzić zmianę np w sposobie zapisu danych do pliku, wystarczy zrobić to tylko
# w jednym miejscu - w zakresie funkcji write_data_to_file.
#
# Załózmy, ze po jakimś czasie stwierdzimy, ze nie chcemy zapisywać do pliku pustych linii. Musielibyśmy dodać sprawdzenie,
# czy napis data nie jest pusty. Jeśli nie byłby pusty, dodalibyśmy wpis do pliku, jeśli byłby pusty, wypisalibyśmy na ekran
# napis "nie mozna dodać pustej linii do pliku". Funkcja write_data_to_file przybrałaby wówczas następującą postać:

# def write_data_to_file(data):
#    if data != "":
#       file_handler = open(os.path.realpath('Functions - basics/Assets/example_log.txt'), 'a')
#       file_handler.write(data)
#       file_handler.close()
#    else:
#       print('nie mozna dodać pustej linii do pliku')
#
# Po tej zmianie w ciele funkcji nie musimy juz nic robic - kazde wywołanie skorzysta juz z uaktualnionej wersji tej funkcji
#
# Jeśli wielokrotnie wykorzystywany kod nie byłby funkcją, ale powielonym metodą kopiuj-wklej kodem,
# musielibyśmy powyzszą zmianę wprowadzić w kazdym miejscu, do którego kopia kodu została wklejona!
#
# Po dokonaniu takiej zmiany kazde wywołanie tej funkcji korzystałoby juz z nowej wersji funkcji.
#
# Funkcje więc minimalizują ilość zmian, jakie trzeba byłoby wprowadzać w kod bez nich - gdyby nie one,
# zmiany trzeba byłoby wprowadzić w kazdym miejscu, w którym kod słuzący np do zapisu danych zostałby powtórzony
#
# Wraz z powtarzaniem kodu rośnie ryzyko wystąpienia błędów, a co za tym idzie, czasu na ich znajdowanie i naprawianie
#
# Funkcje minimalizują to ryzyko.