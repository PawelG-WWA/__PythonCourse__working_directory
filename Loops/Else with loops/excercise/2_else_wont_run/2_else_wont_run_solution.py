# ZADANIE 2
#
# Podana jest lista my_list = ['apple', 'potato', 'tomato']
# Napisz pętlę, która będzie pobierała kolejno wszystkie elementy listy i wypisze kazdy z nich, oprócz elementu 'potato' (uzyj continue)
# Zakończ natychmiast wykonanie pętli, jeśli wartość pod x będzie równa 'tomato'
# Dopisz blok else dla pętli który będzie wypisywał napis 'No break' i sprawdź, czy napis zostanie wypisany na ekran

my_list = ['apple', 'potato', 'tomato']

for x in my_list:
    if x == 'potato':
        continue
    if x == 'tomato':
        break
    print(x)
else:
    print('No break')

# Wyjaśnienie:
#
# Kod zawiera instrukcję break, a więc blok else pętli nie wykonuje się.
#
# Instrukcja continue nie uniemozliwia wykonania bloku else, ale pętla natrafia na instrukcję break, więc blok else nie wykona się
#
# Wynik:
#
# apple