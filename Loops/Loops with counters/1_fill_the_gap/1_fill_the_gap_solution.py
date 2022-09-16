# ZADANIE
#
# W miejsce _gap_1 wstaw funkcję range, któa wygeneruje co drugą liczbę od 0 do 50 włącznie
#
# W miejsce _gap_2 wstaw funkcję range, która będzie zwracała indeksy listy numbers od końca, co trzy, zaczynając od ostatniego
#
# W miejsce _gap_3 wstaw instrukcję, która pozwoli wypisać element na danym indeksie w liście numbers (pamiętaj, ze x w nagłówku for to indeks)
# 
# Przykładowy wynik dla wygenerowanej listy numbers = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]:
#50
#44
#38
#32
#26
#20
#14
#8
#2

numbers = list(range(0, 51, 2))

for x in range(len(numbers)-1, -1, -3):
    print(numbers[x])


# Wyjaśnienie:
#
# range samo w sobie nie zwraca listy, ale obiekt iterowalny. Aby stworzyć listę z zakresu zdefiniowanego przez range,
# musimy opakować wywołanie tej funkcji w funkcję list, która przeiteruje po wszystkich elementach z zakresu
# zdefiniowanego w range i stworzy listę z liczb wchodzących w skład tego zakresu.