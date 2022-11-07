# ZADANIE
#
# Mamy dane dwa konta bankowe: account_a oraz account_b, które przechowują środki wyrazone w liczbie całkowitej
#
# Napisz funkcję o nazwie is_transfer_possible, która sprawdzi, czy na koncie, z którego
# pobierzemy kwotę jest wystarczająca ilość środków. Jeśli nie istnieje wystarczająca ilość
# środków, wypisz komunikat "na koncie brakuje środków" i zakończ wykonywanie programu. Jeśli jest wystarczająca
# ilość środków
#
# Napisz funkcję o nazwie transfer umozliwiającą przelanie pieniędzy z jedngo konta na drugie
# Funkcja transfer powinna przyjmowac trzy argumenty:
# -kwotę przelewu
# -konto, z którego nalezy pobrac kwotę
# -konto, na które nalezy wpłacić kwotę
# Ponadto funkcja transfer powinna zwracać krotkę z nowymi wartościami kont. Wartości te powinny zostać przypisane do account_a oraz account_b
#
# Na końcu wypisz stan obydwu kont
#
# Pamiętaj, ze:
# -program w Pythonie wykonuje się linia po linii, od góry do dołu, kolejność definicji funkcji ma więc znaczenie
# -funkcje mozesz (a czasami nawet powinieneś!) wywoływać wewnątrz innych funkcji
# - unkcje zwracają wartości poprzez uzycie return. Return mozna uzyć równiez do wyjścia z funkcji
#   w celu przerwania jej wykonania

account_a = 100
account_b = 50