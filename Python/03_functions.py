# 03_functions.py
# Introducción a funciones en Python

# Definimos una función para saludar
def saludar(nombre): 
    print("Hola,", nombre)

# Usamos la función con diferentes argumentos
saludar("Sara")
saludar("Carlos")

# Función que suma dos números y devuelve el resultado
def sumar(a, b):
    return a + b

resultado = sumar(5, 7)
print("La suma de 5 y 7 es:", resultado)

# Función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
print(f"El factorial de {num} es:", factorial(num)) #Utilizamos la f antes de las comillas para que se interprete {num} como una variable