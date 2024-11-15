list_of_actions = [
    lambda x, y: print('Add %s + %s = %s' % (x, y, x + y)),
    lambda x, y: print('Multiply %s * %s = %s' % (x, y, x * y)),
    lambda x, y: print('Divide %s / %s = %s' % (x, y, x / y)),
    lambda x, y: print('Subtract %s - %s = %s' % (x, y, x - y))
]

for action in list_of_actions:
    action(3, 4)


# WYJAŚNIENIE
#
# Na początku definiujemy listę działań list_of_actions, którą będziemy wykonywać.
#
# Kazde z działań jest oddzielnym wyrazeniem lambda. Oznacza to, ze wyrazenia lambda, a tak naprawdę obiekty
# typu function są elementami listy
#
# W pętli, przechodząc po elementach tej listy, wywoływane są na tych samych argumentach - 3 oraz 4 - kolejne działania.
#
# Pętla w kazdej iteracji pobiera kolejny element listy i przypisuje go do zmiennej action. Z kazdym przejściem
# pętli nazwa action posiada referencję do innego obiektu - innej funkcji lambda.
#
# Nazwa action w pętli staje się więc wywoływalną funkcją, do której mozna przekazać argumenty.
#
# Jest to jeden z najbardziej praktycznych przykładów zastosowania wyrazenia lambda
#
# Aby osiągnąć podobny efekt - wykonać kilka prostych, pojedynczych funkcji na tym samym zestawie argumentów, musielibyśmy
# bez wyrazenia lambda napisać znacznie więcej kodu. Alternatywne rozwiązanie wyglądałoby następująco:
def add(x, y):
    print('Add %s + %s = %s' % (x, y, x + y))


def multiply(x, y):
    print('Multiply %s * %s = %s' % (x, y, x * y))


def divide(x, y):
    print('Divide %s / %s = %s' % (x, y, x / y))


def subtract(x, y):
    print('Subtract %s - %s = %s' % (x, y, x - y))


list_of_actions = [
    add,
    multiply,
    divide,
    subtract
]

for action in list_of_actions:
    action(3, 4)


# Jak wspomniano wcześniej, kazde wykorzystanie wyrazenia lambda jest mozliwe do zastąpienia bardzo prostą funkcją
# stworzoną za pomocą def. Jeśli są to operacje bardzo proste, pojedyncze, wywoływane raz w programie, który piszesz,
# warto rozwazyc uzycie wyrazenia lambda. Bezspotnie pierwszy przykład stworzony za ich pomocą jest
# znacznie bardziej zwięzły i czytely, dający się ogarnąć jednym rzutem oka.