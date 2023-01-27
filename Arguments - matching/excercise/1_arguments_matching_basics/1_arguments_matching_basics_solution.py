# ZADANIE 1
#
# Wyjaśnij, dlaczego wynik z dzielenia a / b w funkcji divide(a, b) w ponizszym przykładzie zwraca 2.0, a nie 0.5

def divide(a, b):
    return a / b


a = 1
b = 2

print(divide(b, a))

# ZAADNIE 1 - ODPOWIEDŹ
#
# Argumenty domyślnie przekazywane są pozycyjnie. Oznacza to, ze jeśli funkcja jest zdefiniowana następująco: divide(a, b),
# to argumenty będą przypisywane do zmiennych lokalnych funkcji w kolejności od lewej do prawej.
#
# Wywołanie funkcji divide poprzez przekazanie do niej zmiennych a i b z zakresu globalnego w kolejności b, a: divide(b, a) jak wyzej sprawi,
# ze do zmiennej a w funkcji divide zostanie przypisana zmienna b z zakresu globalnego, a do zmiennej b z lokalnego zakresu funkcji zostanie przypisana zmienna a
# z zakresu globalnego.
#
# Dlatego więc a / b w funkcji to tak naprawdę działanie 2 / 1, stąd wynik wynosi 2.0.

# ZADANIE 2
#
# Popraw ponizszy kod w taki sposób, aby wynikiem progrmau było:
# 1
# 2
# 3
#
# ale nie dokonując zmian wewnątrz funkcji some_function, Dlaczego nalezy dokonać zmiany?

print()
def some_function(first, second, third):
    print(first)
    print(second)
    print(third)


print(some_function(1, 2, 3))

# ZADANIE 2 - ODPOWIEDŹ
#
# Mamy do czynienia z podobną sytuacją jak w zadaniu pierwszym.
#
# Argumenty przekazywane są domyślnie pozycyjnie. Przekazanie 3, 1 oraz dwa nie sprawi, ze first, second i third zostaną w magiczny sposób
# utworzone z wartościami, odpowiednio, 1, 2 i 3. Kolejność przekazania argumentów do funkcji ma znaczenie i powoduje, ze parametry funkcji
# wymienione od lewej do prawej będą posiadały wartości równiez przekazane do funkcji od lewej do prawej.

