# ZADANIE
#
# Dane są:
# x = 10
# y = 12
# oraz funkcje, które nalezy uzupełnić:
# -multiply_y_by_2
# -multiply_y_by_x
# -multiply_y_by_z
#
# Funkcje zawierają działania.
#
# Wystąpienia _gap_1, _gap_2, _gap_3 i _gap_4 zastąp kodem, który sprawi, ze działania wykonają się bez błędów,
# a końcowy wynik wypisany na ekranie wyniesie 1440

x = 10
y = 12

def multiply_y_by_2():
    global y # _gap_1
    z = 3
    y *= 2

    def multiply_y_by_x():
        global y #_gap_2
        y *= x
    
        def multiply_y_by_z():
            nonlocal z #_gap_3
            global y #_gap_4
            z *= 2
            y *= z

        multiply_y_by_z()

    multiply_y_by_x()

multiply_y_by_2()
print(y)

# Wyjaśnienie
#
# _gap_1 - uzywa y z globalnego zakresu
# _gap_2 - uzywa y z globalnego zakresu. Mimo, ze poprzednia funkcja juz uzywa y z globalnego zakresu,
#          to funkcja zawarta tez musi wiedzieć w powyzszym przykładzie, ze y znajduje się w globalnym zakresie.
#          Inaczej nastąpi próba stworzenia zmiennej y w funkcji multiply_y_by_x z jednoczensym wykorzystaniem y przed przypisaniem
#          do niego wartości
# _gap_3 - uzywa z pochodzącego z zakresu funkcji zawierającej. Jest to konieczne, poniewaz dwie linie dalej uzywamy z do przypisania
#          nowej wartości do z. Bez uzycia nonlocal Python zgłosił by bląd
# _gap_4 - uzywa y z globalnego zakresu
#
# Pytanie dodatkowe - dlaczego nie musimy uzywac zadnego kwantyfikatora (ani global, ani nonlocal), aby uzyc zmiennej x z globalnego zakresu?
# ODPOWIEDŹ:
#
# Poniewaz x nie nsastępuje próba stworzenia zmiennej o nazwie x wewnątrz funkcji multiply_y_by_x, Python wyszuka x zgodnie z hierarchią
# przeszukiwania zakresów i odnajdzie x w zakresie globalnym