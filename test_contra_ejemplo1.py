# CONTRAEJEMPLO 1: No es reflexiva
from graficos.mostrar import mostrar_analisis_completo

print("="*70)
print("CONTRAEJEMPLO 1: RELACIÓN NO REFLEXIVA (NO ES ORDEN PARCIAL)")
print("="*70)

conjunto_complejo = {"1", "2", "3", "4"}

# Relación: < (menor que estricto)
relacion_compleja = {
    # NO incluye reflexivas - esta es la razón por la que falla
    # Faltan: ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")

    # Relaciones de orden estricto
    ("1", "2"), ("1", "3"), ("1", "4"),
    ("2", "3"), ("2", "4"),
    ("3", "4")
}

mostrar_analisis_completo(conjunto_complejo, relacion_compleja)

print()
