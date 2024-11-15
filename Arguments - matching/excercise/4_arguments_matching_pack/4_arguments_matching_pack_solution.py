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
def add_squad(*squad):
    print(type(squad))

    for member in squad:
        print(member)

    write_to_file('squads.txt', str(squad))

add_squad('Jack', 'George', 'Jimmy', 'Karen')

# WYJAŚNIENIE
#
# Aby spakować dowolną ilość przekazanych argumentów do jednego argumentu w zakresie funkcji lokalnej będącego argumentem
# funkcji add_squad, nazwę argumentu (squad) nalezy poprzedzić gwiazdką.
#
# Typ argumentu to tuple
#
# W związku z tym, ze pakowanie zawsze odbywa się do typu iterowalnego, a tuple jest takim typem, do wypisania
# na ekran mozna uzyc pętli - np. for
# 
# Na końcu funkcji jej wynik zapisujemy do pliku, jeśli mamy na to ochotę, ake nie jest to wymagane
#
# Wywołanie funkcji add)squad nawet z tysiącem argumentów zadziała zawsze tak samo.