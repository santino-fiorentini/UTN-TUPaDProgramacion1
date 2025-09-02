# EJERCICIO 1

for i in range(101):
    print(i)


# EJERCICIO 2

num = int(input("Ingrese un número entero: "))
print("Cantidad de dígitos:", len(str(abs(num))))


# EJERCICIO 3

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a < b:
    suma = sum(range(a+1, b))
else:
    suma = sum(range(b+1, a))
print("La suma es:", suma)


# EJERCICIO 4

suma = 0
while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    suma += n
print("Suma total de los números ingresados:", suma)


# EJERCICIO 5

import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el número (0-9): "))
    intentos += 1
    if intento == secreto:
        print("Adivinaste! Número de intentos:", intentos)
        break


# EJERCICIO 6

for i in range(100, -1, -2):
    print(i)


# EJERCICIO 7

n = int(input("Ingrese un número positivo: "))
suma = sum(range(n+1))
print("La suma es:", suma)


# EJERCICIO 8

cantidad = 100
pares = impares = positivos = negativos = 0
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)



# EJERCICIO 9

cantidad = 100
suma = 0
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num
media = suma / cantidad
print("La media es:", media)


# EJERCICIO 10

num = input("Ingrese un número: ")
print("Número invertido:", num[::-1])