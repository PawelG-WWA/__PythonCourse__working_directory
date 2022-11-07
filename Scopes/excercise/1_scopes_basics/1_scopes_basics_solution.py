# ZADANIE
#
# Dany jest słownik customers, którego klucze to imiona klientów, a wartości kluczy to dane dotyczące wykupionej subskrypcji
#
# Na przykład wpis 'Pawel': { 'plan': 'Regular', 'is_active': True } oznacza, ze klient Pawel posiada wykupiony plan
# na poziomie Regular i plan ten jest aktywny (flaga is_active)
#
# Napisz funkcję add_customer, która do słownika customers doda klienta o imieniu i danych przekazanych jako argument
# 
# Niech dodawany klient ma na imię np. John oraz niech ma wykupiony plan Premium i niech ten plan będzie aktywny
#
# W jakim zakresie znajduje się słownik customers?
#
# Przykładowy wynik działania programu:
# {'Pawel': {'plan': 'Regular', 'is_active': True}, 'Jessica': {'plan': 'Premium', 'is_active': False}, 'John': {'plan': 'Premium', 'is_active': True}}

customers = {
    'Pawel': { 'plan': 'Regular', 'is_active': True },
    'Jessica': { 'plan': 'Premium', 'is_active': False }
} 

def add_customer(customer_name, customer_data):
    customers[customer_name] = customer_data

add_customer('John', { 'plan': 'Premium', 'is_active': True })

print(customers)


# Wyjaśnienie
#
# Słownik customers znajduje się w zakresie globalnym
#
# Oznacza to, ze w funkcji add_customer mozemy bezpośrednio uzyć referencji do tego słownika uzywając zmiennej customers
#
# Jako, ze nie próbujemy stworzyć nowego słownika wewnątrz funkcji, a jedynie odnosimy się do jakiejś nazwy,
# Python zacznie przeszukiwać zakresy - od lokalnego, gdzie nazwa customers nie istnieje, przez zawierający, którego w ogóle nie ma,
# az po globalny, gdzie nazwa customers zostanie odnaleziona, poniewaz to tam miało miejsce stworzenie tej zmiennej (przypisanie do niej wartości)