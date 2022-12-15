employees = {
    'Pawel': { 'age': 33, 'position': 'programmer' },
    'John': { 'age': 30, 'position': 'manager' }
}

def add_entry(d, key, value):
    print('d in update_entry: %s' % d)
    d[key] = value
    print('d in update_entry: %s' % d)

add_entry(employees, 'Martha', { 'age': 35, 'position': 'programmer' })

print(employees)

# Wyjaśnienie
#
# Na początku tworzymy słownik pracowników - employees - zawierający dwóch pracowników - Pawła oraz Johna
#
# Następnie definiujemy funkcję add_entry przyjmującą trzy parametry 
# -d, czyli słownik, do którego dodajemy
# -key, czyli klucz pod jakim dodamy nową wartość
# -value, czyli wartość przechowywana pod nowym kluczem
#
# Funkcja najpierw wypisuje słownik, jaki jest przechowywany pod lokalną zmienną d. Referencja d wskazuje na ten sam obiekt,
# co przekazany do funkcji słownik employees. Jest więc wypisywana wartość słownika.
#
# Następnie do lokalnej zmiennej d - będącej cały czas referencją do tego samego słownika, co zmienna employees - dodajemy nowy wpis.
# Pod kluczem key będziemy przechowywać wartość value
#
# Po wykonaniu operacji dodawania nowego rekordu do słownika ponownie na ekran wypisywany jest obiekt, na który wskazuje referencja d - zmienna
# lokalna dla funkcji add_entry. Jest to słownik przechowujący trzy elementy o kluczach: Pawel, John oraz nowo dodana Martha
#
# Po zakończeniu wykonywania funkcji na ekran wypisywana jest wartość słownika przechowywana pod zmienną employees. Jest to równiez trzyelementowy słownik
# z kluczami Pawel, John i Martha.
#
# Stało się tak dlatego, ze obiekt słownika jest mutowalny. Wywołanie funkcji add_entry z parametrem employees powoduje, ze d zdefiniowane na
# liście argumentów funkcji add_entry staje się referencją do tego samego obiektu, co referencja employees.
#
# Do tego lokalnego d nie przypisujemy zadnego nowego obiektu. Dodanie elementu do słownika jest modyfikacją tego słownika w miejscu.
#
# Nie zmieniamy więc tego, na co wskazuje referencja d - ta cały czas odnosi się do tego samego słownika, co zmienna employees.
#
# Dodanie nowego elementu odbywa się więc w ramach tego samego obiektu, na który wskazuje zarówno referencja d jak i employees
#
# Dlatego właśnie na końcu po wypisaniu na ekran wartości słownika employees widzimy 3 elementy
#
# O referencji mozesz myśleć jak o 'zaczepie', bardziej formalnie jak o wskaźniku na dany obiekt. Wywołując funkcję z argumentem,
# nie przekazujesz obiektu samego w sobie, ale wskaźnik na ten obiekt. Jeśli employees wskazuje na słownik pod adresem XYZ,
# to przekazanie employees jako argumentu do add_entry sprawi, ze d równiez będzie wskazywało na obiekt XYZ i to ten obiekt
# będzie zmieniany, o ile do d wewnątrz funkcji add_entry nie przypiszemy innego obiektu.