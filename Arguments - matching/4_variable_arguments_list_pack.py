def pack_simple_example(*arguments):
    print('------ pack simple example ------')
    print(arguments)
    print(type(arguments))
    print(arguments[0])
    print(arguments[1])
    print(arguments[2])


def pack_dict_example(**arguments):
    print('----- pack dict example -----')
    print(arguments)
    print(type(arguments))


name = 'John'
age = 33
occupation = 'driver'

pack_simple_example(name, age, occupation)

print()

pack_dict_example(name='Paul', age=20, occupation='singer')

# WYJAŚNIENIE
#
# Istnieje mozliwość przekazania dowolnej liczby argumentów do funkcji i spakowania ich do jednej zmiennej
# 
# Funkcja pack_simple_example zdefiniowana jest z argumentem arguments poprzedzonym pojedynczą gwiazdką
#
# Oznacza to, ze przekazane argumenty przekonwertowane będą do obiektu tuple i to z takim obiektem będziesz
# pracował w zakresie lokalnym funkcji, o czym mozesz się przekonać po uruchomieniu programu.
#
# Druga funkcja- pack_dict_example - definiuje równiez parametr arguments, ale poprzedzony dwie gwiazdkami
#
# Oznacza to, ze funkcja przyjmuje wyłącznie parametry ze słowami kluczowymi, a te zostaną przekonwertowane do słownika.
# Przekonaj się o tym uruchamiając program i analizując wypisany na ekranie wynik.
#
# Jeśli chodzi o praktyczne zastosowania, to raczej spotkasz się z tymi metodami przekazywania argumentów dosyć rzadko
# o ile nie będziesz pracował z wyspecjalizowanymi bibliotekami, gdzie nie wiadomo, ile argumentów mozna przekazac do funkcji
#
# Jak pisano wcześniej, najpowszechniejszą metodą przekazywania argumentów jest przekazywanie ich przez pozycję
#
# Argumenty domyślne i ze słowami kluczowymi równiez są spotykane, ale znacznie rzadziej.
#
# Metoda z przykładów powyzej jest zdecydowanie najmniej powszechna