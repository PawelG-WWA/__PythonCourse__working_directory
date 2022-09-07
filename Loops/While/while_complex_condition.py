a = 23 # Przypisz nazwie a wartość liczbową 23

while a > 0 and a%3 != 0: # dopóki a jets większe od zera i reszta z dzielenia z przez 3 nie wynosi 0, wykonuj blok kodu zawarty wewnątrz bloku while
    print('a = %s' % a) # wypisz wartość zapisaną pod nazwą a
    a = a - 1 # pomniejsz a o 1 przed kolejną iteracją

print('a = %s; a/3 = %s' % (a, a/3)) # wypisz a, dla którego warunek pętli nie został spełniony 
                                     # w naszym przypadku, a, które było większe od 0 i którego reszta z dzielenia przez 3 nie wynosiła 0

# Przebieg algorytmu:
# 1. Przypisz nazwie a wartośc liczbową 23
# 2. Sprawdź, czy a (23) jest większe od 0 i czy a podzielone przez 3 daje resztę rózną od zera
# 3. Tak, a (23) jest większe od 0 i wynik dzielenia a przez 3 daje resztę rózną od zera
# 4. wypisz wartość przechowywaną pod zmienną a (23)
# 5. Pomniejsz a o jeden (a = 23 - 1)
# 6. Sprawdź, czy a (22) jest większe od 0 i czy a podzielone przez 3 daje resztę rózną od zera
# 7. Tak, a (22) jest większe od 0 i wynik dzielenia a przez 3 daje resztę rózną od zera
# 8. wypisz wartość przechowywaną pod zmienną a (22)
# 9. Pomniejsz a o jeden (a = 22 - 1)
# 10. Sprawdź, czy a (21) jest większe od 0 i czy a podzielone przez 3 daje resztę rózną od zera
# 11. Nie, choć a (21) jest większe od 0 to wynik dzielenia a przez 3 daje resztę równą zero
# 12. Wyjdź z pętli
# 13. wypisz a oraz wynik dzielenia a przez 3

# Podsumowanie:
# Warunek logiczny pętli while moze być złoony. Iteracja pętli zostanie wykonana wyłącznie, jeśli cały warunek logiczny zwraca wartość True
# W przeciwnym wypadku wykonanywanie pętli zakończy się. Mimo, ze, a > 0, to a podzielone przez 3 nie daje reszty róznej od zera, pętla więc nie wykona się