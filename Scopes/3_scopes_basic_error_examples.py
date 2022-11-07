# UWAGA !!!!
#
# Wszystkie ponizsze przykłady będą generować błędy
#
# Aby uruchomić przykłady osobno i zobaczyć informacje o błędach, naley zakomentować odpowiednie linie kodu z przykładami

# PRZYKŁAD 1 - Nieudana próba wykorzystania zmiennej globalnej w funkcji

x = 0

def add(number):
    x = x + number
    return x

print(add(1))

# PRZYKŁAD 1 - Wyjaśnienie:
#
# Wynik: 
# UnboundLocalError: local variable 'x' referenced before assignment
# (uzycie referencji x przed przypisaniem)
#
# Powyzej najpierw tworzymy zmienną x o zasięgu globalnym z przypisaną wartością x = 0
#
# Następnie w funkcji add próbujemy przypisać do x wynik dodawania x + number, przy czym podczas wywołania funkcji add
# wartość number wynosi 1. Mozemy spodziewać się zatem, ze wynik dodawania x + number wyniesie 1 (0 + 1).
#
# W zamian dostajemy jednak błąd próby pobrania wartości zmiennej przed jej przypisaniem.
#
# Dzieje się tak dlatego, ze zmienna przed uzyciem powinna mieć przypisaną wartość
#
# Gdy wykonuje się funkcja add(1), Python tworzy lokalną zmienną x do której będzie chciał przypisać wynik dodawania x + number
#
# Problem w tym, ze x po prawej stronie przypisania tez jest teraz interpretowany jako lokalny x, do którego nie została
# przypisana jeszcze zadna wartość - dopiero chcemy to zrobić! Rozwiązaniem moze być zmiana nazwy lokalnego x (a więc tego po lewej
# stronie operatora przypisania w funkcji add), np na y. Wówczas python podczas wykonywania dodawania uzyje globalnego x, tj x = 0


# PRZYKŁAD 2
#
# Uzycie zmiennej lokalnej poza zakresem

x = 0

def add(number):
    z = x + number
    return z

print(add(10))
print(z + 1)

# PRZYKŁAD 2 - Wyjaśnienie
#
# Wynik:
# 10
# NameError: name 'z' is not defined
#
# W powyzszym przykładzie definiujemy funkcję add
#
# Wewnątrz funkcji zostanie stworzona zmienna o nazwie z i przypisany do niej będzie wynik dodawania x (globalnego, x = 0) oraz number
# (lokalnego dla funkcji, number = 10 w momencie wywołania)
#
# Następnie wypiszemy na ekran wynik dodawania - 10
#
# Później w nieprawidłowy sposób spróbujemy wykorzystać zmienną z, którą stworzyliśmy wywołują funkcję add(10)
#
# Python zwróci błąd, poniewa zmienna z jest lokalną zmienną funkcji add! Zmienne globalne mogą być wykorzystywane
# wewnątrz wfunkcji w ich lokalnym zakresie, ale zmienne lokalne - stwlrzone w funkcji i na jej potrzeby - nie mogą
# być wykorzystywane w taki sposób poza swoim zakresem, który jest zakresem funkcji!