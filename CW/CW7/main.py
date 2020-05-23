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
import subprocess
import numpy as np
import pandas as pd
import matplotlib as plt
import sympy as sp
import hurwitz as hr

# Tworzymy plik do latexa, ale na poczatku sprawdzamy czy plik o takiej samej nazwie istnieje
# jak tak to go usuwamy

# Ustawiamy s oraz k w SymPy
s = sp.Symbol('s', rational=True)
k = sp.Symbol('k', rational=True, real=True)

# Nasze transmitancje i ich postacie w latexu
K_a = 1/((s+1)*(s+2))
K_b = k
K_c = (s+2)/((s+1)*(s+2))
K_d = 1/(s**2+4*s+5)

LATEX_K_LIST = [str(sp.latex(K_a)), str(sp.latex(K_b)),
                str(sp.latex(K_c)), str(sp.latex(K_d))]
K_LIST = [(K_a), (K_b),
          (K_c), (K_d)]
G_a = k
G_b = 1/((s+1)*(s+2))
G_c = 1/(s+3)
G_d = 1/(s+3)

G_LIST = [(G_a), (G_b),
          (G_c), (G_d)]
LATEX_G_LIST = [str(sp.latex(G_a)), str(sp.latex(G_b)),
                str(sp.latex(G_c)), str(sp.latex(G_d))]


# Podział na licznik i mianownik (symbolicznie)
L_K_a, M_K_a = sp.fraction(K_a)
L_K_b, M_K_b = sp.fraction(K_b)
L_K_c, M_K_c = sp.fraction(K_c)
L_K_d, M_K_d = sp.fraction(K_d)

K_L_LIST = []
K_M_LIST = []
for x in K_LIST:
    K_L_LIST.append(sp.fraction(x)[0])
    K_M_LIST.append(sp.fraction(x)[1])

L_G_a, M_G_a = sp.fraction(G_a)
L_G_b, M_G_b = sp.fraction(G_b)
L_G_c, M_G_c = sp.fraction(G_c)
L_G_d, M_G_d = sp.fraction(G_d)

G_L_LIST = []
G_M_LIST = []
for x in G_LIST:
    G_L_LIST.append(sp.fraction(x)[0])
    G_M_LIST.append(sp.fraction(x)[1])

# Kazde K_Z jako latex w liscie
LATEX_K_Z_LIST = [str(sp.latex((L_K_a*M_G_a)/(L_K_a*L_G_a+M_K_a*M_G_a))), str(sp.latex((L_K_b*M_G_b/(L_K_b*L_G_b+M_K_b*M_G_b)))),
                  str(sp.latex((L_K_c*M_G_c)/(L_K_c*L_G_c+M_K_c*M_G_c))), str(sp.latex((L_K_d*M_G_d/(L_K_d*L_G_d+M_K_d*M_G_d))))]
# Kazde K_Z jako expr
K_Z_LIST = []
for x in range(4):
    K_Z_LIST.append((K_L_LIST[x]*G_M_LIST[x])/(K_L_LIST[x]*G_L_LIST[x]+K_M_LIST[x]*G_M_LIST[x]))
# Dzieli K_Z na mianownik i licznik
K_Z_L_LIST=[]
K_Z_M_LIST=[]
for x in K_Z_LIST:
    K_Z_L_LIST.append(sp.fraction(x)[0])
    K_Z_M_LIST.append(sp.fraction(x)[1])
# Hurwitz, dla kazdego przykladu, dla petli zamknietej
# Dostajemy booleana czy jest stabilny czy nie
# oraz wersje latexowa(string) K_z
K_Z_H_MATRIX = []
K_Z_H_DETS = []
for x in K_Z_LIST:
    K_Z_H_MATRIX.append(hr.Hurwitz_sp(x)[0])
    K_Z_H_DETS.append(hr.Hurwitz_sp(x)[1])
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
if os.path.exists("end_of_mat.txt"):
    os.remove("end_of_mat.txt")

f = open("stabs.txt", "w+")
f.close()
END_NAME_FILE = "end_of_mat.txt"
# dlmwrite('./stabs.txt',[1 2 3 4],'delimiter',',')
if os.name == "nt":  # if is Windows
    print("Detected OS: Windows")
    COMMAND_START = "cmd /c matlab -nodesktop -r \"nyquist_plot_with_k("+str(repr(L_KG_LIST_a))+","+str(
        repr(M_KG_LIST_a))+"," + "\'"+"a"+"\');nyquist_plot_with_k("+str(repr(L_KG_LIST_b))+","+str(
        repr(M_KG_LIST_b))+"," + "\'"+"b"+"\');nyquist_plot("+str(repr(L_KG_LIST_c))+","+str(
        repr(M_KG_LIST_c))+"," + "\'"+"c"+"\');nyquist_plot("+str(repr(L_KG_LIST_d))+","+str(
        repr(M_KG_LIST_d))+"," + "\'"+"d"+"\');finish(\'"+END_NAME_FILE+"\');exit;\""

elif os.name == "posix":  # if is Linux
    print("Detected OS: Linux")
    COMMAND_START = "/usr/local/MATLAB/R2018a/bin/matlab -softwareopengl -nodesktop -r \"nyquist_plot_with_k("+str(repr(L_KG_LIST_a))+","+str(
        repr(M_KG_LIST_a))+"," + "\'"+"a"+"\');nyquist_plot_with_k("+str(repr(L_KG_LIST_b))+","+str(
        repr(M_KG_LIST_b))+"," + "\'"+"b"+"\');nyquist_plot("+str(repr(L_KG_LIST_c))+","+str(
        repr(M_KG_LIST_c))+"," + "\'"+"c"+"\');nyquist_plot("+str(repr(L_KG_LIST_d))+","+str(
        repr(M_KG_LIST_d))+"," + "\'"+"d"+"\');finish(\'"+END_NAME_FILE+"\');exit;\""
else:
    print("Error: Deteced OS: Not known!")
    raise SystemExit

print("Command/s to be run: \n"+COMMAND_START)
os.system(COMMAND_START)


print("Waiting for Matlab to finish:")
i = 0
while not os.path.exists("end_of_mat.txt"):
    if i == 1:  # to sie i tak nie wykona
        print("wtf")

print("Matlab has finished", end="")

print("FINISH")
df = pd.read_csv("stabs.txt", header=None)
STABS_KG = df[0].to_list()
STABS_1_KG = df[1].to_list()

print("Finished analyzing stability")
print("-"*50)
if os.path.exists("stabs.txt"):
    os.remove("stabs.txt")
# if os.path.exists("end_of_mat.txt"):
#     os.remove("end_of_mat.txt")

# DO LATEXA !!!!!!!!!!!!!!
for x in range(1):
    print("\\textbf{Przykład }\n$$K="+sp.latex(K_LIST[x])+"$$\n"+"$$G="+sp.latex(G_LIST[x])+"$$")
    print("Transmitancja CLS:\n$$K_Z=\\frac{k}{1+KG}=\\frac{" + sp.latex(K_LIST[x]) + "}{1+" + sp.latex(K_LIST[x]) + sp.latex(G_LIST[x]) + "}=" +sp.latex(K_Z_LIST[x])+"$$")
    print("Transmitancja OLS:\n$$K_O=K\\cdot G="+sp.latex(K_LIST[x]*G_LIST[x])+"$$")
    print("\\textbf{Sprawdzamy stabilność CLS z pomocą kryterium Hurwitza:}\\newline")
    print("Wielomian charakterystyczny CLS:\n$$M_Z=" + sp.latex(K_Z_M_LIST[x]) + "$$")
    print("Macierz Hurwitza na podstawie tego wielomianu oraz wartości wyznacznika i podwyznaczników:")
    print("$$" + (hr.Hurwitz_sp(K_Z_LIST[x]))[0]+ "$$\n Tabela z wyznacznikami\n$$" + (hr.Hurwitz_sp(K_Z_LIST[x]))[1]+ "$$")
    print("%oceniam stabilnosc recznie")
    print("\\newline\\textbf{Sprawdzam stabilność CLS z pomocą kryterium Nyquista}\\newline")
    print("Wykres Nyquista dla 1+KG:\n\\includegraphics[width=12cm]{}")
    print("%oceniam stabilnosc recznie\n\\newpage")