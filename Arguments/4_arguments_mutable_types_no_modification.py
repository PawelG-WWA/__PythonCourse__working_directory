the_list = [1, 2, 3]

def test(list, element):
    list.append(element)
    print('list in test: %s' % list)

test(the_list[:], 4)

print(the_list)

# Wyjaśnienie
#
# Na początku tworzymy listę the_list
#
# Następnie definiujemy funkcję test, która przyjmuje dwa argumenty - listę oraz element, który wykorzystamy do modyfikacji listy
#
# Wewnątrz funkcji test dodajemy do przekazanej jako argument listy obiekt, do którego odnosi się referencja element
#
# Później wypisujemy listę lokalną dla funkcji test
#
# W kolejnej lisnii wywołujemy funkcję test przekazując jako parametr:
# -Wycinek listy the_list zwracający cały przedział listy, a więc [1, 2, 3]
# -cyfrę 4
#
# Na końcu wypisujemy oryginalną, stworzoną na początku listę the_list
#
# Okazuje się, ze w funkcji test lokalna referencja list odnosi się do obiektu listy o następujących elementach: [1, 2, 3, 4]
# Lista the_list natomiast posiada trzy elementy: [1, 2, 3]
#
# Dzieje się tak dlatego, ze wycinek listy - jak wiemy z poprzednich rozdziałów - zwraca nową listę. Zapis the_list[:]
# kopiuje całą listę od początku do końca. Do funkcji test jest więc przekazana kopia listy the_list, a nie ta lista
#
# W konsekwencji wszystkie operacje wykonywane wewnątrz funkcji test na obiekcie na który wskazuje lokalna dla funkcji referencja list
# są wykonywane na kopii listy stworzonej z listy the_list w momencie wywołania funkcji test.
#
# Podsumowując, do funkcji test przekazaliśmy nie listę the_list, ale jej kopię stworzoną pod innym adresem w pamięci komputera i to na tą
# kopię wskazywać będzie lokalna referencja list w fu nkcji test