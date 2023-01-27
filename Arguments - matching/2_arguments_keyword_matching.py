import json
import os

def read_configuration():
    with open(os.path.realpath('Arguments - matching/Assets/config.json'), 'r') as config_file:
        return json.load(config_file)

def configure_user_access(can_push, can_pull, can_commit, can_fork):
    configuration = read_configuration()
    configuration['can_push'] = can_push
    configuration['can_pull'] = can_pull
    configuration['can_commit'] = can_commit
    configuration['can_fork'] = can_fork

    save_configuration(configuration)


def save_configuration(configuration):
    with open(os.path.realpath('Arguments - matching/Assets/config.json'), 'w') as config_file:
        json.dump(configuration, config_file)


configure_user_access(
    can_push=False,
    can_pull=True,
    can_commit=False,
    can_fork=False)


# WYJAŚNIENIE
#
# Ten przykład jest nieco bardziej skomplikowany celem odświezenia wiedzy a takze dodania nowego elementu
#
# W tym przykładzie definiujemy az 3 funkcje:
# -read_configuration
# -save_configuration
# -configure_user_access
#
# importujemy równiez pakiety os oraz json
# Pakiet os jest juz w niwielkim stopniu znany i wykorzystamy go jak do tej pory - wskazania ściezki do pliku
# z konfiguracją
#
# Pakiet json to nowy pakiet, którego jeszcze nie uzywaliśmy
#
# Dostarcza on funkcje umozliwiające pracę z formatem json (Java Script Object Notation). Jeśli nie znasz tego formatu -
# nie przejmuj się. Jest to prosty zapis pól klucz-wartość, dokładnie jak w słowniku. Po wykonaniu programu zachęcam Cię
# do zajrzenia do pliku Assets/config.json z tego folderu aby przyjrzeć się zawartości pliku.
#
# Funkcja read_configuration odczytuje konfigurację z pliku config.json znajdującego się w folderze Assets
# Do tej pory uzywaliśmy funkcji open do stworzenia zmiennej takiej jak file_handler, na której mogliśmy wykonywac
# rózne operacje
#
# Teraz uzyliśmy instrukcji with ... as
# Instrukcja with ... as zwalnia nas z obowiązku pamiętania o konieczności zwolnienia zasobów (np. wywołania funkcji close()
# po zakończeniu pracy z plikiem). Porównaj z funkcją read_file_data z pliku 2_functions_basics_complex_example.py. Obydwie funkcje
# robią dokładnie to samo, ale wersja with ... as jest bardziej zwięzła. Warto jednak znać obydwa sposoby pracy z zasobami,
# aby rozumieć, co się dzieje w trakcie wykonywania programu.
#
# W funkcji read_configuration instrukcja with ... as odczytuje plik spod wskazanej ściezki i tworzy zmienną
# o wymyślonej przeze mnie nazwie config_file. Następnie wywoływana jest funkcja json.load z argumentem config_file.
#
# json.load odczytuje dane zapisane w pliku i konwertuje je do obiektu słownika w Pythonie. Tak naprawdę, jeśli
# nie napisalibyśmy json.load, a zamiast tego stworzyli zmienną, np:
# config_data = json.load(config_file)
#
# otrzymalibyśmy obiekt słownika przechowywany pod zmienną config_data. Tym samym wywołanie type(config_data)
# zwróciłoby obiekt <class dict>. Spróbuj dodać odpowiednie instrukcje stworzenia zmiennej z obiektu zwracanego
# przez json.load i funkcji type, aby przekonać się, ze to, co zwraca json.load to obiekt słownika.
#
# W końcu, funkcja read_configuration zwraca obiekt słownika, a instrukcja with ... as zwalnia zasoby za nas (wywołuje close())
#
# Funkcja save_configuration robi niemal dokładnie to samo, ale rpacuje z plikiem config.json w trybie zapisu. Aby zapisać
# słownik w formacie JSON w pliku config.json, uzywamy funkcji json.dump(konwertowany_obiekt, plik)
#
# Skupmy się teraz na najwaniejsze funkcji z perspektywy naszego przykładu - configure_user_access
# 
# Funkcja ta przyjmuje kilka parametrów konfigurujących dostęp uzytkownika do róznych akcji jak can_pull, can_push itd..
#
# Oczywiściem parametrów konfiguracji moze być znacznie więcej, ale dla uproszczenia zdefiniowaliśmy tylko 4.
#
# W metodach konfiguracyjnych takich jak ta, przekazywanie argumentów pozycyjnych jest trudne do odszyfrowania.
#
# Wyobraź sobie, ze tę funkcję wywołalibyśmy w następujący sposób:
# configure_user_access(False, False, True, False)
#
# Bez wiedzy o tym, które argumenty odpowiadają jakim wpisom w konfiguracji nie jesteśmy jako programiści
# w stanie stwierdzić, co tak naprawdę konfigurujemy.
#
# Wywołanie funkcji z uzyciem słów kluczowych jak w powyzszym przykładzie znacznie upraszcza czytanie kodu oraz daje nam
# wiedzę i kontrolę nad, którym zmiennym przekazujemy jaką wartość
#
# Nie naduzywaj jednak argumentów słów kluczowych w innuych funkcjach. Jeśli stworzylibysmy w zakresie globalnym zmienne
# can_push=False,
# can_pull=True,
# can_commit=False,
# can_fork=False
#
# moglibyśmy spokojnie wywołać funkcję w następujący sposób, uzywając wyłącznie składni argumentów pozycyjnych,
# bez uzywania słów kluczowych:
# configure_user_access(can_push, can_pull, can_commit, can_fork)
#
# Uzywanie słów kluczowych w takich funkcjach jak konfiguracja jest jednak przydane, poniewaz pozwala pominąć
# zmudny i często zbędny proces tworzenia zmiennych o takich samych nazwach jak argumenty tylko po to,
# aby te argumenty przekazać linijkę nizej