from graficos.mostrar import mostrar_analisis_completo


def ejemplo_relacion_general_grafo():
    """
    RELACIÓN GENERAL: Grafo dirigido arbitrario
    """
    print("\n" + "="*60)
    print("RELACIÓN GENERAL 1: GRAFO DIRIGIDO")
    print("="*60)

    conjunto = {"A", "B", "C", "D", "E", "F"}

    # Relación que forma un grafo con ciclos y caminos
    relacion = {
        # Algunas reflexivas (no todas)
        ("A", "A"), ("C", "C"), ("E", "E"),

        # Conexiones dirigidas
        ("A", "B"), ("B", "C"), ("C", "D"),     # Cadena A→B→C→D
        ("D", "A"),                             # Ciclo D→A
        ("B", "E"), ("E", "F"),                 # Rama B→E→F
        ("F", "B"),                             # Ciclo F→B
        ("C", "F"),                             # Conexión cruzada C→F
        ("D", "E")                              # Otra conexión D→E
    }

    mostrar_analisis_completo(conjunto, relacion)
