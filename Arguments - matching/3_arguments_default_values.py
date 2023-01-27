import json
import os

def read_configuration():
    with open(os.path.realpath('Arguments - matching/Assets/config.json'), 'r') as config_file:
        return json.load(config_file)

def configure_user_access(can_push=False, can_pull=False, can_commit=False, can_fork=False):
    configuration = read_configuration()
    configuration['can_push'] = can_push
    configuration['can_pull'] = can_pull
    configuration['can_commit'] = can_commit
    configuration['can_fork'] = can_fork

    save_configuration(configuration)


def save_configuration(configuration):
    with open(os.path.realpath('Arguments - matching/Assets/config.json'), 'w') as config_file:
        json.dump(configuration, config_file)


configure_user_access(can_pull=True)

# WYJAŚNIENIE
#
# W stosunku do przykładu z pliku 2_arguments_keyword_matching z biezącego folderu zmianie uległa
# jedynie funkcja configure_user_access
#
# Zauwaz, ze lista argumentów tej funkcji zawiera operator przypisania
#
# Operator przypisania uzyty na liście argumentów funkcji sluzy do przypisywania argumentów domyślnych
#
# Funkcję configure_user_access mozemy wywołać nie podając zadnych argumentów:
# configure_user_access()
# 
# i interpreter Pythona nie zgłosi zadnyhc wątpliwości! Po wywołaniu programu bez podawania argumentów, jeśli
# funkcja posiada wartości domyślne, to te wartości będą uzyte w zakresie lokalnym funkcji. Wywołanie funkcji
# configure_user_access bez argumentów sprawi więc, ze w zakresie lokalnym tej funkcji parametry wymienione w definicji
# przyjmą domyślne wartości:
# can_push=False
# can_pull=False
# can_commit=False
# can_fork=False
#
# Jak tę wiedzę mozemy wykorzystać w praktyce?
# 
# Mozemy na przykład wykorzystać znajomośc dopasowania argumentów po słowach kluczowych tak jak w powyzszym przykładzie:
#
# configure_user_access(can_pull=True)
# 
# Takie wywołanie funkcji configure_user_access sprawi, ze tylko parametr can_pull przyjmie wskazaną w wyołaniu funkcji
# wartość, natomiast reszta zmiennych będzie miała wartości domyślne.
#
# mozesz się o tym przekonać uruchamiając program i sprawdzając plik config.json z folderu Assets:
# can_push": false, "can_pull": true, "can_commit": false, "can_fork": false}
#
# Mozemy równiez wywołać funkcję configure_user_access uzywając parametrów pozycyjnych, jednak wtedy nie mozemy ustawić
# wartości dowolnej zmiennej z zakresu argumentów - dopasowanie będzie nastepowało od lewej do prawej:
# configure_user_access(True) = configure_user_access(can_push=True, can_pull=False, can_commit=False, can_fork=False)
# configure_user_access(True, True) = configure_user_access(can_push=True, can_pull=True, can_commit=False, can_fork=False)
# configure_user_access(True, True, True) = configure_user_access(can_push=True, can_pull=True, can_commit=True, can_fork=False)
# configure_user_access(True, True, True, True) = configure_user_access(can_push=True, can_pull=True, can_commit=True, can_fork=True)
