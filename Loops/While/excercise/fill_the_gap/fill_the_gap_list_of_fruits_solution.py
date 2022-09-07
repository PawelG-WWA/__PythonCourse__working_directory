list_of_fruits = ['jablko', 'banan', 'truskawka']

while list_of_fruits: # sprawdza, czy lista nie jest pusta, odpowiednik warunku to len(list_of_fruits) > 0
    print(list_of_fruits[0])
    list_of_fruits = list_of_fruits[1:]

print('koniec')