#Implementacja modułów
from sympy.interactive import printing
from sympy.integrals.transforms import laplace_transform
printing.init_printing(use_latex=True)
from sympy import *
import sympy as sp
#zainicjowanie symboli
t=sp.Symbol('t',real = True)
s=sp.Symbol('s')
w=sp.Symbol('w')
y=sp.Function('y')(t)
Y=sp.Function('Y')(s)
Y1=sp.Function('Y')(0)
Y2=sp.Function('Y\'')(0)
rownania=[(Eq((y.diff(t,t))+3*(y.diff(t))+2*(y),4)),(Eq((y.diff(t,t))+3*(y.diff(t))+2*(y),2)),(Eq((y.diff(t,t))+3*(y.diff(t))+2*(y),t)),(Eq((y.diff(t,t))+3*(y.diff(t))+2*(y),sin(w*t))),(Eq((y.diff(t,t))+2*(y.diff(t))+2*(y),0)),(Eq((y.diff(t,t))+2*(y.diff(t))+2*(y),0))]
for x in rownania:
    #ustawienie równania oraz warunkó początkowych
    Y1=0#y(0)
    Y2=1#y'(0)
    diffeq = x
    print('Równanie: $$',latex(diffeq),'$$Dla warunków początkowych: $','y(0)= ',Y1,', y\'(0)= ',Y2,'$\\')
    #przygotowuje równanie pod oblicznie rozwiązania wymuszonego
    rozWy=diffeq
    rozWy=rozWy.replace(y.diff(t,t),(0))
    rozWy=rozWy.replace(y.diff(t),(0))
    #przygotowuję równanie pod obliczenie rozwiązania swobodnego
    Diffeq=diffeq.replace(y.diff(t,t),((s**2*Y-s*Y1-Y2)))
    Diffeq=Diffeq.replace(y.diff(t),(s*Y-Y1))
    Diffeq=Diffeq.replace(y,Y)
    print('Przygotowuję równanie do obliczenia rozwiązania ogólnego, aby to zrobić dokonuję transformacji Laplace: $$',latex(Diffeq),'$$Po prawej stronie zostać ma tylko Y(s):$$Y(s)=')
    Diffeq=sp.solve(Diffeq,Y)
    print(latex(Diffeq[0]),'$$ po rozłożeniu na ułamki:$$Y(s)=',latex(apart(Diffeq[0],s)),"$$Dokonuję odwrotnej transformacji Laplace:$$y_1=")
    rozOg=expand(sp.inverse_laplace_transform(Diffeq[0], s, t))
    print((latex(rozOg)).replace('\\theta',''),'$$Podstawiając za pochodne y(t) zera otrzymamy rozwiązanie wymuszone$$',latex(rozWy).replace('\theta',''))
    rozWy=sp.solve(rozWy, y)
    roz=rozOg+rozWy[0]
    print('$$ $$y_2(t)=',latex(rozWy[0]),'$$ Rozwiązanie szczególne naszego równania $$y(t)=y_1(t)+y_2(t)$$ $$y(t)=',(latex(roz)).replace('\\theta',''),'$$\\newpage')























