# W zadaniu mozesz wykorzystać funkcję write_to_file zdefiniowaną ponizej

import os

def write_to_file(filename, data):
    with open(os.path.realpath(
        'Arguments - matching/excercise/5_arguments_matching_pack_more_advanced/Assets/%s' % filename),
        'w') as file:
        file.write(data)
        file.write('\n')


# ZADANIE 1
#
# Napisz funkcję add_squad przyjmującą argument squad, do którego spakowana zostanie dowolna ilość przekazanych w wywołaniu funkcji
# argumentów. Tym razem wywołując funkcję add_squad przekaz wyłącznie argumenty ze słowem kluczowym.
#
# Jakich zmian dokonasz w stosunku do poprzedniego zadania?
# 
# Jakiego typu jest argument squad weewnątrz funkcji add_squad?
#
# Dodatkowo, wypisz na ekranie wszystkich członków składu. Pamiętaj, ze do funkcji mozesz przekazac dowolną
# ilość członków zespołu, dlatego raz napisany kod, bez wprowadzania późniejszych zmian powinien zadziałać
# tak samo dla jednego, dwudziestu i 100 przekazanych argumentów. Jakiej konstrukcji uzyjesz?
def add_squad(**squad): 
    print(type(squad))

    for position in squad:
        print('Position: %s, player: %s' % (position, squad[position]))

    write_to_file('squads.txt', str(squad))


add_squad(goalkeeper="Jimmy", defender='John', midfielder='Jack', attacker='Jason')

# WYJAŚNIENIE
#
# Przekazując wyłącznie argumenty ze słowami kluczowymi, aby mogły być spakowane do lokalnej zmiennej squad przyjmowanej
# przez funkcję add_squad jako argument, nalezy poprzedzić nazwę argumenu w definicji funkci dwiema gwiazdkami.
#
# Spowoduje to, ze argumenty przekazane jako słowa kluczowe staną się dostępne w funkcji add_squad jako
# pary klucz-wartość słownika. Stąd typ danych zmiennej squad wewnątrz funkcji add_squad to dict
#
# zmieni się równiez pętla for, która teraz musi dla kluczy pobrać ich wartości.

