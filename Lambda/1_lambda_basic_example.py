k = 5

add = lambda x, y: x + y + k

print(add(1, 2))

# WYJAŚNIENIE:
#
# Na początku tworzymy zmienną k w zakresie globalnym, k = 5
#
# Następnie uzywamy wyrazenia lambda:
# lambda x, y: x + y + k
#
# Wyrazenie tworzy funkcję przyjmującą dwa argumenty - x oraz y - a jej ciało zwraca sumę zmiennych x, y i k
#
# Ciało wyrazenia lambda znajduje się po dwukropku poprzedzonym przez argumenty
#
# Funkcję lambda wywołuje się jak zwykłą funkcję. Nazwa funkcji jest przypisana do nazwy występującej po lewej stronie
# operatora przypisania. Funkcję lambda wywołujemy wiec uzywając tej nazwy i przekazując argumenty.
#
# Pamiętajmy, ze w funkcjach lambda obowiązują nas te same zasady co w całym języku Python. Na przyklad to, ze domyślnie
# operator dodawania musi być zdefiniowany dla operandów - wywołanie add(1, 'a') spowoduje błąd TypeError - Python
# nie potrafi bowiem dodać do siebie liczby (int) i ciągu znaków (string)