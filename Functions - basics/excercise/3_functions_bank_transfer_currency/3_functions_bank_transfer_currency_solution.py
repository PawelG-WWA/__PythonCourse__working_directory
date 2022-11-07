# ZADANIE
#
# W tym zadaniu wykorzystaj rozwiązanie z zadania drugiego
#
# Dopisz jeszcze jedną funkcję, która skorzysta ze słownika currencies przechowującego kursy walut
# 
# Funkcja ta powinna pobrać kurs walut, obliczyś przelewaną kwotę
# i wykorzystać napisane przez Ciebie wcześniej funkcje do wykonania przelewu
#
# Zastanów się, jak napisać nową funkcję bez kopiowania kodu

currencies = { 'USD': 4.5, 'EUR': 4.6, 'CHF': 4.8 }

def transfer(account_from, account_to, amount):
    if is_transfer_possible(account_from, amount):
        account_from -= amount
        account_to += amount
    
    return (account_from, account_to)

def is_transfer_possible(account, amount):
    if amount > account:
        print('Na koncie brakuje środków')
        return False
    return True

def transfer_in_foreign_currency(currency, amount, account_from, account_to):
    final_transfer_amount = currencies[currency] * amount
    
    return transfer(account_from, account_to, final_transfer_amount)

account_a = 100
account_b = 50

(account_a, account_b) = transfer_in_foreign_currency('USD', 10, account_a, account_b)

print(account_a)
print(account_b)