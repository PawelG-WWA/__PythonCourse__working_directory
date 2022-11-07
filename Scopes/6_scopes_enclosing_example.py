x = 10

def enclosing_function():
    x = 11

    def enclosed_function():
        print(x)
    
    enclosed_function()


enclosing_function()

# Wyjaśnienie
#
# Na początku tworzymy zmienną o nazwie x przechowującą wartość 10
#
# Następnie definiujemy funkcję enclosing_function, w której:
#   -tworzymy zmienną lokalną x dla tej funkcji o wartości 11 - x = 11
#   -definiujemy funkcję enclosed_function, w której:
#       -wypisujemy x
#   -następnie w funkcji enclosing_function() wywołujemy zdefiniowaną w niej funkcję enclosed_function()
#
# Na końcu wywołujemy funkcję enclosing_function()
#
# Wynikiem powyzszych czynności jest wypisanie na ekranie liczby 11
#
# Tak jak opisano w części teoretycznej, Python przeszukuje zasięgi w następującej kolejności:
# 1. Zasięg lokalny (Local)
# 2. Zasięg zawierający (Enclosing)
# 3. Zasieg globalny (Global)
# 4. Zasięg wbudowany (Built-in)
#
# W powyzszym przypadku mamy do czynienia z zasięgiem nr 2, czyli zawierającym (Enclosing)
#
# Polega to na tym, ze Python przeszukuje w górę wszystkie lokalne zasięgi funkcji, które zawierają wewnętrzną funkcję wywoływaną
#
# W powyzszym przykładzie wewnętrzną funkcją wywoływaną jest enclosed_function(), a funkcją zawierającą enclosing_function()
#
# Wywołując enclosed_function w enclosing_function Python najpierw będzie szukał x w enclosed_function - nie znajdzie go, a więc
# poszukiwania będzie kontynuował w enclosing_function, gdzie x faktycznie się znajduje i jest to pierwsze x, która Python napotka
#
# x dostępne w enclosed_function pochodzi więc z lokalnego zasięgu enclosing_function i jest równe 11, a nie 10, tak jak x w zasięgu globalnym