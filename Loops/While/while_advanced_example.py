x = 'abc' #Przypisz nazwie x wartość tekstową 'abc' (zainicjalizuj zmienną x wartością tekstową 'abc')

while x: #deklaracja pętli i określenie warunku logicznego - dla łańcuchów znaków (typ string) warunek jest prawdziwy, jeśli łańcuch nie jest pusty; zapis jest równowazny z: while len(x) > 0 lub while x != ''
    print(x) #wypisz wsartość zapisaną pod zmienną x
    x = x[0:len(x)-1] #przypisz nazwie x nową wartość, będącą wycinkiem biezącego łańcucha od pierwszego do przedostatniego znaku.
print("koniec") #Po zakończeniu działania pętli (po wyjściuz pętli) wypisz na ekrtanie napis koniec

# Przebieg algorytmu
# 1. Przypisz nazwie x wartość tekstową 'abc'
# 2. Sprawdź, czy wartość zapisana pod nazwą x ('abc') nie jest pustym łańuchem znaków (dzieje się to automatyczne, powyzszy zapis jest równowazny z: while len(x) > 0 lub while x != ''
# 3. Tak, łańuch nie jest pusty, wykonaj iterację pętli (wykonaj kod znajdujący się w zakresie pętli)
# 4. Wypisz wartość zapisaną pod x ('abc')
# 5. Przypisz nazwie x wycinek z biezącej wartosci zapisanej pod x ('abc') od początku łańcucha (od znaku na pozycji 0, od znaku 'a'), do przedostatniego znaku (len(x)-1)
# 6. Wróc do warunku logicznego pętli w linii 3 i sprawdź, czy wartość zapisana pod nazwą x ('ab') nie jest pustym łańcuchem znaków 
# 7. Tak, łańuch nie jest pusty, wykonaj iterację pętli
# 8. Wypisz wartość zapisaną pod x ('ab')
# 9. Przypisz nazwie x wycinek z biezącej wartości zapisanej pod x ('ab') od początku łańcucha (od znaku na pozycji 0, od znaku 'a'), do przedostatniego znaku (len(x)-1)
# 10. Wróc do warunku logicznego pętli w linii 3 i sprawdź, czy wartość zapisana pod nazwą x ('a') nie jest pustym łańcuchem znaków 
# 11. Tak, łańuch nie jest pusty, wykonaj iterację pętli
# 12. Wypisz wartość zapisaną pod x ('a')
# 13. Przypisz nazwie x wycinek z biezącej wartości zapisanej pod x ('a') od początku łańcucha (od znaku na pozycji 0, od znaku 'a'), do przedostatniego znaku (len(x)-1)
# 14. Wróc do warunku logicznego pętli w linii 3 i sprawdź, czy wartość zapisana pod nazwą x ('') nie jest pustym łańcuchem znaków 
# 15. Nie, łańuch jest pusty, nie wykonuj iteracji pętli
# 16. Wypisz na ekranie napis 'koniec'
