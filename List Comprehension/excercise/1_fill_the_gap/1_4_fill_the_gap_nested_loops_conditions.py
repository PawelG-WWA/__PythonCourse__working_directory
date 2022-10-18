# ZADANIE
#
# Uzupełnij pola _gap_1, _gap_2, _gap_3, _gap_4, _gap_5, _gap_6 tak, aby ułozyć terminarz meczów
#
# Uwzględnij warunek, ze dana druzyna nie powinna grać sama ze sobą
#
# Oczekiwany wynik:
# Barcelona vs. Manchester
# Barcelona vs. Milan
# Barcelona vs. Munich
# Manchester vs. Barcelona
# Manchester vs. Milan
# Manchester vs. Munich
# Milan vs. Barcelona
# Milan vs. Manchester
# Milan vs. Munich
# Munich vs. Barcelona
# Munich vs. Manchester
# Munich vs. Milan

teams = ['Barcelona', 'Manchester', 'Milan', 'Munich']
matches = [_gap_1 for _gap_2 in _gap_3 for _gap_4 in _gap_5 if _gap_6]

for match in matches:
    print(match)