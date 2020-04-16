import numpy
import math
import matplotlib.pyplot as plt

# ---------------------------------------------------------- #
#                       DEFINICJE
# ---------------------------------------------------------- #
def d1(t,p,q):
    s1 = (-2*p-math.sqrt(4*p*p-4*q))/2
    s2 = (-2*p+math.sqrt(4*p*p-4*q))/2
    return (1/(s2-s1))*(math.exp(s2*t)-math.exp(s1*t))

def d2(t,p,q):
    s0 = -1*p
    return t*math.exp(s0*t)

def d3(t,p,q):
    c1 = math.exp(-1*p)/(math.sqrt(q-p*p))
    return c1 * math.sin(t*math.sqrt(q-p*p))


# ---------------------------------------------------------- #
#                       PARAMETRY
# ---------------------------------------------------------- #

krok = 0.02
k = 1500
t = numpy.zeros(k)
y_d1 = numpy.zeros(k)
y_d2 = numpy.zeros(k)
y_d3 = numpy.zeros(k)
t[0] = 0
for i in range(1,k):
    t[i] = t[i-1] + krok
    y_d1[i] = d1(t[i],1.16,0.5)
    y_d2[i] = d2(t[i],1,1)
    y_d3[i] = d3(t[i],1,2)

print(t)
print(y_d1,y_d2,y_d3)

fig6, axs6 = plt.subplots()
axs6.plot(t,y_d1,color='black',alpha=0.8,label=r'$\Delta > 0, p=1.16, q=0.5$')
axs6.plot(t,y_d2,color='green',alpha=0.8,label=r'$\Delta = 0, p=1, q=1$')
axs6.plot(t,y_d3,color='red',alpha=0.8,label=r'$\Delta < 0, p=1, q=2$')
axs6.grid(True)
axs6.legend(fontsize=18,shadow=True,framealpha=0.6)
axs6.set_xlabel(r'$t$',fontsize=30)

plt.show()