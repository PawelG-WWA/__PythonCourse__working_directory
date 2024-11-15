# ZADANIE
#
# Napisz funkcję unbox_order przyjmującą parametry:
# processor,
# memory,
# hard_drive,
# graphics,
# power_supply
#
# Następnie stwóz jakiś obiekt iterowalny w zakresie globalnym, który będzie zawierał części komputerowe
#
# Przekaz ten obiekt w taki sposób, aby nie odnosić się do elementów tego obiketu np. poprzez indeks
#
# Wykorzystaj w tym celu mozliwości rozpakowywania obiektów iterowalnych do listy argumentów
#
# Wewnątrz funkcji wypisz na ekranie elementy przekazane jako argumenty. Przykładowy wynik:
# Your package contains:
#    Processor: Intel Core i5
#    Memory: Kingston 16GB
#    Hard drive: Kingston SSD 512GB
#    Graphics: ASUS GeForce RTX 3060
#    Power supply: Cooler Master 750W
#
# PYTANIE
# Jakiego rodzaju dopasowanie argumentów zostanie zastosowane?

def unbox_order(processor, memory, hard_drive, graphics, power_supply):
    print('''Your package contains:
    Processor: %s
    Memory: %s
    Hard drive: %s
    Graphics: %s
    Power supply: %s''' % (processor, memory, hard_drive, graphics, power_supply))


my_order = ['Intel Core i5', 'Kingston 16GB', 'Kingston SSD 512GB', 'ASUS GeForce RTX 3060', 'Cooler Master 750W']

unbox_order(*my_order)

# WYJAŚNIENIE + ODPOWIEDŹ
#
# Powyzej stworzyliśmy obiekt listy, w tym przypadku listy napisów. Mogłaby być to równiez krotka, która takze jest obiektem iterowalnym.
#
# Następnie przekazaliśmy tę listę jako argument do funkcji unbox_order. Nazwa listy została poprzedzona pojedynczą gwiazdką, co oznacza,
# ze elementy listy zostaną rozpakowane i przyporządkowane argumentom funkcji kolejno od lewej do prawej.
#
# Uzyte w tym przykładzie zostanie więc dopasowanie argumentów przez pozycję