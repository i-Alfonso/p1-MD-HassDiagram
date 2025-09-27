from graficos.mostrar import mostrar_analisis_completo

print("="*80)
print("PRUEBA COMPLETA DEL SISTEMA DE ANÁLISIS DE RELACIONES")
print("="*80)

# EJEMPLO: Relación que no es ni equivalencia ni orden parcial
print("\n" + "="*60)
print("EJEMPLO: RELACIÓN 'LETRAS CONSECUTIVAS EN EL ALFABETO'")
print("="*60)

conjunto_rel = {"a", "b", "c", "d", "e"}

relacion_rel = {
    # Relación de "consecutivas"
    ("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"),
    ("b", "a"), ("c", "b"), ("d", "c"), ("e", "d"),
}

print("Conjunto A = {a, b, c, d, e}")
print("Relación R: (x, y) pertenece a R si y solo si y es consecutiva a x en el alfabeto")
print("Descripción: Dos letras se relacionan si una sigue inmediatamente a la otra")
print()

mostrar_analisis_completo(conjunto_rel, relacion_rel)

print("\n" + "="*80 + "\n")
