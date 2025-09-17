from graficos.mostrar import mostrar_analisis_completo

# A = {∅, {1}, {2}, {1,2}}
# Relación: inclusión de conjuntos ⊆

conjunto = {"∅", "{1}", "{2}", "{1,2}"}

# Relación de inclusión:
# ∅ ⊆ {1}, {2}, {1,2}
# {1} ⊆ {1,2}
# {2} ⊆ {1,2}
# Además todos se incluyen en sí mismos (reflexiva)

relacion = {
    # Reflexiva - cada conjunto se incluye en sí mismo
    ("∅", "∅"), ("{1}", "{1}"), ("{2}", "{2}"), ("{1,2}", "{1,2}"),

    # ∅ se incluye en todos los demás
    ("∅", "{1}"), ("∅", "{2}"), ("∅", "{1,2}"),

    # {1} se incluye en {1,2}
    ("{1}", "{1,2}"),

    # {2} se incluye en {1,2}
    ("{2}", "{1,2}")
}

print("PRUEBA: Relación de inclusión de conjuntos")
print("A = {∅, {1}, {2}, {1,2}}")
print("Relación: inclusión de conjuntos (⊆)")
print("=" * 60)

mostrar_analisis_completo(conjunto, relacion)