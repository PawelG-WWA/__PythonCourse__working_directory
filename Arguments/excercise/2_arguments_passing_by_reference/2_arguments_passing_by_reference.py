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