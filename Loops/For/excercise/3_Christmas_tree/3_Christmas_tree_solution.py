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

number_of_levels = input('How many levels the Christmas Tree should have?: ')

if number_of_levels.isnumeric():
    current_level = 0
    current_number_of_stars = 1
    current_number_of_spaces = int(number_of_levels) - 1

    for level in range(0, int(number_of_levels)):
        stars = '*' * current_number_of_stars
        spaces = ' ' * current_number_of_spaces
        print('%s%s' % (spaces, stars))
        current_number_of_stars = current_number_of_stars + 2
        current_number_of_spaces = current_number_of_spaces - 1
else:
    print('Value is not a number. THE END.')