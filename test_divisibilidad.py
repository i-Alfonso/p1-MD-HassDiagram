from graficos.mostrar import mostrar_analisis_completo

# Conjunto A = {1, 2, 3, 4, 6, 12}
conjunto = {1, 2, 3, 4, 6, 12}

# Relación: a ≤ b si y solo si a divide a b
relacion = {
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 6), (1, 12),
    (2, 2), (2, 4), (2, 6), (2, 12),
    (3, 3), (3, 6), (3, 12),
    (4, 4), (4, 12),
    (6, 6), (6, 12),
    (12, 12)
}

print("PRUEBA: Relación de divisibilidad")
print("Conjunto A = {1, 2, 3, 4, 6, 12}")
print("Relación: a ≤ b si y solo si a divide a b")
print("=" * 60)

mostrar_analisis_completo(conjunto, relacion)