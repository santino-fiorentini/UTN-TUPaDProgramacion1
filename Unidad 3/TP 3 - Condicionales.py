# EJERCICIO 1

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")


# EJERCICIO 2

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# EJERCICIO 3

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# EJERCICIO 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Categoría: Niño/a")
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente")
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a joven")
else:
    print("Categoría: Adulto")


# EJERCICIO 5

contraseña = str(input("Ingrese una contraseña: "))

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# EJERCICIO 6

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f"Los numeros son: {numeros_aleatorios}")

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar si esta distribución tiene sesgo o no")


# EJERCICIO 7

frase = str(input("Ingrese una frase o palabra: "))

if frase[-1].lower() in "aeiou": 
    frase = frase + "!"
print(frase)


# EJERCICIO 8

nombre = str(input("Ingrese su nombre: "))
opcion = int(input("Elige una opción (1, 2, 3): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")


# EJERCICIO 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")


# EJERCICIO 10

hemisferio = input("Ingrese el hemisferio en el que se encuentra (S/N): ").upper()
dia = int(input("Ingrese el día (1-31): "))
mes = int(input("Ingrese el mes (1-12): "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacion_sur = "Invierno"
else:
    estacion_sur = "Primavera"

if estacion_sur == "Verano":
    estacion_norte = "Invierno"
elif estacion_sur == "Otoño":
    estacion_norte = "Primavera"
elif estacion_sur == "Invierno":
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"

if hemisferio == "S":
    print("En el hemisferio sur es:", estacion_sur)
elif hemisferio == "N":
    print("En el hemisferio norte es:", estacion_norte)
else:
    print("Hemisferio no válido. Ingrese 'S' o 'N'.")