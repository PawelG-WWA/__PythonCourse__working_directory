# ZADANIE
#
# Dana jest funkcja transfom_to_bio przyjmująca jako parametr obiekt person
#
# Dana jest równiez zmienna person, w której zdefiniowane są właściwości osoby
#
# Na końcu programu wypisujemy to, co zwraca funkcja transform_to_bio
#
# Napisz wyrazenie lambda zwracające taki sam wynik jak funkcja transform_to_bio
#
# Na końcu wypisz na ekranie wynik działania funkcji lambda.
#
# Wynik powinien być taki sam jak wywołanie print(transofrm_to_bio(person))

def transform_to_bio(person):
    return '%s is %s year(s) old. %s works as %s at %s' % (person["name"],
    person["age"],
    'He' if person["sex"] == 'm' else 'She',
    person["occupation"],
    person["company"]
    )


person = {
    'name': 'Pawel',
    'age': 40,
    'sex': 'm',
    'occupation': 'postman',
    'company': 'Main post'
}

print(transform_to_bio(person))

transform_to_bio_lambda = lambda person: '%s is %s year(s) old. %s works as %s at %s' % (person["name"],
    person["age"],
    'He' if person["sex"] == 'm' else 'She',
    person["occupation"],
    person["company"]
    )

print(transform_to_bio_lambda(person))