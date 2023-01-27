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

def add_employee(name, age, occupation, salary, department):
    global id
    id += 1
    employee = {
        'id': id,
        'name': name,
        'age': age,
        'occupation': occupation,
        'salary': salary,
        'department': department
    }

    employees.append(employee)

add_employee(name='John', age=22, occupation='programmer', salary=1000, department='IT')
add_employee(department='Art & Design', age=30, occupation='desogner', salary=1000, name='Paul')
add_employee(department='Art & Design', occupation='musician', age=33, salary=1000, name='George')

print(employees)


# DODATKOWE WYJAŚNIENIE
#
# Mam nadzieję, ze pamiętałeś o uzyciu instrukcji global, aby odnieść się do globalnie stworzonej zmiennej id, do której
# wewnątrz funkcji add_employee z kazdym wywołaniem tej funkcji przypisujemy nową wartość.
#
# Jeśli wywołasz funkcję add_employee jak powyzej - kilkakrotnie - zamieniając kolejność słów kluczowych na liście parametrów za kazdym razem,
# nie będzie to miało zadnego znaczenia dla przypisania wartości do parametrów lokalnych funkcji.
#
# Przypisujemy bowiem kolejne wartości do nazw parametrów, a nie - jak w domyślnym zachowaniu - w kolejności od lewej do prawej