'''
W tym pliku zdefiniowane sa funkcje potrzebne do kryterium Hurwitza
'''
import sympy as sp
import numpy as np
sp.init_printing(use_latex=True)
sp.init_printing(use_unicode=True)
s = sp.Symbol('s', real=True)
k = sp.Symbol('k', real=True)


def Hurwitz_sp(Yk):
    '''
    Funkcja sprawdzajaca stabilnosc transmitancji
    INPUT: obiekt sp.Function
    OUTPUT: macierz Hurwitza transmitancji(tex syndax), 
            wektor skladajacy się z wartosci podwyznacznikow macierzy
    '''
    # Zainicjowanie symboli
    M = sp.Function('M')(s)
    L = sp.Function('L')(s)
    Y=sp.Function('Y')(s)
    Y=Yk
    L, M = sp.fraction(Y)  # podział na licznik i mianownik
    Ywspolczynniki = sp.Poly(M, s)
    Ywspolczynniki = Ywspolczynniki.all_coeffs()
    # Rozpoczynam algorytm kryterium Hurwitza
    Ystopien = len(Ywspolczynniki)-1
    # Tworze wektory potrzebne do stworzenia macierzy Hurwitza
    pTabParz = sp.Matrix([[]])
    pTabNParz = sp.Matrix([[]])
    pm = 0
    pn = 0
    for x in range(Ystopien):
        pm = x*2
        pn = x*2+1
        if pm <= Ystopien:
            pTabParz = pTabParz.col_insert(x, sp.Matrix([Ywspolczynniki[pm]]))
        else:
            pTabParz = pTabParz.col_insert(x, sp.Matrix([0]))
        if pn <= Ystopien:
            pTabNParz = pTabNParz.col_insert(
                x, sp.Matrix([Ywspolczynniki[pn]]))
        else:
            pTabNParz = pTabNParz.col_insert(x, sp.Matrix([0]))
    # Deklaruje macierz Hurwitza jako macierz zer
    macierzHurwitza = sp.zeros(Ystopien, Ystopien)
    # Algorytm zapusijacy macierz Hurwitza
    parzyste = False
    if Ystopien == 0:
        macierzHurwitza = (sp.ones(1, 1))/Y
    else:
        for x in range(Ystopien):
            if(parzyste == False):
                macierzHurwitza.row_del(x)
                macierzHurwitza = macierzHurwitza.row_insert(x, pTabNParz)
                pTabNParz = pTabNParz.col_insert(0, sp.Matrix([0]))
                pTabNParz.col_del(Ystopien)
                parzyste = (not parzyste)
            elif(parzyste == True):
                macierzHurwitza.row_del(x)
                macierzHurwitza = macierzHurwitza.row_insert(x, pTabParz)
                pTabParz = pTabParz.col_insert(0, sp.Matrix([0]))
                pTabParz.col_del(Ystopien)
                parzyste = (not parzyste)
    # Algorytm sprawdzajacy czy wszystkie podwyznaczniki sa dodatnie
    macierzHurwitzaPomocnicza = macierzHurwitza.copy()
    wyznacznikiHurwitza = []
    for x in range(Ystopien):
        wyznacznikiHurwitza.append(macierzHurwitzaPomocnicza.det())
        if macierzHurwitzaPomocnicza.shape[0] > 0:
            macierzHurwitzaPomocnicza.col_del(
                macierzHurwitzaPomocnicza.shape[0]-1)
            macierzHurwitzaPomocnicza.row_del(
                macierzHurwitzaPomocnicza.shape[0]-1)
        # Jesli wszystkie podwyznaczniki sa dodatnie to zmienna stabilnoscHurwitza jest rowna 1,
        # w przeciwnym wypadku jest rowna 0
    return str(sp.latex(macierzHurwitza)), str(sp.latex(wyznacznikiHurwitza))
