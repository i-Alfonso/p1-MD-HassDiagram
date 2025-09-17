from graficos.mostrar import mostrar_analisis_completo

# EJEMPLO COMPLEJO: Divisores de 60 con múltiples bifurcaciones
print("\n" + "="*70)
print("EJEMPLO COMPLEJO: Divisores de 60 con relación 'divide a'")
print("="*70)

conjunto_complejo = {"1", "2", "3", "4", "5", "6", "10", "12", "15", "20", "30", "60"}

# Relación: a divide a b (a|b)
# 60 = 2² × 3 × 5, por lo que tiene muchos divisores
relacion_compleja = {
    # Reflexiva - cada número se divide a sí mismo
    ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"),
    ("10", "10"), ("12", "12"), ("15", "15"), ("20", "20"), ("30", "30"), ("60", "60"),

    # 1 divide a todos (elemento mínimo)
    ("1", "2"), ("1", "3"), ("1", "4"), ("1", "5"), ("1", "6"),
    ("1", "10"), ("1", "12"), ("1", "15"), ("1", "20"), ("1", "30"), ("1", "60"),

    # Divisiones desde 2
    ("2", "4"), ("2", "6"), ("2", "10"), ("2", "12"), ("2", "20"), ("2", "30"), ("2", "60"),

    # Divisiones desde 3
    ("3", "6"), ("3", "12"), ("3", "15"), ("3", "30"), ("3", "60"),

    # Divisiones desde 4
    ("4", "12"), ("4", "20"), ("4", "60"),

    # Divisiones desde 5
    ("5", "10"), ("5", "15"), ("5", "20"), ("5", "30"), ("5", "60"),

    # Divisiones desde 6
    ("6", "12"), ("6", "30"), ("6", "60"),

    # Divisiones desde 10
    ("10", "20"), ("10", "30"), ("10", "60"),

    # Divisiones desde 12
    ("12", "60"),

    # Divisiones desde 15
    ("15", "30"), ("15", "60"),

    # Divisiones desde 20
    ("20", "60"),

    # Divisiones desde 30
    ("30", "60")
}

print("A = {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}")
print("Relación: divisibilidad (a|b) - 'a divide a b'")
print("60 = 2² × 3 × 5 → muchos divisores → estructura compleja")
print("=" * 70)

mostrar_analisis_completo(conjunto_complejo, relacion_compleja)

print("\n" + "="*70)
print("OTRO EJEMPLO COMPLEJO: Subconjuntos de {1,2,3} con inclusión")
print("="*70)
