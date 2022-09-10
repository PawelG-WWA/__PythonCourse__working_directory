x = 16

while x%2 == 0:
    print('Reszta z dzielenia %s / 2 wynosi 0' % x)
    x = x//2 #moze tez być x = x/2, ale zostanie zmieniony typ danych na liczbę zmiennoprzecinkową i wynik 16/2 będzie wynosił 8.0, a nie 8

print('wartość dla której reszta z dzielenia przez 2 nie wynosi 0 to %s' % x)