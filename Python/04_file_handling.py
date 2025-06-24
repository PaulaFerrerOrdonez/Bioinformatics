# 04_file_handling.py
# Introducción a lectura y escritura de archivos en Python
# Ejemplos útiles para manejar archivos FASTA, CSV, TSV en bioinformática

# Escribir en un archivo de texto
with open("secuencia.txt", "w") as archivo:  #with controla automáticamente la apertura y cierre del archivo
    archivo.write("ATCGTTAGGCTA\n")          #archivo le da nombre al documento
    archivo.write("GGCATCGTAGGC\n")

print("Archivo 'secuencia.txt' creado y escrito.")

# Leer un archivo completo
with open("secuencia.txt", "r") as archivo: #El modo "r" indica lectura
    contenido = archivo.read()

print("\nContenido completo de 'secuencia.txt':")
print(contenido)

# Leer archivo línea por línea
print("Contenido línea por línea:")
with open("secuencia.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip()) #strip() elimina cualquier espacio en blanco alrededor de la línea

# Ejemplo simple de lectura y parseo de archivo FASTA
print("\nEjemplo básico parseando archivo FASTA:")

fasta_simulado = [
    ">seq1 Descripción secuencia 1",
    "ATCGTACGATCG",
    ">seq2 Otra secuencia",
    "GGGTTTCCCAA"
]

# Parsear secuencias FASTA (sin usar librerías externas)
secuencias = {} #donde se va a guardar las secuencias
clave_actual = ""

for linea in fasta_simulado:
    if linea.startswith(">"): #Si la línea empieza con ">", significa que es el nombre de una secuencia.
        clave_actual = linea[1:].split()[0]  # toma el ID (primer elemento después del >)
        secuencias[clave_actual] = ""
    else:
        secuencias[clave_actual] += linea.strip()

print("Secuencias parseadas:")
for id_seq, seq in secuencias.items():
    print(f"{id_seq}: {seq}")