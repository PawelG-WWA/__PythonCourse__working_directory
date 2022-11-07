from re import X


x = 0

def multiply_x(multiplier):
    global x
    x = 10
    x = x * multiplier

multiply_x(10)

print(x)

# Wyjaśnienie
#
# Na początku tworzymy zmienną x równą 0
#
# Zmienna ta jest stworzona w zasięgu globalnym
#
# Następnie definiujemy funkcję multiply_x, którą wywołujemy z argumentem 10
#
# Na końcu wypisujemy x z zasięgu globalnego. Wynik to 100
#
# Dzieje się tak przez uzycie w funkcji multuply_x instrukcji global.
#
# Mówi ona, aby x było pobrane z zasięgu globalnego. Powoduje to, ze z z zasiegu globalnego będzie teraz wskazywało na wartość 10, a nie 0
#
# Następnie w funkcji wartość x z zasięgu globalnego jest zmieniana na biezącą wartość x powiększoną o wartość zmiennej multiplier
#
# Gdy wypiszemy na końcu globalne x, otrzymamy wynik 100, poniewaz:
# -wskazaliśmy w funkcji poprzez uzycie instrukcji global, aby x uzywane w funkcji było pobierane z zasięgu globalnego, a nie lokalnego
# -globalnemu x została przypisana wartość 10
# -później nowa wartość przypisywana do x, to wartość bieąca x pomnozona przez wartość przechowywaną pod multiplier (10)
#
# Nie zwracamy wyniku z funkcji - funkcja posiada tzw. efekt uboczny, czyli zmienia coś, co jest poza jej zakresem, w tym wypadku globalne x.
#
# Nalezy uwazać ze stosowaniem kwantyfikatora global, poniewaz moze on wprowadzić do kodu sporo zamieszania, przy czym jego znajomość moze byc przydatna