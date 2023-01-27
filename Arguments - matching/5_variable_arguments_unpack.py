def unpack_example(name, age, occupation):
    print('----- unpack example -----')
    print(name, age, occupation)

def unpack_dict_example(can_commit=False, can_pull=False, can_push=False, can_fork=False):
    print('----- unpack dict example -----')
    print(can_commit, can_fork, can_pull, can_push)

user_data = ('John', 33, 'driver')
user_access = { 'can_commit': True, 'can_pull': True, 'can_push': True, 'can_fork': True }

unpack_example(*user_data)

print()

unpack_dict_example(**user_access)


# WYJAŚNIENIE
#
# definiujemy dwie funkcje - unpack_example oraz unpack_dict_example
#
# Obydwie przyjmują jakąś liste argumentów
#
# Następnie definiujemy w zakresie globalnym dwa obiekty - pierwsze, user_data, będący obiektem typu tuple zawierającym
# dane uzytkownika oraz drugi, user_access, będącym obiektem typu dictionary zawierającym konfigurację dostępu uzytkownika
# do zasobów.
#
# mając takie obiektu, przekazanie parametrów do funkcji musiało by się odbyć poprzez wskazanie indeksem lub kluczem
# poządanych wartości, np:
#
# unpack_example(user_data[0], user_data[1], user_data[2])
# unpack_dict_example(user_acces[can_commit], user_access[can_pull], user_access[can_push], user_access[can_fork])
#
# Jak widzisz, wywołanie takiej fynkcji w taki sposób moze być karkołomne, nieczytelne i wymagać bardzo duzo skupienia oraz
# uwagi
#
# Mozemy jednak zastosować - podobnie jak w przypadku pakowania, lecz teraz w momencie wywoływania funkcji - specjalnych znaków
# gwiazdki (*) poprzedzających przekazywany do funkcji argument.
#
# W taki sposób moza przekazać wyłącznie obiekty iterowalne (jak krotki czy słowniki)
#
# W przypadku krotki, poprzedzenie jej nazwy pojedynczą gwiaxdką sprawi, ze wartości przechowywane w krotce zostaną
# rozpakowane i dopasowane do argumentów funkcji według pozycji
#
# W przypadku słownika, poprzedzonego dwiema gwiazdkami w momencie wywołania funkcji, słownik zostanie
# rozpakowany i jego klucze i wartości zostaną dopasowane do argumentów według słów kluczowych
#
# Podobnie jak w przykładach z pliku 4_variable_arguments_list_pack nie jest to zbyt popularna metoda przekazywania argumentów,
# jednak warto ją znać mając na uwadze, ze mozemy się z nia spotkać w naszej codziennej, zawodowej pracy