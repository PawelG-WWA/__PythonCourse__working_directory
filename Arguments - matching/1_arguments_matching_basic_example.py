def a(x, y):
    return x - y

x = 1
y = 2

print(a(y, x))

# WYJAŚNIENIE
#
# Na początku definiujemy funkcję a
#
# Następnie tworzymy zmienne x oraz y, którym przypisujemy kolejny 1 oraz 2
#
# Do funkcji a przekazujemy jednak zmienne w kolejności y oraz x
#
# Wypisajuemy na ekranie wynik zwracany przez funkcję a.
#
# Zwróć uwagę, ze do a przekazaliśmy najpierw y = 2, a potem x = 1. Nie ma znaczenia, ze argumenty x oraz y
# w funkcji a podane są w odwrotnej kolejności. Do x w a zostanie przypisane globalne y, a do y w a zostanie
# przypisane globalne x
#
# W funkcji a x = 2, a y = 1.
#
# Dlaetgo wynik końcowy wypisany na ekranie wynosi dokładnie 1