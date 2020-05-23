'''
TODO:
0. Do hurtwiza wklep mianownik "L_K*L_G+M_K*M_G".
Jest to rozwinięty mianownik K_Z,
więc hurtwiz w tym momencie nam wypluje stabilnosc petli zamknietej

1. Mamy petle otwarta i zamknieta
    1.1 Wyswietl transmitancje dla obu petli nazwij K_Z i K_O

2. Sprawdzamy stabilnosc K*G Hurwitz'em

3. Rysujemy Nyquista, dla 1+K*G

4. Zależnie od stabilności K*G oceniamy na podstawie 1+K*G, oceniamy
stabilnosc całego układu zamknietego
'''
import os
import numpy as np
import pandas as pd
import matplotlib as plt
import sympy as sp
# Ustawiamy s oraz k w SymPy
s = sp.Symbol('s', rational=True)
k = sp.Symbol('k', rational=True, real=True)

# Nasze transmitancje i ich postacie w latexu
K_a = 1/((s+1)*(s+2))
K_b = k
K_c = (s+2)/((s+1)*(s+2))
K_d = 1/(s**2+4*s+5)

LATEX_K_a = str(sp.latex(K_a))
LATEX_K_b = str(sp.latex(K_b))
LATEX_K_c = str(sp.latex(K_c))
LATEX_K_d = str(sp.latex(K_d))

G_a = k
G_b = 1/((s+1)*(s+2))
G_c = 1/(s+3)
G_d = 1/(s+3)


LATEX_G_a = str(sp.latex(G_a))
LATEX_G_b = str(sp.latex(G_b))
LATEX_G_c = str(sp.latex(G_c))
LATEX_G_d = str(sp.latex(G_d))


# Podział na licznik i mianownik (symbolicznie)
L_K_a, M_K_a = sp.fraction(K_a)
L_K_b, M_K_b = sp.fraction(K_b)
L_K_c, M_K_c = sp.fraction(K_c)
L_K_d, M_K_d = sp.fraction(K_d)

L_G_a, M_G_a = sp.fraction(G_a)
L_G_b, M_G_b = sp.fraction(G_b)
L_G_c, M_G_c = sp.fraction(G_c)
L_G_d, M_G_d = sp.fraction(G_d)

# Hurwitz, dla kazdego przykladu, dla petli zamknietej
# Dostajemy booleana czy jest stabilny czy nie
# oraz wersje latexowa(string) K_z
# K_Z_STAB_a, K_Z_LATEX_a = Hurwitz_sp(L_K_a*L_G_a+M_K_a*M_G_a)
# K_Z_STAB_b, K_Z_LATEX_b = Hurwitz_sp(L_K_b*L_G_b+M_K_b*M_G_b)
# K_Z_STAB_c, K_Z_LATEX_c = Hurwitz_sp(L_K_c*L_G_c+M_K_c*M_G_c)
# K_Z_STAB_d, K_Z_LATEX_d = Hurwitz_sp(L_K_d*L_G_d+M_K_d*M_G_d)


# Licznik i Mianownik K'atych (jako listy wspolczynnikow przy s'ach)
L_KG_LIST_a, M_KG_LIST_a = [[float(i) for i in sp.Poly(
    i, s).all_coeffs()] for i in (K_a*G_a).replace(k, 1).as_numer_denom()]
L_KG_LIST_b, M_KG_LIST_b = [[float(i) for i in sp.Poly(
    i, s).all_coeffs()] for i in (K_b*G_b).replace(k, 1).as_numer_denom()]
L_KG_LIST_c, M_KG_LIST_c = [[float(i) for i in sp.Poly(
    i, s).all_coeffs()] for i in (K_c*G_c).replace(k, 1).as_numer_denom()]
L_KG_LIST_d, M_KG_LIST_d = [[float(i) for i in sp.Poly(
    i, s).all_coeffs()] for i in (K_d*G_d).replace(k, 1).as_numer_denom()]


'''
Tworzymy plik txt, ktory bedzie handlerem wyniku stabilnosci ktory otrzymamy od matlaba. 
Dodatkowo za pomoca modulu os wykonamy odpowiednie, dla systemu komendy, aby matlab wyprodukowal nam 
wysokiej jakosci plot'y Nyquista
'''
if os.path.exists("stabs.txt"):
      os.remove("stabs.txt")
f = open("stabs.txt", "w+")
f.close()

# dlmwrite('./stabs.txt',[1 2 3 4],'delimiter',',')
if os.name == "nt":  # if is Windows
    print("Detected OS: Windows")
    COMMAND_START = "matlab -nodesktop -r \"nyquist_plot_with_k("+str(repr(L_KG_LIST_a))+","+str(
        repr(M_KG_LIST_a))+"," + "\'"+"a"+"\');nyquist_plot_with_k("+str(repr(L_KG_LIST_b))+","+str(
        repr(M_KG_LIST_b))+"," + "\'"+"b"+"\');nyquist_plot("+str(repr(L_KG_LIST_c))+","+str(
        repr(M_KG_LIST_c))+"," + "\'"+"c"+"\');nyquist_plot("+str(repr(L_KG_LIST_d))+","+str(
        repr(M_KG_LIST_d))+"," + "\'"+"d"+"\');exit;\""

elif os.name == "posix":  # if is Linux
    print("Detected OS: Linux")
    COMMAND_START = "/usr/local/MATLAB/R2018a/bin/matlab -softwareopengl -nodesktop -r \"nyquist_plot_with_k("+str(repr(L_KG_LIST_a))+","+str(
        repr(M_KG_LIST_a))+"," + "\'"+"a"+"\');nyquist_plot_with_k("+str(repr(L_KG_LIST_b))+","+str(
        repr(M_KG_LIST_b))+"," + "\'"+"b"+"\');nyquist_plot("+str(repr(L_KG_LIST_c))+","+str(
        repr(M_KG_LIST_c))+"," + "\'"+"c"+"\');nyquist_plot("+str(repr(L_KG_LIST_d))+","+str(
        repr(M_KG_LIST_d))+"," + "\'"+"d"+"\');exit;\""
else:
    print("Error: Deteced OS: Not known!")
    raise SystemExit

print("Command/s to be run: \n"+COMMAND_START)
os.system(COMMAND_START)


df = pd.read_csv("stabs.txt", header=None)
STABS_KG = df[0].to_list()
STABS_1_KG = df[1].to_list()

# if os.path.exists("stabs.txt"):
#       os.remove("stabs.txt")
