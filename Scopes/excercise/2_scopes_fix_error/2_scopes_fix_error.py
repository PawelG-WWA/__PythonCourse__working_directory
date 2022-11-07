# ZADANIE
#
# Znajdź oraz napraw błąd w ponizszym kodzie

recipes = {
    'scrambled eggs': { 'eggs': 3, 'ham': '10g', 'tomato': '2 slices' },
    'tomato soup': { 'mirepoix': 1, 'tomato': '750g', 'cream': '100ml', 'pork bone': 1}
}

def add_recipe(meal, ingredients):
    recipes = recipes + { meal: ingredients }

add_recipe('banana bread', { 'banana': 3, 'flour': '350g', 'egg': 1, 'sugar': '100g', 'butter': '70g', 'salt': '1x teaspoon', 'sodium': '1x teaspoon' })

print(recipes)