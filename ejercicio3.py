def fibonacci(numero):
    a = 1
    b = 1
    c =0
    for i in range(1, numero-1):
        c=a +b
        a = b
        b = c
    return c

def fibonacci2(numero):
    a = 1
    b = 1
    for i in range(1, numero-1):
        a, b= b,a+b
    return b

def fibonacci_bottom_up(numero):
    fib_parcial = [1,1]
    while len(fib_parcial) <numero:
        fib_parcial.append(fib_parcial[-1]+fib_parcial[-2])
        
f = fibonacci(4)
print(f)


