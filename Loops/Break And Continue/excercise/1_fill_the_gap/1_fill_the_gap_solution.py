# Zadanie 1
# w miejscu _gap_1 uzyj warunku i slowa kluczowego continue tak, aby pominąć wszystkie
# liczby niepodzielne przez 3. Wypisz na ekran tylko liczby podzielne przez 3 w zakresie od 1 do 100

for x in range(1, 101):
    if x % 3:
        continue
    print(x)


# Zadanie 2
# Pętla while True: to pętla która moze działać w nieskończonośc. Czasami chcemy aby tak działała, ale tez mozemy chcieć ją zatrzymać.
#
# Pobieraj w pętli dane od uyzytkownika dopóki nie wpisze słowa break.
#
# Jeśli uzytkownik wpisze słowo break, wyjdź z pętli
while True:
    x = input('Podaj dowolne słowa, jeśli napiszesz słowo "break", pętla zakończy się: ')
    
    if x == 'break':
        break
print('KONIEC')
