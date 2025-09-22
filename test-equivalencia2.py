from graficos.mostrar import mostrar_analisis_completo

print("="*80)
print("PRUEBA COMPLETA DEL SISTEMA DE ANÁLISIS DE RELACIONES")
print("="*80)

# EJEMPLO 1: Relación de equivalencia completa
print("\n" + "="*60)
print("EJEMPLO: RELACIÓN DE EQUIVALENCIA (congruencia módulo 3)")
print("="*60)

conjunto_equiv = {"0", "1", "2", "3", "4", "5"}

relacion_equiv = {
    # Reflexiva - cada elemento se relaciona consigo mismo
    ("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"),

    # Clase [0]: {0, 3} - números que dan resto 0 al dividir por 3
    ("0", "3"), ("3", "0"),

    # Clase [1]: {1, 4} - números que dan resto 1 al dividir por 3
    ("1", "4"), ("4", "1"),

    # Clase [2]: {2, 5} - números que dan resto 2 al dividir por 3
    ("2", "5"), ("5", "2")
}

print("Conjunto A = {0, 1, 2, 3, 4, 5}")
print("Relación R: a ≡ b (mod 3)")
print("Descripción: Dos números son equivalentes si tienen el mismo resto al dividir por 3")
print()

mostrar_analisis_completo(conjunto_equiv, relacion_equiv)

print("\n" + "="*80 + "\n")
