from graficos.mostrar import mostrar_analisis_completo

# ============================================================================
# EJEMPLO 1: Congruencia módulo 3
# ============================================================================
print("\n" + "="*60)
print("EJEMPLO 1: Congruencia módulo 3")
print("="*60)

conjunto1 = {0, 1, 2, 3, 4, 5}

# Relación: a ≡ b (mod 3) si (a-b) es divisible por 3
relacion1 = {
    # Reflexiva: todo número es congruente consigo mismo
    (0,0), (1,1), (2,2), (3,3), (4,4), (5,5),

    # Clase [0]: {0, 3} - resto 0 al dividir por 3
    (0,3), (3,0),

    # Clase [1]: {1, 4} - resto 1 al dividir por 3
    (1,4), (4,1),

    # Clase [2]: {2, 5} - resto 2 al dividir por 3
    (2,5), (5,2)
}

print("Conjunto: {0, 1, 2, 3, 4, 5}")
print("Relación: congruencia módulo 3 (a ≡ b mod 3)")
print("Descripción: Dos números son equivalentes si tienen el mismo resto al dividir por 3")
mostrar_analisis_completo(conjunto1, relacion1)
