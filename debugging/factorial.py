import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrementamos n en cada iteración
    return result

if len(sys.argv) > 1:  # Verificamos que se haya pasado un argumento
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
else:
    print("Por favor, ingresa un número entero como argumento.")




    