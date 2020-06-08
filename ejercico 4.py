#estrategia descendente o top-down
memoria= {1:1, 2:1, 3:1}

def fibonacci(numero):
    a =1 
    b = 1
    for i in range (1, numero-1):
        a , b=b, a+b
    return b

def fibonacci_top_down(numero):
    if numero in memoria:
        return memoria[numero]
    f = fibonacci(numero-1) + fibonacci(numero-2)
    memoria[numero] = f
    return memoria[numero]

print(fibonacci_top_down(5))
print(memoria)

print(fibonacci_top_down(4))
print(memoria)
