# Zadanie
#
# Ponizsze dane prezentują słownik, którego kluczami są imiona osób, a wartościami listy osób, z którymi dana osoba jest w relacji
#
# Napisz program, który dla kazdej z osób wypisze osoby, z którymi dana osoba jest w relacji, np w poniszy sposób:
#
# Paul is in relation with: Ann, Frank, 
# Ann is in relation with: Paul, 
# Frank is in relation with: Paul, Kate, 
# Martin is in relation with: 
# Kate is in relation with: Frank,

people = {
    'Paul': ['Ann', 'Frank'],
    'Ann': ['Paul'],
    'Frank': ['Paul', 'Kate'],
    'Martin': [],
    'Kate': ['Frank']
}