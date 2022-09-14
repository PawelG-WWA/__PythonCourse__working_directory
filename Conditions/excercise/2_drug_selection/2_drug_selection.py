# ZADANIE
#
# Dane:
# słownik symptomów choroby wraz z lekami dla tych symptomów, lista symptomów spośród których wybiera uzytkownik
#
# Cel:
# Napisz program, którzy sprawdzi, czy dane wprowadzone przez uytkownika
# to liczba oraz czy podana liczba jest w zakresie ilości symptomów do wyboru (są cztery symptomy, więc
# wpisanie np. numeru 5 albo -1 powinno skutkować wypisaniem na ekran np. wiadomości 'Unknown symptom').
# Jeśli warunek jest spełniony, pobierz ze słownika lek dla danego symptomu i wstaw ten lek do listy
# patients_drugs. Dodatkowo, jeśli wybrany symptom to 'headache', dodaj do listy patients_drugs
# lek na 'weakness', pobierając go ze słownika.

drugs_for_symptoms = {
    'headache': 'Drug for headache',
    'throatache': 'Drug for throatache',
    'katar': 'Drug for katar',
    'weakness': 'Drug for weakness'
}

symptoms = ['headache', 'throatache', 'katar', 'weakness']
selected_symptom_number = input('Select a symptom:\n1: headache\n2: throatache\n3: katar\n4: weakness\n')
patients_drugs = []
selected_drug = None
