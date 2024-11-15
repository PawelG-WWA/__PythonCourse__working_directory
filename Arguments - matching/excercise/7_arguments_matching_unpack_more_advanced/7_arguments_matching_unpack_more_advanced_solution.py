# ZADANIE
#
# Do wykonania tego zadania wykorzystaj fucnkję unbox_order, którą stworzyłeś w zadaniu poprzednim
#
# Tym razem jednak kolekcję, którą przekazujesz do funkcji unbox_order zamień na słownik
#
# Jaki otrzymałeś wynik?
#
# Co powinieneś zrobić, aby program zadziałał poprawnie?
#
# Jakiego rodzaju dopasowanie argumentów zostanie zastosowane tym razem?
# 
# Czy program zadziała inaczej, jeśli zmienisz kolejność elementów słownika?
#
# Przykładowy wynik:
# Your package contains:
#    Processor: Intel Core i5
#    Memory: Kingston 16GB
#    Hard drive: Kingston SSD 512GB
#    Graphics: ASUS GeForce RTX 3060
#    Power supply: Cooler Master 750W

def unbox_order(processor, memory, hard_drive, graphics, power_supply):
    print('''Your package contains:
    Processor: %s
    Memory: %s
    Hard drive: %s
    Graphics: %s
    Power supply: %s''' % (processor, memory, hard_drive, graphics, power_supply))


my_order = {
    'memory': 'Kingston 16GB',
    'graphics': 'ASUS GeForce RTX 3060',
    'processor': 'Intel Core i5',
    'hard_drive': 'Kingston SSD 512GB',
    'power_supply': 'Cooler Master 750W'
}

unbox_order(**my_order)

# WYJAŚNIENIE + ODPOWIEDŹ
#
# Powyzej stworzyliśmy obiekt słownika, w tym przypadku pary klucz-wartość odpowiadają częściom komputerowym.
#
# Następnie przekazaliśmy ten słownik jako argument do funkcji unbox_order. Nazwa słownika została poprzedzona dwiema gwiazdkami, co oznacza,
# ze elementy słownika zostaną rozpakowane i przyporządkowane argumentom funkcji po słowach kluczowych, gdzie klucz ze słownika będzie
# oznaczał nazwę zmiennej, a wartość dla tego klucza zostanie przypisana wartości zmiennej kluczowej.
#
# Uzyte w tym przykładzie zostanie więc dopasowanie argumentów przez słowa kluczowe, dlatego kolejność elementów w słoniku nie ma zadnego znaczenia
# dla wyniku programu!