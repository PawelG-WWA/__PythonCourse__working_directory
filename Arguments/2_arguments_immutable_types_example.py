some_tuple = (1, "ring", { 'to': 'rule them all'})

def some_function(t):
    print(f't in some_function: {t}')
    t = ('some', 'random', 'quote')
    print(f't in some_function: {t}')

some_function(some_tuple)

print(some_tuple)

# Wyjaśnienie
#
# Na początku tworzymy krotkę (tuple) przechowującą trzy obiekty - cyfrę 1, napis 'ring' oraz słownik { 'to': 'rule them all'}
#
# Następnie definiujemy funkcję some_function, która:
# -przyjmuje jako parametr zmienną t
# -wypisuje to, co t wskazuje (do czego jest referencją)
# -zmienia to, co t przechowuje (zmienia referencję na inny obiekt/krotkę)
# -ponownie wypisuje to, na co t wskazuje (do czego jest referencją)
#
# Następnie wywoływana jest funkcja some_function z some_tuple jako argumentem
#
# Na samym końcu wypisywana jest wartość na którą wskazuje some_tuple
#
# W momencie wywołania some_function referencje t oraz some_tuple wskazują na ten sam obiekt, czyli krotkę: (1, "ring", { 'to': 'rule them all'})
# Świadczy o tym pierwszy komunikat wypisywany z funkcji some_function - t jest referencją do dokładnie tej samej krotki: (1, "ring", { 'to': 'rule them all'})
#
# Następnie przypisujemy do t inną krotkę: ('some', 'random', 'quote')
#
# Krotki są typami niemutowalnymi. Oznacza to, ze t wskazuje teraz (jest referencją) do innej krotki - typy niemutowalne nie mogą być zmieniane w miejscu.
#
# Oznacza to, ze lokalna zmienna t pierwotnie przechowująca referencję taką jak przekazana krotka some_tuple teraz jest referencją do innej krotki
# Świadczy o tym drugi wypisywany komunikat z funkcji some_function: t in some_function: ('some', 'random', 'quote')
#
# Po wykonaniu się funkcji some_function wypisujemy na ekran obiekt na który wskazuje referencja (zmienna) some_tuple - jak widać,
# jest to oryginalny, przekazany do funkcji some_function obiekt: (1, 'ring', {'to': 'rule them all'})
#
# Mimo, ze some_tuple przekazane do some_function oraz t lokalne dla some_function na początku wywołania funkcji wskazują na ten sam obiekt (krotkę),
# to przypisanie nowego obiektu do zmiennej t nie powoduje zmiany obiektu, na który wskazuje some_tuple! Zmienna lokalna t funkcji some_function
# moze zostać zmieniona bez konsekwencji dla argumentu, który został do niej przypisany w momencie wywołania funkcji.