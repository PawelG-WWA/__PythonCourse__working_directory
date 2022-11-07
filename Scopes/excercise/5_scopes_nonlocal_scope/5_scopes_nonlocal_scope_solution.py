# ZADANIE
#
# Zmień kod w taki sposób, aby wynik wykonania ponizszego programu wynosił 12

x = 10

def enclosing_function():
    x = 11

    def nested_function():
        nonlocal x
        x = 12
    
    nested_function()
    print(x)

enclosing_function()

# WYJAŚNIENIE
#
# Pierwsze x (x = 10) jest tworzone w zasięgu globalnym
#
# Kolejne x (x = 11) jest tworzone w zasięgu lokalnym funkcji enclosing_function
#
# Naszym celem jest zmienić lokalne dla enclosing_function x w taki sposób, aby print(x) wypisało wartośc przypisaną do x w nested_function
#
# Jeśli zostawimy po prostu w nested_function samo przypisanie x = 12, to Python stworzy zmienną x w zakresie lokalnym funkcji nested_function
#
# Wartość ta będzie więc niewidoczna dla wszystkich pozostałych zakresów, a więc równiez dla zakresu enclosing_function, gdzie lokalne x nadal będzie równe 11
#
# Aby nested_function mogło przypisać do nielokalnie utworzonego x nową wartość widoczną poza lokalnym zakresem funkcji nested_function,
# nalezy wskazać przy uzyciu kwantyfikatora nonlocal, ze x nie pochodzi z zakresu lokalnego nested_function
#
# Python więc będzie poszukiwał x w innym zakresie - tu w zakresie zawierającym (Enclosing) i do tamtego x, które zostało utworzone z wartością
# 11 przypisze wartość 12
#
# nested_function do x, które jest lokalne dla enclosing_function przypisze nową wartość,
# która po wywołaniu nested_function będzie dostępna pod x w enclosing_function