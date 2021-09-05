#Kirsanov str.77
import numpy as np
from numpy import transpose as tra
from numpy.linalg import det as det
from numpy import r_
from numpy import ix_
B=np.matrix([
[3, -1, 0, 0, 0, -1, -1],
[-1, 2, 0, 0, 0, 0, -1],
[0, 0, 2, -1, 0, 0, -1],
[0, 0, -1, 2, -1, 0, -1],
[0, 0, 0, -1, 3, -1, -1],
[-1, 0, 0, 0, -1, 2, -1],
[-1, -1, -1, -1, -1, 0, 5]
])

n,n=B.shape
i=3;j=3;
MB=B[ix_(r_[0:i-1,i:n],r_[0:j-1,j:n])]


print(det(MB))

I=np.matrix('0 0 1 1 0 0 0 0 1 0;\
0 0 1 0 0 0 1 0 0 0;\
1 0 0 0 0 1 0 0 0 0;\
0 0 0 0 0 1 0 1 0 1;\
0 0 0 0 1 0 0 0 0 1;\
0 1 0 1 1 0 0 0 0 0;\
1 1 0 0 0 0 1 1 1 0')

A=np.matrix(\
'0 1 0 0 0 1 1;\
1 0 0 0 0 0 1;\
0 0 0 1 0 0 1;\
0 0 1 0 1 0 1;\
0 0 0 1 0 1 0;\
1 0 0 0 1 0 1;\
1 1 1 1 0 1 0'\
)

I*I.T-2*A-B

I1=np.matrix(\
'0 0 -1 -1 0 0 0 0 -1 0;\
0 0 1 0 0 0 -1 0 0 0;\
-1 0 0 0 0 -1 0 0 0 0;\
0 0 0 0 0 1 0 -1 0 -1;\
0 0 0 0 -1 0 0 0 0 1;\
0 -1 0 1 1 0 0 0 0 0;\
1 1 0 0 0 0 1 1 1 0'\
)

I1*I1.T-B

# M=np.matrix('1 2;4 7')
# print(M)

# M=np.matrix('1 2;\
#             4 7')
# print(M)


# pri\
# nt(3)