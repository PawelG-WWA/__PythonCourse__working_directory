# ZADANIE
#
# Uzupełnij pola _gap_1,_gap_2, _gap_3, _gap_4, _gap_5 tak,
# aby kazdy chłopiec był w parze z kazdą dziewczynką
#
# Oczekiwany wynik:
# ['John - Ann', 'John - Clementine', 'John - Meryl', 'George - Ann', 'George - Clementine', 'George - Meryl', 'Michael - Ann', 'Michael - Clementine', 'Michael - Meryl']

boys = ['John', 'George', 'Michael']
girls = ['Ann', 'Clementine', 'Meryl']

pairs = [boy + ' - ' + girl for boy in boys for girl in girls]
print(pairs)