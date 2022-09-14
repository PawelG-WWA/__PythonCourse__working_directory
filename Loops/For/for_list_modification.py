fruits = ['apple', 'pineapple', 'strawberry']

for fruit in fruits:
    fruit = fruit.upper() #zmienia wartość przechowywaną pod nazwą fruit, a nie element listy

print(fruits)

for i in range(len(fruits)):
    fruits[i] = fruits[i].upper() # zmienia element listy

print(fruits)

# Przebieg algorytmu
#
# 1. Stwórz listę owoców z trzema elementami
# 2. Z listy fruits pobierz element, przypisz jego wartość do nazwy fruit
# 3. przypisz do nazwy fruit nowy napis, który jest taki sam jak aktualny, ale powiększony do wielkich liter
# ... zroób to samo ze wszystkimi pozostałymi elementami listy fruits
# 4. Wypisz listę fruits - lista fruits nie zmieniła się
# 5. Stwórz zakres od 0 do 3 (len(fruits) jest równe 3)
# 6. Weź wartość z zakresu (0) i przypisz ją do i
# 7. Zamień element listy na pozycji i (fruits[0]) na ten sam napis, ale powiększony do wielkich liter
# ... wykonaj kroki 6-7 dla pozostałych elementów listy
# 8. wypisz na ekranie listę fruits - tym razem lista fruits została zmieniona
#
# WYJAŚNIENIE
#
# funkcja range tworzy zakres od 0 do 3, ale 3 jest otwartą granicą przedziału, co oznacza, ze iteracja jest
# po wartościach kolejno 0, 1, 2. W zapisie matematycznym równowazne zdanie wygląda następująco: [0, 3) lub <0, 3),
# tj. wszystkie wartości od zera do trzy, ale bez 3.