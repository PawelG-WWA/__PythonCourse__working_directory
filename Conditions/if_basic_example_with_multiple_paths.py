x = 0 # Przypisanie wartości 0 do zmiennej x

if x < 0: # instrukcja if wskazująca, ze mamy do czeynienia z warunkiem logicznym, który zdefiniowany jest za słowem if
    print('x mniejsze od 0 od zera') # kod do wykonania, jeśli warunek logiczny jest spełniony
elif x == 0:
    print('x równe 0') # kod do wykonania, jeśli drugi warunek logiczny nie jest spełniony
else:
    print('x większe od 0') # kod do wykonania, jeśli zaden warunek logiczny nie jest spełniony

print('koniec')

# Przebieg algorytmu
# 1. Przysz nazwie x wartość 0
# 2. Sprawdź, czy wartość pod x jest mniejsza od 0
# 3. Nie, wartość zapisana pod x nie jest mniejsza od 0
# 4. Przejdź do kolejnego testu warunku logicznego w instrukcji elif
# 5. Sprawdź, czy wartość zapisana pod x jest równa 0
# 6. Tak, wartość zapisana pod x jest równa zero
# 7. Wypisz na ekranie 'x równe 0'
# 8. Pomiń instrukcję else i blok kodu w zakresie instrukcji else, poniewaz juz wykonaliśmy pozytywny test warunku logicznego
# 9. Wypisz na ekranie napis 'koniec'