# 02_loops.py
# Introducción a bucles (loops) en Python

# Bucle for: iterar sobre una secuencia
print("Bucle for sobre una lista:")
bases = ["A", "T", "C", "G"]
for base in bases:
    print("Base nitrogenada:", base) #Base cambia de valor en cada vuelta

# Bucle for: usando range()
print("\nBucle for con range():") #/n es un salto de linea
for i in range(5): #range genera una secuencia de numeros 0,1,2,3,4,5
    print("Número:", i)

# Acumulando valores en un bucle
print("\nSumando los primeros 5 números:")
suma = 0 #donde se sumarán los números
for i in range(1, 6): #El limite superior no se incluye en la secuencia
    suma = suma + i
print("Suma total:", suma)

# Bucle while: ejecuta mientras la condición sea verdadera
print("\nBucle while:")
contador = 0
while contador < 3: #Repitirá el bucle 3 veces
    print("Contador:", contador)
    contador += 1 #Equivalente a contador = contador +1

# Ejemplo con cadena de ADN
print("\nContar cuántas veces aparece 'A' en una cadena de ADN:")
adn = "ATCGAAAGGCTA"
contador_a = 0
for base in adn:
    if base == "A":
        contador_a += 1
print("Número de 'A':", contador_a)