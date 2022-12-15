# ZADANIE
#
# Podane jest zdanie sentence = "Madam, I'm Adam"
#
# Palindrom to słowo, wyrazenie lub zdanie, którego szyk liter od lewej do prawej jest taki sam jak od prawej do lewej
#
# Palindromem jest więc np. słowo kajak
#
# Napisz funkcję is_palindrome, która sprawdzi, czy przekazany ciąg znaków jest palindromem.
#
# UWAGA: Istnieje wiele metod napisania takiej funkcji. Dobrze, jeśli będziesz skupiał się na jak najbardziej efektywnym
# rozwiązaniem problemu w sposób wykorzystujący jak najwięcej mozliwości Pythona (np. właściwość, ze ciąg znaków jest kolekcją znaków)
#
# W sprawdzaniu mozesz pominąć przecinki, spacje i apostrofy - sprawdź tylko kolejność liter
#
# PYTANIE 1:
# Czy przekazana do funkcji is_palindrome zmienna sentence ulegnie zmianie wewnątrz funkcji?

sentence = "Madam, I'm Adam"

def is_palindrome(s):
    clean_string = s.replace(',','').replace("'", '').replace(' ', '')
    reversed_clean_string = s[::-1].replace(',','').replace("'", '').replace(' ', '')
    return clean_string.lower() == reversed_clean_string.lower()

print(is_palindrome(sentence))
print(sentence)


# Wyjaśnienie
#
# Funkcja is_palindrome przyjmuje argument s
#
# W momencie wywołania, kiedy następuje przypisanie obiektu do lokalnej zmiennej s funkcji is_palindrome, s wskazuje na ten sam
# łańcuch znaków (obiekt), co zmienna sentence. Zmienna globalna sentence oraz lokalna zmienna s wskazują na ten sam ciąg - "Madam, I'm Adam"
#
# W pierwszej linii czyścimy łańcuch znaków s ze wszystkich przecinków, spacji i apostrofów
# W kolejnej linii robimy to samo, ale z odwróconym łancuchem znaków (s[::-1] to instrukcja wycinka zwracająca odwróconą kolekcję)
#
# Następnie porównujemy obydwa ciągi znaków ze znakami pomniejszonymi - jest to istotne, poniewaz te same znaki rózniące się wielkością
# nie są takie same w świecie programowania (np M oraz m to dwa rózne znaki, aby porównać napisy, musimy przekonwertować znaki wszystkie znaki
# w ciągu na małe lub na wielkie i tylko wtedy je porównywać)
#
# Na końcu wypisujemy wynik wywołania funkcji is_palindrome z przekazanym do niej argumentem sentence oraz łańcuch znaków sentence po wywołaniu funkcji
#
# PYTANIE 1 - ODPOWIEDŹ:
# Nie, ani do sentence, ani do s nie zostanie przypisana zadna nowa wartość, na którą mogłyby wskazywać obydwie zmienne
# Funkcja replace wywoływana na obiekcie s zwraca zawsze nowy ciąg znaków - ciągi znaków są niemutowalne, tzn. ze ewentualna modyfikacja
# zaawsze wiąze się ze zwróceniem nowego ciągu znaków.
#
# To samo dotyczy wycinków - tworzenie wycisnka z s jak powyzej: s[::-1] nie modyfikuje obiektu przechowywanego pod s, a jedynie zwraca nowy
# wynikowy, stworzony na bazie s
#
# Do samego końca więc lokalne dla funkcji is_palindrome s wskazuje na ten sam obiekt (ciąg znaków) co globalna zmienna sentence - mozesz
# to sprawdzić dodając linijkę print(s) przed instrukcją return w funkcji is_palindrome