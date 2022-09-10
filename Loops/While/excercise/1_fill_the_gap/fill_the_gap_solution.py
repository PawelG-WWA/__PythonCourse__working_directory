x = 'Przykładowy tekst'

while x:
    print(x[len(x)-1:len(x)], end='')
    x = x[0:len(x)-1]