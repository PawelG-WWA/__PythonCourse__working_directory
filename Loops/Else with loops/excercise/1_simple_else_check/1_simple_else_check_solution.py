# ZADANIE 1
#
# Podana jest lista my_list = ['apple', 'potato', 'tomato']
# Napisz pętlę, która będzie pobierała kolejno wszystkie elementy listy i wypisze kazdy z nich, oprócz elementu 'potato' (uzyj continue)
# Następnie, jeśli pętla zakończy się bez break, wypisz na ekran napis 'No break' (w bloku else)

my_list = ['apple', 'potato', 'tomato']

for x in my_list:
    if x == 'potato':
        continue
    print(x)
else:
    print('No break')

# Wyjaśnienie:
#
# Kod nie zawiera instrukcji break, a więc blok else pętli wykonuje się.
#
# Instrukcja continue nie uniemozliwia wykonania bloku else
#
# Wynik:
# apple
# tomato
# No break