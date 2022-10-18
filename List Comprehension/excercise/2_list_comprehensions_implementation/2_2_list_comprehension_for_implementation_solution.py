# ZADANIE
#
# W miejscu trzykropka zaimplementuj pętlę for, która do listy words_first_letters doda dokładnie takie same elementy
# jak implementacja listy składanej w linii:
#
# words_first_letters = [w[0:1] for w in words]
#
# Są to pierwsze litery słów przechowywanych w liście words

words = ['abc', 'xyz', 'qwe']

words_first_letters = [w[0:1] for w in words]

print(words_first_letters)

words_first_letters = []
#... 
for w in words:
    words_first_letters.append(w[0:1])

print(words_first_letters)