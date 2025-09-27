from graficos.mostrar import mostrar_analisis_completo

print("="*80)
print("EJEMPLOS DE RELACIONES DE EQUIVALENCIA - 12 NODOS")
print("="*80)

# EJEMPLO 1: Congruencia módulo 4
print("\n" + "="*60)
print("EJEMPLO 1: RELACIÓN DE EQUIVALENCIA (congruencia módulo 4)")
print("="*60)

conjunto1 = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"}

relacion1 = {
    # Reflexiva - cada elemento se relaciona consigo mismo
    ("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"),
    ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"), ("11", "11"),

    # Clase [0]: {0, 4, 8} - números que dan resto 0 al dividir por 4
    ("0", "4"), ("4", "0"), ("0", "8"), ("8", "0"), ("4", "8"), ("8", "4"),

    # Clase [1]: {1, 5, 9} - números que dan resto 1 al dividir por 4
    ("1", "5"), ("5", "1"), ("1", "9"), ("9", "1"), ("5", "9"), ("9", "5"),

    # Clase [2]: {2, 6, 10} - números que dan resto 2 al dividir por 4
    ("2", "6"), ("6", "2"), ("2", "10"), ("10", "2"), ("6", "10"), ("10", "6"),

    # Clase [3]: {3, 7, 11} - números que dan resto 3 al dividir por 4
    ("3", "7"), ("7", "3"), ("3", "11"), ("11", "3"), ("7", "11"), ("11", "7")
}

print("Conjunto A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}")
print("Relación R: a ≡ b (mod 4)")
print("Descripción: Dos números son equivalentes si tienen el mismo resto al dividir por 4")
print("Clases de equivalencia:")
print("  [0] = {0, 4, 8}")
print("  [1] = {1, 5, 9}")
print("  [2] = {2, 6, 10}")
print("  [3] = {3, 7, 11}")
print()

mostrar_analisis_completo(conjunto1, relacion1)

print("\n" + "="*80 + "\n")
