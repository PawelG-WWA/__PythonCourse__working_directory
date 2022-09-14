petents = ['Jack', 'Frank', 'Julie']


dictionary = {
    'Jack': {
        'Problems': [
            {
                'Name': 'Check engine',
                'Solved': False
            },
            {
                'Name': 'Change tyres',
                'Solved': False
            }
        ]
    },
    'Frank': {
        'Problems': [
            {
                'Name': 'Change tyres',
                'Solved': False
            },
        ]
    },
    'Julie': {
        'Problems': [
            {
                'Name': 'Check transmission',
                'Solved': False
            },
            {
                'Name': 'ABS not working',
                'Solved': False
            }
        ]
    }
}

while petents:

    print('Taking care of petent: %s' % petents[0])

    for p in dictionary[petents[0]]['Problems']:
        p['Solved'] = True

    petents = petents[1:len(petents)]

print(dictionary)


# Przebieg algorytmu
#
# 1. Przypisz do listy petents imiona petentów w kolejce
# 2. Stwórz słownik z problemami, z jakimi petenci przyszli do warsztatu.
#    -Słownik jest kilkakrotnie zagniedony - pierwszy poziom zawiera klucze, które są imionami petentów
#    -Kazdy petent posiada przypisaną listę problemów, z którymi przyszedł do warsztatu
#    -Kada lista składa się z jednoelementowych słowników z wartościami Name (nazwa problemu) i wartością Solved mówiącą, czy problem został naprawiony
# 3. Dopóki w kolejce znajdują się petenci, wykonuj pętlę while
# 4. Wypisz na ekran imię petenta, którego problemami będziemy się zajmować
# 5. Pobierz problem petenta z listy problemów petenta i przypisz go do nazwy p
# 6. Oznacz problem jako rozwiązany (p['Solved'] = True)
# ... wykonuj kroki 5 i 6 az wszystkie problemy zostana rozwiązane
# 7. Skróć listę petentów (kolejkę) poprzez przypisanie do listy petents wycinka obecnej listy petents
# 8. Wróć do kroku 3
# 9. Wypisz na ekranie listę petentów z ich problemami - wszystkie sa rozwiązane


# Dodatkowe objaśnienie
#
# Zapis petents = petents[1:len(petents)] oznacza, ze nalezy listę petents zastąpić listą petentów znajdujących się od
# miejsa pod indeksem 1 do miejsca pod indeksem len(petents), przy czym druga wartość jest wartością otwartą i nalezy
# pamiętać, ze indeksy w liście liczone są od 0
#
# Nasza lista wygląda następująco: petents = ['Jack', 'Frank', 'Julie']
#
# len(petents) zwraca 3
#
# zapis petents[1:len(petents)] jest więc równowazny z zapisem petents[1:3]
#
# listy są indeksowane od zera, a więc nasze elementy znajdują się pod indeksami:
# 0 - Jack
# 1 - Frank
# 2 - Julie
#
# zakres lista[x:y] jest zakresem prawostronnie otwartym, totez petents[1:3] pobierze elementy pod indeksami 1 oraz 2
# petents = petents[1:len(petents)] zwróci listę petents = ['Frank', 'Julie']
#
# teraz len(petents) wynosi 2, a elementy przechowywane są pod indeksami:
# 0 - Frank,
# 1 - Julie
#
# petents = petents[1:len(petents)] jest równowazne z zapisem petents[1:2]
#
# petents[1:2] zwróci listę petents = ['Julie']
#
# teraz len(petents) = 1, a elementy przechowywane sa pod następującymi indeksami:
# 0 - Julie
#
# Przy kolejnym przejściu wynik petents[1:len(petents)], gdzie len(petents) = 1, zwróci pustą listę
#
# Pusta lista jest tłumaczona przez interpreter Pythona jako False, dlatego warunek pętli while nie jest spełniony i pętla kończy swoje działanie