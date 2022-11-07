# ZADANIE
#
# Zmień kod w taki sposób, aby wynik wykonania ponizszego programu wynosił 12

x = 10

def enclosing_function():
    x = 11

    def nested_function():
        x = 12
    
    nested_function()
    print(x)

enclosing_function()
