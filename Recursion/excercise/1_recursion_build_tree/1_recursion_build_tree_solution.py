# Zadania z rekurencji są zazwyczaj bardzo trudne i wymagają duzo wysiłku intelektualnego
#
# Oczywiście, mógłbym napisać zadanie polegające na wyznaczeniu ciągu fibonnaciego,
# ale takich prostych przykładów jest masa, a podstawy zostały zaprezentowane na przykładach
# w części opisowej w folderze Recursion. Mozesz do nich wrócić i spróbować odtworzyć ich kod,
# traktując go jako ćwiczenia wprowadzające do bardziej wymagających zadań.
#
# Pamiętaj, ze obecnie masz mnóstwo pomocy naukowych - nie bój się korzystać z zasobów internetu,
# podpowiedzi ChatGPT i ksiązek.
# 
# Mozesz takze poprosić o wyjaśnienie na naszej grupie Discord dostępnej w ramach subskrypcji Premium.
#
# 
# Drzewa posiada korzeń oznaczone w tym przypadku cyfrą 0
# Element, od którego wychodzą krawędzie w dół nazywamy rodzicem. Element, do którego dochodzą krawędzie od góry
# nazywamy dzieckiem. Ostatnie dziecko, od którego nie wychodzą zadne krawędzie w dół to liście drzewa.
#
# Na potrzeby tego zadania drzewo zdefiniujemy jako listę liczb całkowitych.
#
# # Pierwszy element listy zawsze odpowiada temu, co znajduje po lewej stronie rodzica. Drugi element odpowiada temu,
# co znajduje się po prawej stronie rodzica.
#
# Zapis [1, 2] oznaczałby, ze po lewej stronie zera znajdzie się 1, a po prawej 2:
#    0
#   / \
#  1   2
#
# Zapis [[1, [2]]] oznacza, ze po lewej stronie 0 znajduje się 1, po lewej stronie 1 znajduje się 2, a po prawej stronie 0
# nie ma nic (zwróć uwagę, ze tablica najwyzszego poziomu jest jednoelementowa, a więc definiuje tylko element z lewej strony)
#
#     0
#    /
#   1
#  /
# 2
#
# Zapis [[1, [2, 3]], [4]] oznacza, ze po lewej stronie 0 jest 1, po prawej stronie 0 jest 4, po lewej stronie 1 jest 2,
# a po prawej stronie 1 jest 3
#
#          0
#         / \
#        1   4
#       / \
#      2   3
#
# ZADANIE
# Ponizej zaprezentowano trukturę drzewa:
#
#          0
#        /   \
#       1     4
#      / \   / \
#     2   3 5   6
#              /
#             7
# Ponizsza lista lista jest definicją drzewa. Nie jest to zapis prosty, więc spróbuj poświęcić chwilę na jego zrozumienie
# [[1, [2]], [3, [4, [5, [6]]]]]
#
# Napisz funkcję pre_order, ktory poprzez rekurencyjne przejście drzewa wypisze jego elementy znajdujące się w pierwszej kolejności po lewej stronie
# korzenia i gałęzi, a w drugiej kolejności po prawej stronie korzenia i gałęzi:
#
# Oczekiwany rezultat:
# 0, 1, 2, 3, 4, 5, 6, 7

#tree_data = []
#tree_data = [[1], [2]]
tree_data = [[[1], [[2], [3]]], [[4], [[5], [[6], [7]]]]]


def pre_order(tree_data):
    if len(tree_data) == 0:
        return

    if len(tree_data) == 1:
        print(tree_data[0])
        return
    
    pre_order(tree_data[0])
    pre_order(tree_data[1])

    


print(0)
pre_order(tree_data)