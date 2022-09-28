# Zadanie
#
# Napis zpętlę for, w której zamienisz wszystkie lementy listy numbers na napis 'zero'
# 
# Zanim dany element zamienisz na napis 'zero', wypisz na ekranie informację:
# 'changing _element_ to "zero"', gdzie "_element_" to aktualnie przetwarzany element
#
# Wykorzystaj do tego funkcję enumerate i zwracaną przez nią krotkę
#
# Na końcu wypisz na ekranie listę
#
# Przykładowy wynik:
# numbers = ['zero', 'zero', 'zero']

numbers = ['one', 'two', 'three']

for (index, number) in enumerate(numbers):
    print('changing %s to "zero"' % number)
    numbers[index] = 'zero'

print('numbers = %s' % numbers)

# Dodatkowe wyjaśnienie
#
# number = 'zero' zmieni tylko wartość przypisaną do zmiennej number, a nie element listy,
# wywołanie numbers[index] = 'zero' zmieni zaś element listy na podanym indeksie