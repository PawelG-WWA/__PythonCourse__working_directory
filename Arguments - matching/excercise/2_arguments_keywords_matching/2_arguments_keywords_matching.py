# ZADANIE
#
# Dane są dwie zmienne globalne - liczba całkowita id oraz lista pracowników o nazwie employees
#
# Napisz funkcję add_employee, która, będzie przyjmować następujące parametry: name, age, occupation, salary, department
# 
# Następnie utwórz nowego pracownika - wykorzystaj do tego słownik. Kluczom name, age, occupation, salary i department przypisz
# wartości przekazane jako argumenty funkcji.
#
# Dodatkowo, wykorzystaj w środku funkcji add_employee zmienną globalną id tak, aby id równiez było parą klucz-wartość
# w słowniku employee. Za kazdym razem, gdy będziesz wywoływał funkcję add_employee, zwiększ id o 1, aby kazdy pracwonik dodany do listy
# employees posiadał swój id. Jeśli dodasz jednego pracownika, będzie on miał id = 1, jeśli dodasz drugiego, będzie miał id = 2 itd.
#
# W funkcji add_employee dodaj do listy employees nowego pracownika.
#
# Wywołaj kilk arazy funkcję add_employee przekazując parametry poprzez słowa kluczowe.
#
# Z kazdym wywołaniem zmień kolejność słów kluczowych - czy ma to jakieś znaczenie dla ogólnego działania programu?

id = 0
employees = []

# Tu napisz swój kod

print(employees)
