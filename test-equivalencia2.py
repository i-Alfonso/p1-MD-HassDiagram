from graficos.mostrar import mostrar_analisis_completo

print("="*80)
print("PRUEBA COMPLETA DEL SISTEMA DE ANÁLISIS DE RELACIONES")
print("="*80)

# EJEMPLO: Relación de equivalencia con letras
print("\n" + "="*60)
print("EJEMPLO: RELACIÓN DE EQUIVALENCIA (vocales y consonantes)")
print("="*60)

conjunto_equiv = {"a", "e", "i", "o", "u", "b", "c", "d"}

relacion_equiv = {
    # Reflexiva - cada elemento se relaciona consigo mismo
    ("a", "a"), ("e", "e"), ("i", "i"), ("o", "o"), ("u", "u"),
    ("b", "b"), ("c", "c"), ("d", "d"),

    # Clase [vocales]: todas se relacionan entre sí
    ("a", "e"), ("a", "i"), ("a", "o"), ("a", "u"),
    ("e", "a"), ("e", "i"), ("e", "o"), ("e", "u"),
    ("i", "a"), ("i", "e"), ("i", "o"), ("i", "u"),
    ("o", "a"), ("o", "e"), ("o", "i"), ("o", "u"),
    ("u", "a"), ("u", "e"), ("u", "i"), ("u", "o"),

    # Clase [consonantes]: se relacionan entre sí
    ("b", "c"), ("b", "d"),
    ("c", "b"), ("c", "d"),
    ("d", "b"), ("d", "c"),
}

print("Conjunto A = {a, e, i, o, u, b, c, d}")
print("Relación R: Dos letras son equivalentes si ambas son vocales o ambas son consonantes")
print("Descripción: La relación divide el conjunto en dos clases de equivalencia: vocales y consonantes")
print()

mostrar_analisis_completo(conjunto_equiv, relacion_equiv)

print("\n" + "="*80 + "\n")
