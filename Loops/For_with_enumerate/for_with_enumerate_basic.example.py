people = ['Anna', 'James', 'Roman']

for (index, person) in enumerate(people):
    print('%s = %s' % (person, people[index]))

# Przebieg algorytmu:
#
# 1. przypisz zmiennej o nazwie people listę ['Anna', 'James', 'Roman']
# 2. Dla listy przechowywanej pod zmienną people, zwróć kolejną krotkę (index, person) - (index, person) = (0, 'Anna')
# 3. Wypisz na ekranie Anna = Anna - zmiennej person przypisana zostaje wartość z listy 'Anna', a zmiennej index numer indeksu
# 4. Dla listy przechowywanej pod zmienną people, zwróć kolejną krotkę (index, person) - (index, person) = (1, 'James')
# 5. Wypisz na ekranie James = James - zmiennej person przypisana zostaje wartość z listy 'James', a zmiennej index numer indeksu
# 6. Dla listy przechowywanej pod zmienną people, zwróć kolejną krotkę (index, person) - (index, person) = (2, 'Roman')
# 7. Wypisz na ekranie Roman = Roman - zmiennej person przypisana zostaje wartość z listy 'Roman', a zmiennej index numer indeksu
# 8. Zakończ działanie programu

# Dodatkowe wyjaśnienie
#
# enumerate(people) przy kadej iteracji zwraca krotkę w postaci pary (indeks, element z kolekcji)
#
# w nagłówku pętli for uzyliśmy więc równiez krotki (index, person), zamiast pojedynczego obiektu jak w dotychczasowych przekładach
# 
# dzięki temu w kazdej iteracji pętla for przypisze wartości zwracane przez enumerate do wskazanych przez nas nazw index oraz person
#
# to są oczywiście tylko nazwy, a liczy się kolejność. Jeśli zamienimy kolejność nazw w naszej krotce, do której przypiszemy wynik
# kazdego kolejnego pobrania krotki zwracanej przez enumerate(people) w taki sposób: (person, index), to pod nazwą person będziemy
# mieli numer indeksu, a pod nazwą index znajdzie się element listy, np. 'Anna'. Warto nadawać więc zmiennym sensowne nazwy
#
# Dla przypomnienia, jeśli mamy krotkę np (0, 'Anna') i wykonamy następujące przypisanie:
# (x, y) = (0, 'Anna')
#
# to interpreter Pythona przypisze wartości do x oraz y dokładnie w kolejności od lewej do prawej, a więc x = 0, y = 'Anna'
#
# Nie ma znaczenia, w jakiej kolejności my uzyjemy nazw po lewej stronie operatora przypiszania. Jeśli zamienimy x oraz y miejscami:
# (y, x) = (0, 'Anna')
#
# to interpreter nadal wykona przypisanie kolejno od lewej do prawej, a więc y = 0, x = 'Anna'
# 
# jest to bardzo wazna funkcjonalność przy pracy z krotkami, o której nalezy pamiętać
    
