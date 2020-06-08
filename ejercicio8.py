import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

def insertsort(lista):
    global times
    for i in range(1, len(lista)):
        times += 1
        actual = lista[i]
        posicion = i
        while posicion > 0 and lista[posicion-1] > actual:
            times += 1
            lista[posicion] = lista[posicion-1]
            posicion = posicion -1
        lista[posicion] = actual
    return lista

TAM =101
eje_x = list(range(1,TAM,1))
eje_y = []

lista_variable=[]

for num in eje_x:
    lista_variable = random.sample(range(0,1000),num)
    times = 0
    lista_variable= insertsort(lista_variable)
    eje_y.append(times)

fig, ax = plt.subplots(facecolor= 'w', edgecolor='k')
ax.plot(eje_x,eje_y,marker= "o", color="b", linestyle="None")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend(["insert sort"])

plt.title("insert sort")
plt.show()

#graficar quicksort con el modelo RAM