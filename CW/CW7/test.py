import os
import subprocess
import numpy as np
import pandas as pd
import matplotlib as plt
import sympy as sp
import hurwitz as hr

# Tworzymy plik do latexa, ale na poczatku sprawdzamy czy plik o takiej samej nazwie istnieje
# jak tak to go usuwamy
if os.path.exists("main.tex"):
    os.remove("main.tex")
# Tworzymy plik latexa
main_tex = open("main.tex", "w+")
main_tex.write("\\documentclass\{article\}\n")
main_tex.write("\\usepackage\{polski\}\n")
main_tex.write("\\usepackage\[utf8\]\{inputenc\}\n")
main_tex.write("\\usepackage\{graphicx\}\n")
main_tex.write("\\usepackage\{amsmath\}\n")
main_tex.write("\\usepackage\{amssymb\}\n")
main_tex.write("\\usepackage\{mathtools\}\n")
main_tex.write("\n\n")
main_tex.write("\\title\{Teoria Regulacji - Cwiczenia\}\n")
main_tex.write("\\author\{Jan Bronicki 249011 \\ \n")
main_tex.write("        Denis Firat         \\ \n")
main_tex.write("        Borys Staszczak 248958 \}\n")
main_tex.write("\date\{\}\n")
main_tex.write("\n\n")
main_tex.write("\\begin\{document\}\n")