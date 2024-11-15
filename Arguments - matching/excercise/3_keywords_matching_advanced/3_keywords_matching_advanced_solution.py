import os

def write_to_file(filename, data):
    with open(os.path.realpath('Arguments - matching/excercise/3_keywords_matching_advanced/Assets/%s' % filename), 'a') as file:
        file.write(data)
        file.write('\n')

# ZADANIE 1
# Dana jest funkcja configure przyjmująca parametry server_name, database_name, user_id oraz password
#
# PYTANIA:
# 1. Jakiej kategorii są te parametry?
# 2. Spróbuj wywołać funkcję przekazując argumenty w rózny sposób - poprzez słowo kluczowe
#    oraz pozycyjnie. Jakie przeszkody, błedy oraz mozliwości znalazłeś?
def configure(server_name, database_name="core", user_id="default", password="abc"):
    configuration = {
        'server_name': server_name,
        'database_name': database_name,
        'user_id': user_id,
        'password': password
    }

    write_to_file('3_excercise_1.txt', str(configuration))

# ODPOWIEDŹ
#
# Ad. 1: Funkcja przyjmuje parametry wymagające podania wartości w momencie wywołania oraz parametry domyślne
# Ad. 2: Funkcję mozemy wywołać na wiele poprawnych sposobó:

configure('server name') # podanie wartości tylko pierwszego parametru, reszta bedie miała wartości domyślne

configure('server_name', 'backup') # podanie wartości kilku parametrów których wartości zostaną dopasowane
                                   # pozycyjnie od lewej do prawej. Dla reszty parametrów (user_id oraz password w tym przypadku)
                                   # zostaną uzyte wartości domyślne

configure(server_name="local") # podanie pierwszego parametru poprzez słowo kluczowe, dla pozostałych parametrów
                               # zostaną uzyte wartości domyślne

configure('local', user_id='new_user') # podanie wartości pierwszego parametru nie mającego wartości domyślnej, którego
                                       # wartość będzie dopasowana w sposób pozycyjny (server_name = 'local'),
                                       # a następnie podanie dowolnego parametru ze zbioru tych, które posiadają wartości domyślne.
                                       # Dla pozostałych parametrów nie wskazanych na liście argumentów w takim wywołaniu zostaną
                                       # uzyte wartości domyślne, o ile takie były.

# Istnieją jednak takie mozliwości wywołania funkcji configure, które spowodują błąd.
# Aby przekonać się o problemach wynikającyhc z uzycia wywołań, odkomentuj kod:
# ---- KOD ----
# configure(database_name='far_away_db') # TypeError - brakuje wymaganego argumentu pozycyjnego: server_name
                                         # argument ten nie posiada wartości domyślnej, więc podanie jego wartości jest wymagane

# ---- KOD ----
# configure('server_name', database_name='some_database', 'new_user', 'new_password')
# SyntaxError: W powyzszym przykładzie podaliśmy server_name jako pierwszy argument pozycyjnie, następnie poprzez słowo kluczowe
# został wskazany argument database_name, a później, za argumentem ze słowem kluczowym podaliśmy kolejne argumenty pozycyjne.
# Interpreter Pythona zwraca błąd Syntax Error, poniewaz niedozwolone jest podawanie argumentów pozycyjnych za argumentami
# ze słowem kluczowym. Wynika to z tego, ze nie wiadomo, ktore argumenty nalezy po słowie kluczowym dopasować. Moglibyśmy 
# napisać coś następującego: configure('server_name', user_id='some user', 'some_user2', 'new password') - zauwaz, ze argument
# z id uzytkownika moglby zostac dwa razy. Stąd właśnie wynika błąd Syntax Error - pozycyjne dopasowanie argumentów działa tylko
# przed wszystkimi argumentami ze słowami kluczowymi.


# ZADANIE 2
#
# Popraw błędy w ponizszych wywołaniach funkcji configure:

configure(user_id='new_user')
# WYJAŚNIENIE: Brak wymaganego argumentu pozycyjnego nie zawierającego domyślnej wartości - server_name

configure('server_name', user_id='new_user', 'database_name', 'password')
# WYJAŚNIENIE: po przekazaniu jakiegokolwiek argumentu przy uzycia słowa kluczowego nie mozna po nim
#              podawać argumentów nie uzywając słów kluczowych

configure()
# WYJAŚNIENIE: Podobnie jak w pierwszym przykładzie - brakuje wymaganego argumentu pozycyjnego server_name.
#              Wystarczy podać tylko ten argument, a dla reszty zostaną uzyte wartości domyslne wskazane w
#              definicji funkcji configure.


# ZADANIE 3
#
# Dlaczego w ponizszym przykladzie nie ma błędu?
configure(password='abc', user_id='new_user', database_name='db', server_name='server_name')
# WYJAŚNIENIE: wszystkie argumenty zostały przekazane jako słowa kluczowe - równiez wymagany argument server_name,
#              nie posiadający wartości domyślnej. W związku z tym interpreter Pythona wie, w jaki sposób
#              przypisać lokalnym zmiennym funkcji configure wartości