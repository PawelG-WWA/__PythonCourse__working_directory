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

# def ... - tu napisz funkcję add_squad


add_squad(goalkeeper="Jimmy", defender='John', midfielder='Jack', attacker='Jason')