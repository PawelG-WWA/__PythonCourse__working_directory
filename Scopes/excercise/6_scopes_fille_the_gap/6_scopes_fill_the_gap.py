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
    _gap_1
    z = 3
    y *= 2

    def multiply_y_by_x():
        _gap_2
        y *= x
    
        def multiply_y_by_z():
            _gap_3
            _gap_4
            z *= 2
            y *= z

        multiply_y_by_z()

    multiply_y_by_x()

multiply_y_by_2()
print(y)

# Pytanie dodatkowe - dlaczego nie musimy uzywac zadnego kwantyfikatora (ani global, ani nonlocal), aby uzyc zmiennej x z globalnego zakresu?