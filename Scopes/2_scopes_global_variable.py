x = 0

def add(number):
    z = x + number
    return z

print(add(3))
print(x)

# Opis
#
# 1. Tworzymy zmienną o nazwie x o zasięgu globalnym i przypisujemy jej wartość 0
# 2. Definiujemy funkcję o nazwie add, przyjmującą argument number
#    2a. Wewnątrz funkcji add tworzymy zmienną o nazwie z i przypisujemy do niej wynik działania. Zmienna ta domyślnie posiada zakres lokalny.
#    2c. Na końcu zwracamy wynik zapisany pod z
#
# 3. Wywołujemy funkcję add
#    3a. Python stworzy nazwę z w zakresie lokalnym i przypisze do tek zmiennej wynik dodawnia x + number.
#        Pamiętajmy, ze przypisanie wartosci do zmiennej jest wymagane przed pierwszym uzyciem zmiennej
#    3b. Zanim przypisanie nastąpi, Python przeszuka przestrzenie nazw, aby odnaleźć zmienną x. Zrobi to w następującej kolejności:
#        -najpierw zostanie przeszukany zakres lokalny funkcji add. W zakresie tym nie istnieje jednak nazwa x
#        -następnie przeszukany zostanie zakre zawierający. Funkja add nie jest zawarta ani nie zawiera zadnej innej funkcji,
#         ten krok nie ma zatem zastosowania
#        -potem Python przeszuka zakres globalny. Zmienna o nazwie x znajduje się w zakresie globalnym, a jej wartość wynosi 0
#    3c. W podobny sposób zostanie odnaleziona zmienna number, do której została przypisana wartość 3 w momencie wywołania funkcji
#    3d. Zmienna o nazwie z zostanie teraz utworzona i będzie przechowywała wartość dodawania x + number, gdzie x jest zmienną globalną x = 0,
#        a number zmienną lokalną funkcji number = 3
#    3e. Następnie zwrócony zostanie wynik dodawania przechowywany pod z (3)
# 4. Wynik add(3) wypisywany jest na ekranie (3)
# 5. Na ekranie wypisywana jest wartość przechowywana pod globalnym x (0)