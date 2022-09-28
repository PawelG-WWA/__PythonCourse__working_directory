# Zadanie
#
# Narysuj choinkę ze znaków gwiazdki jak ponizej, uywając pętli for. Uzytkownik powinien mieć mozliwość wprowadzenia
# ilośc poziomów choinki.
#
# Przykład działania programu:
# How many levels the Christmas Tree should have?: 4
#
#    *
#   ***
#  *****
# *******


# Rozwiązanie 1
number_of_levels = input('How many levels the Christmas Tree should have?: ')

if number_of_levels.isnumeric():
    current_level = 0
    current_number_of_stars = 1
    current_number_of_spaces = int(number_of_levels) - 1

    for level in range(int(number_of_levels)):
        stars = '*' * current_number_of_stars
        spaces = ' ' * current_number_of_spaces
        print('%s%s' % (spaces, stars))
        current_number_of_stars = current_number_of_stars + 2
        current_number_of_spaces = current_number_of_spaces - 1
else:
    print('Value is not a valid number. THE END.')


# Rozwiązanie 2
# w pierwszy rozwiązaniu przechodziliśmy pętlę n razy, a tutaj musimy przejść trzy pętle
# jedną n razy
# drugą n * x razy
# trzecią n * y razy
# więc jest więcej operacji
if number_of_levels.isnumeric():
    for level in range(int(number_of_levels)):

        for x in range(int(number_of_levels) - (level + 1)):
            print(' ', end='')

        for y in range(2 * level + 1):
            print('*', end='')
        
        print()
else:
    print('Value is not a valid number. THE END.')