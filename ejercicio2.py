# Algoritmo greedy
def cambio(cantidad, monedas):
    resulatdo = []
    while cantidad > 0:
        if cantidad >= monedas[0]:
            num = cantidad//monedas[0]
            cantidad = cantidad - (num*monedas[0])
            resulatdo.append([monedas[0], num])
        monedas = monedas[1:]
    return resulatdo

if __name__== "__main__":
    print(cambio(1000,[20, 10, 5, 2 , 10]))
    print(cambio(20,[20, 10, 5, 2 , 10]))
    print(cambio(30,[20, 10, 5, 2 , 10]))
    print(cambio(98,[50, 20, 5,1]))