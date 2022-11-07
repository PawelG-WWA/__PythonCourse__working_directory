# PRZYKŁAD 1

y = 2

def multiply_y(multiplier):
    return y * multiplier

print(multiply_y(10))

# PRZYKŁAD 1 - Wyjaśnienie
#
# zmienna o nazwie y przechowująca cyfrę 2 jest zdefiniowana w zasięgu globalnym, poza definicją funkcji w zakresie def
#
# mozna więc uzyc zmiennej y w def i Python przeszuka najpierw zasięg lokalny funkcji multuply_y, nie znajdując w nim y, a następnie
# przeszuka zasięg globalny, w którym znajduje się nazwa y i uzyje jej wartości
#
# Wynik: 20


# PRZYKŁAD 2
def multiply_z(multiplier):
    return z * multiplier

z = 10

print(multiply_z(10))

# PRZYKŁAD 2 - wyjaśnienie
#
# funckaj multiply_z została zdefiniowana przed przypisaniem wartości (uwtorzeniem z), a mimo to funkcja zadziała\
#
# Zmienna z równie zostanie pobrana z zasięgu globalnego, tak jak y w przykładzie nr 1
#
# Przeszukiwanie zasięgów odbywa się w momencie wywołania funkcji (jak w print(multiply_z(10))), a nie w momencie napotkania
# przez interpreter slowa def


# PRZYKŁAD 3
x = 0

def multiply_x(multiplier):
    x = 9
    return x * multiplier

print(multiply_x(10))

# PRZYKŁAD 3 - wyjaśnienie
#
# Na początku tworzymy x w zakresie globalnym i przypisujemy mu wartośc 0
#
# Następnie definiujemy funkcję, w której równiez jest zmienna o nazwie x, ale przypisujemy do niej 9
#
# Wynik x * multiplier to 90, a nie 0. Dzieje się tak dlatego, ze x wewnątrz funkcji multiply_x jest innym x, niz x uzywane poza funkcją
#
# W funkcji jest to x zdefiniowane w zakresie lokalnym
#
# Poza funkcją zaś istnieje tylko x zdefiniowane w zakresie globalnym, które jest innym x
#
# Funkcja uzywa swojego lokalnego x, poniewaz to tam Python w pierwszej kolejności znajduje x, do którego przypisana jest wartość 9
#
# Dlatego właśnie wynik jest równy 90


# PRZYKŁAD 4
def multiply_x_ver2(multiplier):
    return x * multiplier

print(multiply_x_ver2(10))

# PRZYKŁAD 4 - wyjaśnienie
#
# Tym razem stworzyliśmy inną wersję funkcji multiply_x z dopiskiem _ver2
#
# Ta funkcja nie tworzy w swoim zakresie zmiennej o nazwie x, dlatego x, który zostanie uzyty pochodzić będzie z zakresu globalnego
#
# Oznacza to, ze tym razem wynik wywołania funkcji multiply_x_ver2 będzie równy 0