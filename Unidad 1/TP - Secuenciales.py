# EJERCICIO 1
print("Hola mundo!")

# EJERCICIO 2
nombre = str(input("Ingrese tu nombre: "))
print("Hola", nombre, "!")

# EJERCICIO 3
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
lugar = str(input("Ingrese su lugar de residencia: "))
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# EJERCICIO 4
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

# EJERCICIO 5
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"La cantidad de segundos equivale a {horas:.2f} horas")

# EJERCICIO 6
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# EJERCICIO 7
num1 = int(input("Ingrese el primer número entero (distinto de 0): "))
num2 = int(input("Ingrese el segundo número entero (distinto de 0): "))
if num1 == 0 or num2 == 0:
    print("Los números deben ser distintos de 0.")
else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    print(f"Resultados:")
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division}")

# EJERCICIO 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es de: {imc:2f}")

# EJERCICIO 9
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = 9/5 * celsius + 32
print (f"La temperatura en Celsius ingresada equivale a {fahrenheit:2f} grados Fahrenheit")

# EJERCICIO 10
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los números ingresados es: {promedio}")