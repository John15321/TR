# Implementacja modułów
import numpy as np
import sympy as sp
from sympy.interactive import printing
printing.init_printing(use_latex=True)


def Hurwitz_sp(Y):
    '''
    Funkcja sprawdzajaca stabilnosc transmitancji
    INPUT: obiekt sp.Function
    OUTPUT: stabilnosc 1 lub 0, macierz Hurwitza transmitancji(tex syndax)
    '''
    # zainicjowanie symboli
    s = sp.Symbol('s', real=True)
    # Y = sp.Function('Y')(s)
    M = sp.Function('M')(s)
    L = sp.Function('L')(s)
    # Transmitancja
    # Y = (1/((s+1)*(s+2)*(s+1)))
    L, M = sp.fraction(Y)  # podział na licznik i mianownik
    Ywspolczynniki = sp.Poly(M, s)
    Ywspolczynniki = Ywspolczynniki.all_coeffs()
    # rozpoczynam algorytm kryterium Hurwitza
    Ystopien = len(Ywspolczynniki)-1
    # tworze wektory potrzebne do stworzenia macierzy Hurwitza
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
    # deklaruje macierz Hurwitza jako macierz zer
    macierzHurwitza = sp.zeros(Ystopien, Ystopien)
    # algorytm zapusijacy macierz Hurwitza
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
    # algorytm sprawdzajacy czy wszystkie podwyznaczniki sa dodatnie
    stabilnoscHurwitza = 1
    macierzHurwitzaPomocnicza = macierzHurwitza
    for x in range(Ystopien):
        if macierzHurwitzaPomocnicza.det() <= 0:
            stabilnoscHurwitza = 0
        macierzHurwitzaPomocnicza.col_del(0)
        macierzHurwitzaPomocnicza.row_del(0)
    # jesli wszystkie podwyznaczniki sa dodatnie to zmienna stabilnoscHurwitza jest rowna 1, w przeciwnym wypadku jest rowna 0
    return stabilnoscHurwitza, sp.latex(macierzHurwitza)


# s = sp.Symbol('s', real=True)
# a, b = Hurwitz_sp((1/((s+1)*(s+2)*(s+1))))
