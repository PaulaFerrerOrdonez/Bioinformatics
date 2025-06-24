# 05_bio_basics.py
# Manipulaciones básicas de secuencias biológicas (ADN)

# Cadena de ADN de ejemplo
secuencia = "ATCGAAAGGCTA"

# Contar nucleótidos
def contar_nucleotidos(seq):
    conteo = {}
    for base in seq:
        if base in conteo: #si la base ya se encuentra en nuestro diccionario sumamos uno
            conteo[base] += 1 
        else:
            conteo[base] = 1
    return conteo

print("Conteo de nucleótidos:", contar_nucleotidos(secuencia))

# Secuencia inversa (reverse)
def secuencia_inversa(seq):
    return seq[::-1]

print("Secuencia inversa:", secuencia_inversa(secuencia))

# Secuencia complementaria (A <-> T, C <-> G)
def secuencia_complementaria(seq):
    complementos = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complementos.get(base, "N") for base in seq)

print("Secuencia complementaria:", secuencia_complementaria(secuencia))

# Buscar un motivo en la secuencia y devolver posiciones (index base 0)
def buscar_motivo(seq, motivo):
    posiciones = []
    largo = len(motivo)
    for i in range(len(seq) - largo + 1):
        if seq[i:i+largo] == motivo:
            posiciones.append(i)
    return posiciones

motivo = "AA"
print(f"Posiciones del motivo '{motivo}':", buscar_motivo(secuencia, motivo))