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

if selected_symptom_number.isnumeric() and int(selected_symptom_number) > 0 and int(selected_symptom_number) <= len(symptoms):
    selected_symptom = symptoms[int(selected_symptom_number)-1]

    patients_drugs.append(drugs_for_symptoms[selected_symptom])

    if (selected_symptom == 'headache'):
        patients_drugs.append(drugs_for_symptoms['weakness'])

else:
    print('Unknown symptom')

print(patients_drugs)