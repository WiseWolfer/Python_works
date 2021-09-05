import numpy as np
import matplotlib.pyplot as plt
import networkx  as nx


# Матрицу смежности (страница 30)
# Задание: дан орграф. Сколько в нем маршрутов длиной 4?

#Исходная матрица

A = np.matrix([
[0, 1, 1, 0, 1, 0, 0], 
[0, 0, 1, 0, 1, 0, 0], 
[0, 0, 0, 1, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 1], 
[0, 0, 1, 1, 0, 0, 0], 
[1, 1, 1, 1, 1, 0, 0], 
[0, 1 ,0, 0, 1, 1, 0]]) 

print("\n") 
print("Исходная матрица: \n\n",A)
print("\n") 

#Возведем эту матрицу в степень 4:
    
P1 = A;        
print("Результат первого умножения : ")
print("\n")
print(P1)
print("\n") 

print("Результат второго умножения : ")
print("\n")
P2 = A.dot(A)
print(P2);
print("\n") 

print("Результат третьего умножения : ")
print("\n")
P3 = P2.dot(A)
print(P3) 
print("\n")

print("Результат четвертого умножения : ")
print("\n")
P4 = P3.dot(A)
print(P4)  #Возводим матрицу в 4 степень

i = 0;
j = 0;
super_result = 0;

# iterate through rows 
for i in range(len(P4)): 
# iterate through columns       
    for j in range(len(P4[0][0])):   
              super_result = np.sum(P4)

print("\n")              
print("Количество маршрутов длиной 4 =",super_result) 


# sy.sum(P4)    # сумма элементов в матрице

G = nx.DiGraph() # Создадим орграф.

plt.figure(figsize =(9, 16)) 

G.add_edges_from([(1, 2), (1, 3), (1, 4), (2 ,3), (2, 4),(3, 4),(4, 2),(4, 7),(5,3),
                  (5, 4), (6, 5), (6, 1), (6,2),(6,3),(6,4),(7, 2),(7,5),(7,2)]) 


plt.subplot(211) 
nx.draw_networkx(G) 
plt.title('My Orientated Graph ', fontsize=20, fontname='Times New Roman')

plt.show()


