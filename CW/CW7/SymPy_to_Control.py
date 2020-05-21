
import numpy as np
import sympy as sympy
import control as co
# We tell python to treat "s" as a SymPy symbol
# We have to make it rational!
s = sympy.Symbol('s', rational=True)
# An example Transfer function
K = (s+3)/(3*s**3 + 2*s**2 + 1*s + 1)
'''
Here is where it gets dirty.
We convert the expression to a Polynomial object in SymPy 
and then we extract coefficients, but that list of coefficients
we will get, will be full of sympy.core.numbers, so
it's going to be numbers but sympy's numbers. That's why then we 
go and each one of them into a float
'''
# We get the numerator and denomiator
num_list, den_list =  [[float(i) for i in sympy.Poly(i, s).all_coeffs()] for i in K.as_numer_denom()];
# Now num_list and den_list are simple float lists and we put them into 
# TransferFunction() function from control module
trf = co.TransferFunction(num_list, den_list)
