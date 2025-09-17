from graficos.mostrar import mostrar_analisis_completo

print("="*80)
print("EJEMPLOS DE ÓRDENES PARCIALES - DIAGRAMAS DE HASSE")
print("="*80)

# EJEMPLO 1: Divisores de un número
print("\n" + "="*60)
print("EJEMPLO 1: Divisores de 12 con relación 'divide a'")
print("="*60)

conjunto1 = {"1", "2", "3", "4", "6", "12"}

# Relación: a divide a b (a|b)
relacion1 = {
    # Reflexiva - todo número se divide a sí mismo
    ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("6", "6"), ("12", "12"),

    # 1 divide a todos
    ("1", "2"), ("1", "3"), ("1", "4"), ("1", "6"), ("1", "12"),

    # 2 divide a 4, 6, 12
    ("2", "4"), ("2", "6"), ("2", "12"),

    # 3 divide a 6, 12
    ("3", "6"), ("3", "12"),

    # 4 divide a 12
    ("4", "12"),

    # 6 divide a 12
    ("6", "12")
}

print("A = {1, 2, 3, 4, 6, 12}")
print("Relación: 'a divide a b' (a|b)")
mostrar_analisis_completo(conjunto1, relacion1)