people = {
    'Paul': ['Ann', 'Frank'],
    'Ann': ['Paul'],
    'Frank': ['Paul', 'Kate'],
    'Martin': [],
    'Kate': ['Frank']
}

for person in people:
    print('%s is in relation with: ' % person, end='')

    for relationship in people[person]:
        print(relationship, end=', ')

    print('\n')
