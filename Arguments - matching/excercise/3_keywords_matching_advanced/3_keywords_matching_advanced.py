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


# ZADANIE 2
#
# Popraw błędy w ponizszych wywołaniach funkcji configure:

# ---- KOD 1 ----
# configure(user_id='new_user')

# ---- KOD 2 ----
# configure('server_name', user_id='new_user', 'database_name', 'password')

# ---- KOD 3 ----
# configure()


# ZADANIE 3
#
# Dlaczego w ponizszym przykladzie nie ma błędu?
configure(password='abc', user_id='new_user', database_name='db', server_name='server_name')
