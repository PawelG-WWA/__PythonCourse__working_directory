# ZADANIE 1
#
# Wyjaśnij, dlaczego wynik z dzielenia a / b w funkcji divide(a, b) w ponizszym przykładzie zwraca 2.0, a nie 0.5

def divide(a, b):
    return a / b


a = 1
b = 2

print(divide(b, a))


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


print(some_function(3, 1, 2))

