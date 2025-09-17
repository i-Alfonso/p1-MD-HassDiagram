# EJEMPLO 3: Potencias de 2
from graficos.mostrar import mostrar_analisis_completo

print("\n" + "="*60)
print("EJEMPLO 3: Potencias de 2 con divisibilidad")
print("="*60)

conjunto4 = {"1", "2", "4", "8", "16"}

relacion4 = {
    # Reflexiva
    ("1", "1"), ("2", "2"), ("4", "4"), ("8", "8"), ("16", "16"),

    # Cadena de divisibilidad
    ("1", "2"), ("1", "4"), ("1", "8"), ("1", "16"),
    ("2", "4"), ("2", "8"), ("2", "16"),
    ("4", "8"), ("4", "16"),
    ("8", "16")
}

print("A = {1, 2, 4, 8, 16}")
print("Relación: divisibilidad (a|b)")
mostrar_analisis_completo(conjunto4, relacion4)

