# W zadaniu mozesz wykorzystać funkcję write_to_file zdefiniowaną ponizej

import os

def write_to_file(filename, data):
    with open(os.path.realpath('Arguments - matching/excercise/4_arguments_matching_pack/Assets/%s' % filename), 'w') as file:
        file.write(data)
        file.write('\n')

# ZADANIE 1
#
# Napisz funkcję add_squad przyjmującą argument squad, do którego spakowana zostanie dowolna ilość przekazanych w wywołaniu funkcji
# argumentów. Jakiego typu jest argument squad weewnątrz funkcji add_squad?
#
# Dodatkowo, wypisz na ekranie wszystkich członków składu. Pamiętaj, ze do funkcji mozesz przekazac dowolną
# ilość członków zespołu, dlatego raz napisany kod, bez wprowadzania późniejszych zmian powinien zadziałać
# tak samo dla jednego, dwudziestu i 100 przekazanych argumentów. Jakiej konstrukcji uzyjesz?

# def ... - tu napisz funkcję add_squad


add_squad('Jack', 'George', 'Jimmy', 'Karen')