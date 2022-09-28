numbers = [1, 2, 3]

next_number = next(numbers)
#next_number = numbers.__next__()

# Przebieg algorytmu
#
# 1. Do zmiennej o nazwie numbers przypisz listę cyfr 1, 2, 3 - numbers = [1, 2, 3]
# 2. Wykonaj na liście wbudowaną funkcję Pythona next, która wykorzystuje iterator do pobierania kolejnego elementu
# 
# Wynik algorytmu:
# TypeError: 'list' object is not an iterator - obiekt typu 'list' nie jest iteratorem
#
# Dodatkowe wyjaśnienie
#
# obiekt list nie jest iteratorem - jest obiektem iterowalnym
#
# Jeśli odkomentujesz linię nr 4 usuwając znak # i zakomentujesz linię nr 3 dodając znak # na samym początku wiersza,
# a następnie uruchomisz program, zobaczysz na ekranie błąd:
# AttributeError: 'list' object has no attribute '__next__'
#
# Oznacza on, ze obiekt typu list nie posiada atrybutu '__next__' - nie posiada go, bo taki atrybut posiada tylko,
# iterator, natomiast list nie jest iteratorem, jest obiektem iterowalnym
#
# Lista moze zwrócić iterator, ale nalezy uzyc funkcji wbudowanej iter - iter(numbers) lub wywołać
# funkcję __iter__() listy - numbers.__iter__(), aby pozyskać obiekt iteratora i dopiero na tym obiekcie będzie
# mozna wywoływać funkcję wbudowaną next lub funkcję __next__ tego obiektu, aby dokonać iteracji