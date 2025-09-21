from relaciones.analizador import AnalizadorRelaciones

def mostrar_analisis_completo(conjunto, relacion):
    """
    Función para mostrar un análisis completo de una relación incluyendo
    orden parcial, equivalencia y grafos generales.
    """
    print(f"ANÁLISIS DE LA RELACIÓN")
    print("=" * 50)
    print(f"Conjunto: {sorted(conjunto)}")
    print(f"Relación: {sorted(relacion)}")
    print()

    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)
        propiedades = analizador.analizar_propiedades()

        # Mostrar propiedades básicas
        print("PROPIEDADES DE LA RELACIÓN:")
        print("-" * 30)

        propiedades_basicas = ['reflexiva', 'irreflexiva', 'simetrica',
                               'asimetrica', 'antisimetrica', 'transitiva']

        for propiedad in propiedades_basicas:
            resultado, justificacion = propiedades[propiedad]
            status = "✓ SÍ" if resultado else "✗ NO"
            print(f"{propiedad.upper()}: {status}")
            print(f"  Justificación: {justificacion}")
            print()

        # Análisis de orden parcial
        print("ANÁLISIS DE ORDEN PARCIAL:")
        print("-" * 30)
        print(propiedades['orden_parcial'][1])

        # Análisis de relación de equivalencia
        print("ANÁLISIS DE RELACIÓN DE EQUIVALENCIA:")
        print("-" * 40)
        print(propiedades['equivalencia'][1])

        # Determinar qué tipo de visualización mostrar
        es_orden_parcial = propiedades['orden_parcial'][0]
        es_equivalencia = propiedades['equivalencia'][0]

        print("\n" + "="*50)
        print("VISUALIZACIÓN:")
        print("-" * 15)

        if es_orden_parcial:
            print("Generando diagrama de Hasse...")
            analizador.mostrar_diagrama_hasse()

        elif es_equivalencia:
            # Mostrar clases de equivalencia
            print("CLASES DE EQUIVALENCIA:")
            print("-" * 25)

            _, datos_equiv = analizador.calcular_clases_equivalencia()
            for i, clase in enumerate(datos_equiv['clases'], 1):
                print(f"Clase {i}: {{{', '.join(map(str, clase))}}}")

            print(f"\nTotal de clases: {datos_equiv['num_clases']}")
            print("La partición del conjunto es:", datos_equiv['particion'])

            print("\nGenerando grafo de equivalencia...")
            analizador.mostrar_grafo_general()

        else:
            # Para cualquier otra relación, mostrar grafo general completo
            print("Generando grafo general completo (incluyendo aristas reflexivas)...")
            datos_grafo = analizador.generar_grafo_general()
            print(f"Total de aristas en la relación: {datos_grafo['total_aristas']}")
            print(f"Aristas reflexivas: {datos_grafo['total_aristas'] - datos_grafo['aristas_no_reflexivas']}")
            print(f"Aristas no reflexivas: {datos_grafo['aristas_no_reflexivas']}")
            analizador.mostrar_grafo_completo()

    except ValueError as e:
        print(f"Error: {e}")

def mostrar_solo_grafo(conjunto, relacion):
    """
    Función auxiliar para mostrar solo el grafo de una relación.
    """
    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)
        print("Generando visualización...")
        analizador.mostrar_grafo_general()
    except ValueError as e:
        print(f"Error: {e}")

def mostrar_clases_equivalencia(conjunto, relacion):
    """
    Función auxiliar para mostrar solo las clases de equivalencia.
    """
    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)
        es_equiv, _ = analizador.es_equivalencia()

        if es_equiv:
            _, datos = analizador.calcular_clases_equivalencia()
            print("CLASES DE EQUIVALENCIA:")
            print("-" * 25)
            for i, clase in enumerate(datos['clases'], 1):
                print(f"[{', '.join(map(str, clase))}]")
            return datos
        else:
            print("La relación no es de equivalencia.")
            return None

    except ValueError as e:
        print(f"Error: {e}")
        return None
