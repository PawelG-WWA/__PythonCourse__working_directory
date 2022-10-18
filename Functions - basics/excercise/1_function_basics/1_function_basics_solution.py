# Dany jest kod:

name = input('Imię: ')
if name != '':
    print(name)
else:
    print('Pole "Imię" nie moze byc puste')

age = input('Wiek: ')
if age != '':
    print(age)
else:
    print('Pole "Wiek" nie moze byc puste')

occupation = input('Zawód: ')
if occupation != '':
    print(occupation)
else:
    print('Pole "Zawód" nie moze byc puste')

# ZADANIE:
#
# Zidentyfikuj w powyzszym przykładzie powtarzające się instrukcje. Wyizoluj je i napisz funkcję, która odwzoruje wielokrotnie
# skopiowaną logikę z przykładu w jednym miejscu. Następnie wywołaj tę funkcję odpowiednią ilość razy. Porównaj wyniki z kodem powyzej
#
# Podpowiedź:
# Spróbuj dodać do funkcji jakiś parametr (argument), dzięki któremu funkcja ta stanie się bardziej ogólna/uniwersalna,
# pozwalając na wykonanie tego samego kodu dla nieograniczonej ilości pytań

def ask(question):
    answer = input('%s: ' % question)
    if answer != '':
        print(answer)
    else:
        print('Pole "%s" nie moze byc puste' % answer)

ask('Imię')
ask('Wiek')
ask('Zawód')