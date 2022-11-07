x = 10

def enclosing_function():
    x = 11

    def enclosed_function():
        x = x + 1
        print(x)

    enclosed_function()

enclosing_function()

# Wyjaśnienie
#
# Powyzszy przykład zwróci błąd: "UnboundLocalError: local variable 'x' referenced before assignment"
# (Uzycie lokalnej zmiennej x przed przypisaniem)
#
# W poprzednim pliku - 6_scopes_enclosing_example.py - widzielismy, ze funkcja zawarta w innej funkcji moze
# odnosić się do zmiennych stworzonych w funkcji zawierającej
#
# Jest to prawda, o ile nie chcemy zmienić wartości takiej zmiennej
#
# Wówczas Python 'myśli', ze próbujemy modyfikować zmienną lokalną, o czym informuje nas błąd
#
# Domyślnie, modyfikacja zmiennych z zakresu zawierającego (Enclosing) wewnątrz funkcji zagniezdzonych jest niedozwolona