import sympy as sy
 
sy.var('a,b,c,d,g', commutative=False)
v=[a,b,c,d,g]
B=sy.Matrix([
[0, b, c, d, g],
[0, 0, c, 0, g],
[a, b, 0, d, 0],
[a, 0, c, 0, g],
[0, b, 0, d, 0]])
A=sy.Matrix([
[0, 1, 1, 1, 1],
[0, 0, 1, 0, 1],
[1, 1, 0, 1, 0],
[1, 0, 1, 0, 1],
[0, 1, 0, 1, 0]])

n,n=A.shape
#n=A.shape[0]
P1=A
P2s=B*P1
sy.pprint(P2s)
P2=sy.Matrix(n, n, lambda i,j: 0 if i==j else P2s[i,j])
sy.pprint(P2)

P3s=B*P2
sy.pprint(P3s)
for i in range(0,n):
    P3s[i,:]=P3s[i,:].subs(v[i],0)
P3=sy.Matrix(n, n, lambda i,j: 0 if i==j else P3s[i,j])
sy.pprint(P3)

P4s=B*P3
sy.pprint(P4s)
for i in range(0,n):
    P4s[i,:]=P4s[i,:].subs(v[i],0)
P4=sy.Matrix(n, n, lambda i,j: 0 if i==j else P4s[i,j])
sy.pprint(P4)

P5s=B*P4
sy.pprint(P5s)
for i in range(0,n):
    P5s[i,:]=P5s[i,:].subs(v[i],0)
####P4=sy.expand(sy.Matrix(n, n, lambda i,j: 0 if i==j else P4s[i,j]))
P5=P5s
sy.pprint(sy.expand(P5))
print(sy.expand(P5))

