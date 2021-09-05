import numpy as np
import matplotlib.pyplot as pl
#import numpy.linalg.matrix_power as MatMult
from numpy.linalg import matrix_power as MatMult 
#print("qwe")
x=np.linspace(0,10,1001)
pl.plot(x,np.sin(x))
pl.show()

A=np.array([[1,2,3],[5,-1,0],[-12,3,4]])
print("A=\n",A)
print("\n ne to, zdes poelementno")
print(A*A)
print("\n ne to, zdes poelementno")
print(np.power(A,2))
print("\n ne to, zdes poelementno")
print(A**2)
print("\n umnoj kak v matematike")
print(np.dot(A,A))
print("\n umnoj kak v matematike")
print(np.linalg.matrix_power(A,2))
print("\n umnoj kak v matematike")
print(MatMult(A,2))



import sympy as sy
x=sy.symbols("x")
dy=sy.diff(sy.sin(x**2),x)
print("\n",dy)

e1=sy.expand(x*(x-1)*(x-2)*(x-3))
print(e1)

e2=sy.factor(x**2-2*x+1)
print(e2)