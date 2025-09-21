from relaciones.analizador import AnalizadorRelaciones

def mostrar_analisis_completo(conjunto, relacion):
    """
    Función para mostrar un análisis completo de una relación.
    SIEMPRE muestra las propiedades y SIEMPRE muestra un grafo.
    """
    print(f"ANÁLISIS DE LA RELACIÓN")
    print("=" * 50)
    print(f"Conjunto: {sorted(conjunto)}")
    print(f"Relación: {sorted(relacion)}")
    print()

    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)
        propiedades = analizador.analizar_propiedades()

        # SIEMPRE mostrar propiedades básicas
        print("PROPIEDADES DE LA RELACIÓN:")
        print("-" * 30)

        propiedades_basicas = ['reflexiva', 'irreflexiva', 'simetrica',
                               'asimetrica', 'antisimetrica', 'transitiva']

        for propiedad in propiedades_basicas:
            resultado, justificacion = propiedades[propiedad]
            status = "✓ SÍ" if resultado else "✗ NO"
            print(f"{propiedad.upper()}: {status}")
            print(f"  {justificacion}")
            print()

        # SIEMPRE mostrar análisis de orden parcial
        print("ANÁLISIS DE ORDEN PARCIAL:")
        print("-" * 30)
        print(propiedades['orden_parcial'][1])

        # SIEMPRE mostrar análisis de equivalencia
        print("ANÁLISIS DE RELACIÓN DE EQUIVALENCIA:")
        print("-" * 40)
        print(propiedades['equivalencia'][1])

        # Determinar qué visualización usar
        es_orden_parcial = propiedades['orden_parcial'][0]
        es_equivalencia = propiedades['equivalencia'][0]

        if es_orden_parcial:
            print("\n" + "="*50)
            print("Generando diagrama de Hasse...")
            analizador.mostrar_diagrama_hasse()

        elif es_equivalencia:
            print("\n" + "="*50)
            print("CLASES DE EQUIVALENCIA:")
            print("-" * 25)

            _, datos_equiv = analizador.calcular_clases_equivalencia()
            for i, clase in enumerate(datos_equiv['clases'], 1):
                print(f"Clase {i}: {{{', '.join(map(str, clase))}}}")

            print(f"\nTotal de clases: {datos_equiv['num_clases']}")
            print("Partición del conjunto:", datos_equiv['particion'])

            print("\n" + "="*50)
            print("Generando grafo de equivalencia...")
            analizador.mostrar_grafo_general()

        else:
            print("\n" + "="*50)
            print("GENERANDO GRAFO DIRIGIDO COMPLETO:")
            print("-" * 35)
            datos_grafo = analizador.generar_grafo_general()
            print(f"Total de aristas en la relación: {datos_grafo['total_aristas']}")
            print(f"Aristas no reflexivas: {datos_grafo['aristas_no_reflexivas']}")
            print(f"Elementos: {len(datos_grafo['elementos'])}")
            print("Mostrando grafo dirigido completo (incluye aristas reflexivas)...")
            analizador.mostrar_grafo_completo_con_reflexivos()

    except ValueError as e:
        print(f"Error: {e}")
