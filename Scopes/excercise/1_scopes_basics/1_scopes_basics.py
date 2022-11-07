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

customers = {
    'Pawel': { 'plan': 'Regular', 'is_active': True },
    'Jessica': { 'plan': 'Premium', 'is_active': False }
}

# Napisz rozwiązanie tutaj

print(customers)