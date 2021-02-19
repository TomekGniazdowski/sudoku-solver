def okresl_kwadrat(tablica,rzad,kolumna):
    rzad/3
    kolumna/3


def czy_mozliwa_liczba(tablica,rzad,kolumna,kwadrat,wartosc):

    for i in range(9):
        if tablica[rzad][i] == wartosc and i != kolumna:
            return False

    for j in range(9):
        if tablica[j][kolumna] == wartosc and j != rzad:
            return False

    for n in range(3):
        for k in range(3):
            if tablica[int(rzad/3)*3+ n][int(kolumna/3)*3+k] == wartosc:
                return False


    return True

def rozwiarz_sudoku(tablica):

    for i in range(9):
        for j in range(9):
            if tablica[i][j] == 0:
                for wartosc in range(1,10):
                    if czy_mozliwa_liczba(tablica,i,j,1,wartosc):
                        tablica[i][j] = wartosc
                        rozwiarz_sudoku(tablica)
                        tablica[i][j] = 0
                return

    print("###########################")
    wyswietl(tablica)

def wyswietl(tablica):
    for i in range(9):
        print(tablica[i])

sudoku = [
[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]
]

wyswietl(sudoku)
rozwiarz_sudoku(sudoku)
