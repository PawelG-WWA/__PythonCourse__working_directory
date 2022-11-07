# ZADANIE
#
# Znajdź w ponizszym kodzie błąd i napraw go.
#
# W funkcji add nie zamieniaj linii x = x + y + z. Nie wprowadzaj za x zadnej nowej zmiennej.
#
# Oczekiwany wynik: x + y = z = 10 + 2 + 15 = 27

x = 10
y = 2
z = 15

def add():
    x = x + y + z
    return x

print(add())