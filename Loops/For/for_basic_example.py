title = 'predator'

for letter in title:
    print(letter.upper(), end='')

print('\n')

print('KONIEC')

# Przebieg algorytmu
#
# 1. Nazwie title przypisz wartość tekstową 'predator'
# 2. Z kolekcji - łańcucha znaków title - weź element ('p') i przypisz go nazwie letter
# 3. Wypisz na ekran znak przechowywany pod nazwą letter ('p'), powiększając go do wielkiej litery
# 4. Weź następny element z kolekcji title ('r') i przypisz go nazwie letter
# 5. Wypisz na ekran znak przechowywany pod nazwą letter, powiększając go do wielkiej litery
# ... powtarzaj kroki 4-5 az nie będzie więcej elementów dopobrania z kolekcji title
# 6. wypisz na ekran nową, pustą linię
# 7. wypisz na ekran napis 'KONIEC'

L = ['one', 'two', 'three']

for i in range(len(L)):
    L[i] = L[i].upper()


print(L)