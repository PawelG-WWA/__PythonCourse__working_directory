def factorial(n):
    if n < 0:
        print('silnia to permutacja zbioru, nie istnieje ujemna liczba mozliwych permutacji zbioru')
        return 0
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(4))

# WYJAŚNIENIE
#
# Jest to najbardziej klasyczny przykład rekurencji, ułatwiający zrozumienie podstaw funkcji rekurencyjnych,
# a więc takich, które wywołują same siebie.
#
# Zadaniem funkcji factorial jest obliczenie silni z n - n!. Silnia to iloczyn kolejnych liczb od 1 do n.
# Zapis 6! oznacza więc 1 * 2 * 3 * 4 * 5 * 6, a wynik jest równy 720.
#
# Funkcja factorial przyjmuje jako parametr n, a więc liczbę, dla której będziemy wyznaczać silnię.
#
# Następnie sprawdzamy warunek n < 0, poniewaz chcemy liczyć silnię tylko dla całkowitych liczb dodatnich (naturalnych),
# gdyz silnię traktujemy jako ilośc permutacji zbioru - zbiór nie moze mieć ujemnej liczby elementów. totez nie moze istnieć
# ujemna ilość jego permutacji. Dlatego, jeśli n jest mniejsze od 0, wyświetlamy na ekranie stosowny komunikat, a następnie
# zwracamy 0.
#
# Jeśli n jest równe 0, to zwracamy 1, poniewaz jest tylko jedna mozliwość poukładania zbioru pustego. Dla n = zwracamy więc 1
#
# Obydwa powyzsze warunki to warunki brzegowe/warunki zakończenia rekurencji. Z następnym akapitem nabierze to więcej sensu.
#
# Jeśli bowiem obydwa powyzsze warunki nie są spełnione, wówczas mnozymy n razy kolejna wartość zwrócona przez funkcję factorial,
# a więc przez wynik wywołania factorial(n - 1).
#
# Mnozenie jest oczywiście działaniem przemiennym, więc np dla n = 3, n! = 1 * 2 * 3 i da taki sam wynik jak 3 * 2 * 1 = 6
#
# Dla n = 4 wywołanie rekurencyjne funkcji factorial(4) ma następujący przebieg:
# 1. Sprawdź, czy n < 0
# 2. Nie, 4 nie jest < 0, sprawdź czy n = 0
# 3. Nie, 4 nie jest równe 0
# 4. Wywołaj funkcję factorial(3)
# 5. Sprawdź, czy n < 0
# 6. Nie, 3 nie jest < 0, sprawdź czy n = 0
# 7. Nie, 3 nie jest równe 0
# 8. Wywołaj funkcję factorial(2)
# 9. Sprawdź, czy n < 0
# 10. Nie, 2 nie jest < 0, sprawdź czy n = 0
# 11. Nie, 2 nie jest równe 0
# 12. Wywołaj funkcję factorial(1)
# 13. Sprawdź, czy n < 0
# 14. Nie, 1 nie jest < 0, sprawdź czy n = 0
# 15. Nie, 1 nie jest równe 0
# 16. Wywołaj funkcję factorial(0)
# 17. Sprawdź, czy n < 0
# 18. Nie, 0 nie jest < 0, sprawdź czy n = 0
# 19. Tak, 0 jest równe 0, zwróc 1
# 20. Wróć do funkcji factorial, która wywołała factorial(1) (krok 12) i pomnóz 2 * 1 - wynik = 2
# 21. Wróć do funkcji factorial, która wywołała factorial(2) (krok 8) i pomnóz 3 * 2 - wynik = 6
# 22. Wróć do funkcji factorial, która wywołała factorial(3) (krok 4) i pomnóz 4 * 6 - wynik 24
# 23. Wyjdź z funkcji factorial(4) wywołanej na najwyzszym poziomie rekurencji
# 24. Wypisz wynik na ekranie - 24