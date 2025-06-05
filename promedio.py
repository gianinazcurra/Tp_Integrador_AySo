# Lista vacía para almacenar las notas
notas = []

# Pedimos 3 notas al usuario
for i in range(3):
    nota = float(input(f"Ingresá la nota {i+1}: "))
    notas.append(nota)

# Calculamos el promedio
promedio = sum(notas) / len(notas)

# Mostramos el resultado
print(f"\nLas notas ingresadas son: {notas}")
print(f"El promedio es: {promedio}")
