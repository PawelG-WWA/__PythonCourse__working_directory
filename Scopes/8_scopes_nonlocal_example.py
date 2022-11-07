x = 10

def enclosing_function():
    x = 11

    def enclosed_function():
        nonlocal x
        x = x + 1
    
    enclosed_function()
    print(x)


enclosing_function()

# Wyjaśnienie
#
# Na początku tworzymy zmienną o nazwie x przechowującą wartość 10
#
# Następnie definiujemy funkcję enclosing_function, w której:
#   -tworzymy zmienną lokalną x dla tej funkcji o wartości 11 - x = 11
#   -definiujemy funkcję enclosed_function, w której:
#       -wskazujemy, ze x uzywane w tej funkcji nie pochodzi z lokalnego zakresu, ale z zakresu funkcji zawierajacej
#       -nielokalne z powiększamy o wartość 1
#   -następnie w funkcji enclosing_function() wywołujemy zdefiniowaną w niej funkcję enclosed_function() i wypisujemy
#   - x, które jest lokalne dla funkcji enclosing_function()
#
# Na końcu wywołujemy funkcję enclosing_function()
#
# Wynikiem powyzszych czynności jest wypisanie na ekranie liczby 12
#
# Tak jak opisano w części teoretycznej, Python przeszukuje zasięgi w następującej kolejności:
# 1. Zasięg lokalny (Local)
# 2. Zasięg zawierający (Enclosing)
# 3. Zasieg globalny (Global)
# 4. Zasięg wbudowany (Built-in)
#
# W powyzszym przykładzie wewnętrzną funkcją wywoływaną jest enclosed_function(), a funkcją zawierającą enclosing_function()
#
# enclosed_function wskazuje, ze x, którego będzie uzywac nie pochodzi z jej zakresu lokalnego. Do wskazania tego słuzy instrukcja nonlocal
#
# Bez uzycia kwantyfikatora nonlocal otrzymalibyśmy błąd, tak jak w przykładzie z pliku 7_scopes_enclosing_error_example.py
#
# Gdybyśmy bowiem pominęli słowo nonlocal, Python próbowałby utworzyć zmienną x w zakresie lokalnym enclosed_function,
# a do tego potrzebował by równiez jednocześnie uzyć x działaniu x + 1, jednak x nie byłoby przecie jeszcze utworzone!
#
# Właśnie do rozwiązania tego problemu słuzy instrukcja nonlocal
#
# x dostępne w enclosed_function pochodzi więc z lokalnego zasięgu enclosing_function i jest równe 11, a nie 10, tak jak x w zasięgu globalnym
#
# Dzięki nonlocal mozemy jednak zmienić x z zakresu lokalnego funkcji enclosing_function wewnątrz enclosed_function
#
# Nie nalezy przesadzać z uzywaniem instrukcji nonlocal, poniewaz ma ona potencjał do wprowadzania w kodzie nieptorzebnego zamieszania