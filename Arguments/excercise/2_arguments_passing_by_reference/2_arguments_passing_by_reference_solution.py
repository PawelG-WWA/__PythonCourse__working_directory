# ZADANIE
#
# Dany jest słownik customers zawierający dwóch klientów w naszej nowej firmie - Pawła i Annę
#
# Napisz funkcję register_new_customer, która do istniejącej kolekcji klientów będzie dodawać
# nowych klientów naszej firmy
#
# Funkcja powinna przyjmować trzy argumenty - kolekcję (słownik), do której dodamy nowego klienta,
# klucz, pod jakim go zapiszemy oraz dane klienta.
#
# Następnie wywołaj funkcję, przekazując do niej argumenty - kolekcję (nasz słownik), identyfikator nowego
# klienta oraz obiekt new_customer (dane nowego klienta)
#  
# Na końcu wypisz zawartość słownika customers
#
# Czy przekazany do funkcji obiekt został zmieniony wewnątrz funkcji? Dlaczego?

customers = {
    'customer_1': {
        'name': 'Pawel', 'age': 33, 'order_history': [
            {'date': '2022-01-01', 'item': 't-shirt', 'price': 30},
            {'date': '2022-02-02', 'item': 'joggers', 'price': 70}
        ]},
    'customer_2': {'name': 'Anna', 'age': 21, 'order_history': [
            {'date': '2022-01-01', 'item': 'book', 'price': 10}
        ]}
}

new_customer = {'name': 'George', 'age': 50, 'order_history': []}

def register_new_customer(customer_registry, customer_id, customer_details):
    customer_registry[customer_id] = customer_details

register_new_customer(customers, 'customer_3', new_customer)

print(customers)

# Wyjaśnienie
#
# Argumenty przekazywane są do funkcji poprzez referencję do obiektu i przekazywane parametry
# przypisywane są zmiennym funkcji w kolejności od lewej do prawej.
# 
# Oznacza to, ze np wywołanie:
# register_new_customer(customers, 'customer_3', new_customer)
# 
# zmiennej customer_registry przypisze wskaźnik na ten sam obiekt, na który wskazuje globalna zmienna customers,
# zmiennej customer_id zostanie przypisany napis 'customer_3', a zmiennej new_customer zostanie przypisany wskaźnik (referencja)
# na ten sam obiekt, na który wskazuje zmienna new_customer zdefiniowana globalnie
#
# Wywołanie więc linii:
# customer_registry[customer_id] = customer_details
# 
# zonacza, ze do tego samego obiektu, na który wskazują dwie zmienne - customers oraz customer_registry wewnątrz funkcji -
# zostanie dodany nowy klient przechowywany pod zmienną new_customer oraz customer_details.
#
# ODPOWIEDŹ: Tak, kolekcja stworzona na zewnątrz funkcji register_new_customer zostanie zmieniona ze względu
# na to, ze słownik jest obiektem mutowalnym, a zmienne przekazywane są do funkcji przez referencje
# do obiektów, co oznacza, ze jeśli wewnątrz funkcji nie przypiszemy do zadnej z przekazanych zmiennych
# nowej wartości, to zmienne te będą wskazywałe na te same obiekty, na które wskazują zmienne przekazane
# do funkcji 