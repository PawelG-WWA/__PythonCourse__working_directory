words = ['jeden', 'dwa', 'trzy']

for x in range(len(words)-1, -1, -1):
    print(words[x])

# Przebieg algorytmu:
#
# 1. Do zmiennej o nazwie words przypisz listę trójelementową ['jeden', 'dwa', 'jeden']
# 2. Wygeneruj zbiór liczb od długości listy pomniejszonej o jeden, do -1, odejmując od kazdej kolejnej liczby 1 - lista wygenerowanych liczb: [2, 1, 0]
# 3. Weź element z zakresu i przypisz do x - x = 2
# 4. Wypisz na ekran element listy words na indeksie x - words[2] = trzy
# 5. Weź element z zakresu i przpisz do x - x = 1
# 6. Wypisz na ekran element listy words na indeksie x - words[1] = dwa
# 7. Weź element z zakresu i przpisz do x - x = 0
# 6. Wypisz na ekran element listy words na indeksie x - words[0] = jeden
#
#
# Wyjaśnienie:
#
# Funkcja len(words) zwraca ilość elementów liście, a więc len(words) = 3.
#
# My chcemy operować na indeksach listy, a maksymalnym indeksem listy jest indeks 2 (lista ma 3 elementy, przyporządkowane indeksom 0, 1 i 2)
#
# Musimy więc pomniejszyć wynik len(words) o jeden, poniewaz chcemy pobierać elementy listy od końca, a więc od indeksu 2
#
# Drugi argument funkcji range to -1. Range generuje zakres prawostronnie otwarty, a więc range(x, y) tworzy zakres od x włącznie do y, ale bez y, np:
# range(0, 4) zwróci: 0, 1, 2, 3.
#
# Naszym najmniejszy indeksem w liście zawsze jest 0, dlatego chcemy wygenerować zakres do 0, a skoro range jest prawostronnie otwarty,
# wskazujemy, ze chcemy generować wartości do -1, ale bez -1.
#
# Trzeci argument funkcji range wskazuje, jaki ma być krok generacji. Od kadej wygenerowanej liczby kolejna liczba ma być mniejsza o 1,
# dlatego trzeci argument to -1
#
# wynik range(len(words)-1, -1, -1) to zakres 2, 1, 0, poniewaz:
#   -len(words) = 3, a więc len(words)-1 = 2
#   -generujemy do -1, a więc od 2 do -1 ale bez -1
#   -kazda kolejna wygenerowana liczba startując od 2 będzie mniejsza od poprzedniej o 1