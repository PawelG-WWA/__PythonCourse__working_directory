teams = ['Barcelona', 'Manchester', 'Milan', 'Munich']
matches = [x + ' vs. ' + y for x in teams for y in teams if x != y]

for match in matches:
    print(match)