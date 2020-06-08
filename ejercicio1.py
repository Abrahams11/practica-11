#Estrategia de fuerza bruta
#Realiza una busqueda exaustiva
from string import ascii_letters, digits
from itertools import product
from time import time

caracteres = ascii_letters +digits

def buscar(con):
    #abrir el archivo con las cadenas generadas
    archivo = open("combinaciones.txt", "w")

    if 3<= len(con) <=4:
        for i in range(3,5):
            for comb in product(caracteres, repeat = i):
                prueba = "".join(comb)
                archivo.write(prueba+"\n")
                if prueba == con:
                    print("la contrasena es {}",format(prueba))
                    archivo.close()
                    break
    
    else: 
        print("Ingrese una contrasena de longitud 3 o 4")

if __name__=="__main__":
    con = input("ingresa una contrasena\n")
    t0 = time()
    buscar(con)
    print("tiempo de ejecuccion {}".format(round(time()-t0,6)))