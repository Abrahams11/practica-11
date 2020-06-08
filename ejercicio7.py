import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from time import time
from ejercicio5 import insertsort
from ejercicio6 import quickSort

datos =[ii*100 for ii in range(1,21)]
tiempo_is = []
tiempo_qs = []


# for ii in datos:
    # lista_is = random.sample(range(0,1000000),ii)
    # t0 = time()
    # insertSort(lista_is)
    # tiempo_is.append(round(time()-t0, 6))
# 
# print("Tiempos parciales de ejecucion en insertsort {} [s]" .format(tiempo_is))
# 
# fig, ax = plt.subplots()
# ax.plot(datos, tiempo_is, label="inser sort", marker = "*", color = "r")
# ax.set_xlabel("Datos")
# ax.set_ylabel("Tiempo")
# ax.grid(True)
# ax.legend(loc = 2)
# plt.title("Tiempo de ejecucion [s] inser sort")
# plt.show()

for ii in datos:
    lista_is = random.sample(range(0,1000000),ii)
    lista_qs = lista_is.copy()

    t0 = time()
    insertsort(lista_is)
    tiempo_is.append(round(time()-t0, 6))
    
    t0 = time()
    quickSort(lista_qs)
    tiempo_qs.append(round(time()-t0, 6))

print("Tiempos parciales de ejecucion en insertsort {} [s]" .format(tiempo_is))

print("Tiempos parciales de ejecucion en quick sort{} [s]" .format(tiempo_qs))

fig, ax = plt.subplots()
ax.plot(datos, tiempo_is, label="insert sort", marker = "*", color = "r")
ax.plot(datos, tiempo_qs, label="quick sort", marker = "o", color = "g")


ax.set_xlabel("Datos")
ax.set_ylabel("Tiempo")
ax.grid(True)
ax.legend(loc = 2)
plt.title("Tiempo de ejecucion [s] inser sort vs quick sort")
plt.show()