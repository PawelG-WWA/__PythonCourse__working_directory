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
# -funkcje zwracają wartości poprzez uzycie return. Return mozna uzyć równiez do wyjścia z funkcji
#  w celu przerwania jej wykonania

def transfer(account_from, account_to, amount):
    if is_transfer_possible(account_from, amount):
        account_from -= amount
        account_to += amount
    
    return (account_from, account_to)

def is_transfer_possible(account, amount):
    if amount > account:
        print('Na koncie brakuje środków')
        return False
    return True

account_a = 100
account_b = 50

(account_a, account_b) = transfer(account_a, account_b, 1000)

print(account_a)
print(account_b)
