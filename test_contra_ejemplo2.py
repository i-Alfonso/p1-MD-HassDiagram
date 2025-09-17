# CONTRAEJEMPLO 2: No es antisimétrica (tiene ciclos)
from graficos.mostrar import mostrar_analisis_completo

print("="*70)
print("CONTRAEJEMPLO 2: RELACIÓN NO ANTISIMÉTRICA (NO ES ORDEN PARCIAL)")
print("="*70)

conjunto_complejo = {"A", "B", "C", "D"}

# Relación: con ciclos bidireccionales
relacion_compleja = {
    # Reflexiva - incluye todos los pares (a,a)
    ("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"),

    # Relaciones normales
    ("A", "B"), ("A", "C"),
    ("C", "D"),

    ("B", "D"), ("D", "B")  # Viola antisimetría
}

mostrar_analisis_completo(conjunto_complejo, relacion_compleja)
