def multiply_word(w, m):
    return w * m

word = 'something'
multiplier = 3

multiplied_word = multiply_word(word, multiplier)

print(multiplied_word)

# Wyjaśnienie
#
# Na początku definiujemy funkcję multiply+word przyjmującą dwa parametry - w (od word - słowo) i m (od multiplier - mnoznik).
# Nie jest to najlepszy sposób na nazywanie argumentów funkcji, ale słuzy ilustracji tego,
# ze zmienne lokalne odnoszące się do lokalnych argumentów nie są tymi samymi zamiennymi, co przekazywane argumenty
#
# Funkcja zwraca podane słowo w powtórzone m razy
#
# Następnie tworzymy zmienne word oraz multiplier: word = 'something' , multiplier = 3
#
# Dalej wywołujemy multiply_word, przekazując stworzone chwilę wcześniej word oraz multiplier jako argumenty
#
# Wynik wywołania przypisujemy do multiplied_word, którego wartość wypisujemy na ekranie.
#
# Wynik działania programu:
# somethingsomethingsomething
#
# W momencie wywołania funkcji multiply_word(word, multiplier) zmienne lokalne w oraz m wskazują na te same obiekty,
# co zmienne word oraz multiplier - odpowiednio 'something' oraz 3.