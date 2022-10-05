# ZADANIE
#
# Uzupełnij pola _gap_1-8.
#
# W polach _gap_1-4 do pobrania iteratora i kolejnych elementów uzyj metody listy i metody iteratora
#
# W polach _gap_5-8 do pobrania iteratora i kolejnych elementów uzyj wbudowanych metod Pythona

words = ['one', 'two', 'three']

words_iterator = words.__iter__()
print(words_iterator.__next__())
print(words_iterator.__next__())
print(words_iterator.__next__())

print()

words_iterator = iter(words)
print(next(words_iterator))
print(next(words_iterator))
print(next(words_iterator))
