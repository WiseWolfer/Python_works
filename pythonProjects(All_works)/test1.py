import numpy as np
import matplotlib.pyplot as pl
#print("qwe")
x=np.linspace(0,10,1001)
pl.plot(x,np.sin(x))
pl.show()

A=np.array([[1,2,3],[5,-1,0],[-12,3,4]])
print(A)
print("ne to a eto poelementno")
print(A*A)
print("eto umnoj kak v math")
print(np.dot(A,A))

import sympy as sy
x=sy.symbols("x")
dy=sy.diff(sy.sin(x**2),x)
print(dy)

e1=sy.expand(x*(x-1)*(x-2)*(x-3)) 
print(e1)

e2=sy.factor(x**2-2*x+1)    

e3=sy.expand(6*x + 11*x**2 + 6*x**3+x**4 - 2*(2*x+3*x**2+ x**3))
print(e3)

e4=sy.factor(x**4 + 4*x**3 + 5*x**2 + 2*x)
print(e4)