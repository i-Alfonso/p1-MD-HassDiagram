from graficos.mostrar import mostrar_analisis_completo

print("="*70)
print("TEST: RELACIÓN GENERAL (No es orden parcial ni equivalencia)")
print("="*70)

# Relación general con algunas reflexivas, algunas simétricas, algunos ciclos
conjunto_general = {"A", "B", "C", "D"}

relacion_general = {
    # Algunas reflexivas (no todas)
    ("A", "A"), ("C", "C"),

    # Algunas conexiones dirigidas
    ("A", "B"), ("B", "C"), ("C", "D"),

    # Un ciclo
    ("D", "A"),

    # Algunas conexiones adicionales
    ("B", "D"), ("A", "D")
}

print("Conjunto: {A, B, C, D}")
print("Relación con reflexivas parciales y ciclos")
print("Debe mostrar TODAS las propiedades y el grafo completo")
print()

mostrar_analisis_completo(conjunto_general, relacion_general)
