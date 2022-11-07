x = 0

def add(number):
    x = 1
    x = x + number
    return x

print(add(3))
print(x)

# Opis
#
# 1. Tworzymy zmienną o nazwie x o zasięgu globalnym i przypisujemy jej wartość 0
# 2. Definiujemy funkcję o nazwie add, przyjmującą argument number
#    2a. Wewnątrz funkcji add tworzymy zmienną o nazwie x i przypisujemy do niej 1. Zmienna ta domyślnie posiada zakres lokalny.
#    2b. Nastepnie definiujemy operację dodawania
#    2c. Na końcu zwracamy wynik zapisany pod x
#
# 3. Wywołujemy funkcję add
#    3a. Python wyszukuje nazwę x w zakresie lokalnym i odnajduję zmienną o wartości x = 1
#    3b. Następnie dodaje do x wartość pod number (3)
#    3c. Na końcu zwracany jest wynik dodawania (4)
# 4. Wynik add(3) wypisywany jest na ekranie (4)
# 5. Na ekranie wypisywana jest wartość przechowywana pod globalnym x (0)
#
#
# Dodatkowe wyjaśnienie
#
# Jak napisano w części teoretycznej, zmienne zdefiniowane w def domyślnie posiadają zakres lokalny dla funkcji
# Oznacza to, ze x wewnątrz funkcji to inny x niz ten stworzony poza funkcją. Obydwie zmienne o nazwie x
# przechowują zupełnie inne wartości i są umieszczone w innych miejscach pamięci komputera
#
# Python przy wyowłaniu funkcji tworzy zmienną x = 1. Potem przeszukuje lokalną przestrzeń nazw i znajduje w niej x = 1
# To tego x o wartości równej 1 Python uzyje do wykonania działania oraz przypisania. To ten x zostanie zwrócony z funkcji add
#
# x stworzony poza funkcją to inny x, który nie zostanie zmodyfikowany.