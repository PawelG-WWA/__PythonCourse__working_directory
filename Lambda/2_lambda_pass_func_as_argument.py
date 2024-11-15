def some_function(x, y, func):
    print(x)
    print(y)
    print(func(x, y))


my_lambda_expression = lambda x, y: x * y

some_function(4, 2, my_lambda_expression)

# WYJAŚNIENIE
#
# Na samym początku definiujemy funkcję some_function, która po prostu wypisuje na ekran przekazane argumenty x oraz y,
# a następnie wypisuje na ekranie wynik działania przezkazanego jako func
#
# Później tworzymy zmienną my_lambda_expression i przypisujemy do niej wyrazenie lambda zdefiniowane jako zwykłe mnozenie
# dwóch argumentów
#
# Na samym końcu wywołujemy funckję some_function przekazując do niej dwie liczby i zmienną, która jest
# referencją do funkcji zdefiniowanej za pomocą wyrazenia lambda.
#
# Na ekranie zostają wypisane argumenty oraz wynik funkcji func, przekazanej jakos argument, którym jest
# nasze wyrazenie lambda.
#
# Zauwaz, ze takie wywoływanie funkcji jest dosyć niebezpieczne, poniewaz dla przekazanych argumentów musi
# byc zdefiniowany operator wykorzystywany wewnątrz zapisanej z pomocą wyrazenia lambda, a trzeci argument musi być funkcją.
#
# W prawdziwym programie, moglibyśmy dodać sprawdzanie typów (z uzyciem instrukcji type) w celu zabezpieczenia się przed
# błędami TypeError.