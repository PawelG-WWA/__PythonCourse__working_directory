# ZADANIE
#
# Dana jest lista zawodników players. Kazdy zawodnik posiada następujące dane:
#    -player_id - identyfikator zawodnika
#    -name - imię zawodnika
#    -age - wiek zawodnika
#    -club_id - identyfikator klubu, w którym gra zawodnik
#
# Dana jest równiez lista klubów. Kazdy klub posiada następujące dane:
#    -club_id - identyfikator klubu
#    -name - nazwa klubu
#
# Zadanie polega napisaniu instrukcji listy składanej, która:
#    -wybierze zawodników w wieku powyzej 30 lat
#    -wybierze kluby o club_id < 3
#    -będzie zwracać do listy wynikowej łańcuhy znaków będące pełnymi danymi zawodnika w formacie:
#        Zawodnik: imię_zawodnika, wiek: wiek_zawodnika, klub: nazwa_klubu
#
# Na końcu po stworzeniu listy naley wypisać wszystkie elementy
#
# Oczekiwany wynik:
#
# Wynikowa lista zawiera dwa elementy: ['Zawodnik: Robert, wiek: 33, klub: Tokio', 'Zawodnik: Cristian, wiek: 35, klub: Nowy Jork']
#
# Na ekranie wypisane są elementy listy wynikowej jeden pod drugim:
# Zawodnik: Robert, wiek: 33, klub: Tokio
# Zawodnik: Cristian, wiek: 35, klub: Nowy Jork
#
# Czyli zawodnicy w wieku powyzej 30 lat grający w klubach, których id jest mniejsze od 3

players = [
    { 'player_id': 1, 'name': 'Robert', 'age': 33, 'club_id': 1 },
    { 'player_id': 2, 'name': 'Cristian', 'age': 35, 'club_id': 2 },
    { 'player_id': 3, 'name': 'Lion', 'age': 34, 'club_id': 3 },
    { 'player_id': 4, 'name': 'Jacob', 'age': 22, 'club_id': 1 },
    { 'player_id': 5, 'name': 'Karim', 'age': 30, 'club_id': 2 }
]

clubs = [
    { 'club_id': 1, 'name': 'Tokio' },
    { 'club_id': 2, 'name': 'Nowy Jork' },
    { 'club_id': 3, 'name': 'Madryt' }
]

players_in_clubs_one_and_two = [ 'Zawodnik: %s, wiek: %s, klub: %s' % (player['name'], player['age'], club['name'])
    for player in players if player['age'] > 30
    for club in clubs if club['club_id'] < 3 and player['club_id'] == club['club_id']]

for player_data in players_in_clubs_one_and_two:
    print(player_data)