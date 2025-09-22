from relaciones.analizador import AnalizadorRelaciones

def mostrar_analisis_completo(conjunto, relacion):
    """
    Función auxiliar para mostrar un análisis completo de una relación.

    Args:
        conjunto: Conjunto de elementos
        relacion: Conjunto de pares ordenados que definen la relación
    """
    print(f"ANÁLISIS DE LA RELACIÓN")
    print("=" * 50)
    print(f"Conjunto: {sorted(conjunto)}")
    print(f"Relación: {sorted(relacion)}")
    print()

    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)
        propiedades = analizador.analizar_propiedades()

        print("PROPIEDADES DE LA RELACIÓN:")
        print("-" * 30)

        for propiedad, (resultado, justificacion) in propiedades.items():
            if propiedad not in ['orden_parcial', 'relacion_equivalencia']:
                status = "✓ SÍ" if resultado else "✗ NO"
                print(f"{propiedad.upper()}: {status}")
                print(f"  Justificación: {justificacion}")
                print()

        # Mostrar análisis de orden parcial
        print("ANÁLISIS DE ORDEN PARCIAL:")
        print("-" * 30)
        print(propiedades['orden_parcial'][1])

        # Mostrar análisis de relación de equivalencia
        print("ANÁLISIS DE RELACIÓN DE EQUIVALENCIA:")
        print("-" * 40)
        print(propiedades['relacion_equivalencia'][1])

        # Si es orden parcial, mostrar diagrama de Hasse
        es_orden_parcial = propiedades['orden_parcial'][0]
        if es_orden_parcial:
            print("\n" + "="*50)
            print("Generando diagrama de Hasse...")
            analizador.mostrar_diagrama_hasse()

        # Si es relación de equivalencia, mostrar análisis completo
        es_relacion_equivalencia = propiedades['relacion_equivalencia'][0]
        if es_relacion_equivalencia:
            mostrar_analisis_equivalencia(analizador)
        elif not es_orden_parcial:
            # Si no es orden parcial ni equivalencia, mostrar grafo general
            print("\n" + "="*50)
            print("Generando grafo general de la relación...")
            analizador.mostrar_grafo_general()

    except ValueError as e:
        print(f"Error: {e}")

def mostrar_analisis_equivalencia(analizador):
    """
    Muestra el análisis completo de una relación de equivalencia:
    - Clases de equivalencia
    - Conjunto cociente
    - Matriz de la relación
    - Grafo de equivalencia
    """
    print("\n" + "="*60)
    print("ANÁLISIS DE RELACIÓN DE EQUIVALENCIA")
    print("="*60)

    # Generar clases de equivalencia
    resultado_clases = analizador.generar_clases_equivalencia()
    if resultado_clases[0]:  # Si se pudieron generar las clases
        datos_clases = resultado_clases[1]

        print("\nCLASES DE EQUIVALENCIA:")
        print("-" * 25)
        for i, clase in enumerate(datos_clases['clases'], 1):
            elementos_clase = sorted(list(clase))
            representante = min(clase)
            print(f"[{representante}] = {{{', '.join(map(str, elementos_clase))}}}")

        print(f"\nCONJUNTO COCIENTE A/R:")
        print("-" * 20)
        print(f"A/R = {{{', '.join(datos_clases['conjunto_cociente'])}}}")
        print(f"Número de clases de equivalencia: {len(datos_clases['clases'])}")

    # Mostrar matriz de la relación
    print(f"\nMATRIZ DE LA RELACIÓN:")
    print("-" * 25)
    mostrar_matriz_relacion(analizador)

    # Mostrar grafo de equivalencia
    print(f"\n{'='*50}")
    print("Generando grafo de relación de equivalencia...")
    print("(Incluye aristas reflexivas y simétricas)")
    analizador.mostrar_grafo_equivalencia()

def mostrar_matriz_relacion(analizador):
    """
    Muestra la matriz de la relación de forma organizada.
    """
    datos_matriz = analizador.generar_matriz_relacion()
    matriz = datos_matriz['matriz']
    elementos = datos_matriz['elementos']
    n = datos_matriz['tamaño']

    # Mostrar encabezados de columnas
    print("    ", end="")
    for elemento in elementos:
        print(f"{elemento:>3}", end=" ")
    print()

    # Mostrar filas con etiquetas
    for i, elemento_fila in enumerate(elementos):
        print(f"{elemento_fila:>3} ", end="")
        for j in range(n):
            print(f"{matriz[i][j]:>3}", end=" ")
        print()

    print(f"\nInterpretación: M[i][j] = 1 si el elemento i se relaciona con el elemento j, 0 en caso contrario")

def mostrar_solo_grafo(conjunto, relacion):
    """
    Función auxiliar para mostrar solo el grafo de una relación.
    """
    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)

        # Verificar qué tipo de relación es
        es_orden, _ = analizador.es_orden_parcial()
        es_equiv, _ = analizador.es_relacion_equivalencia()

        print(f"Conjunto: {sorted(conjunto)}")
        print(f"Relación: {sorted(relacion)}")
        print()

        if es_equiv:
            print("Esta es una relación de equivalencia. Mostrando grafo con clases...")
            analizador.mostrar_grafo_equivalencia()
        elif es_orden:
            print("Esta es un orden parcial. Mostrando diagrama de Hasse...")
            analizador.mostrar_diagrama_hasse()
        else:
            print("Mostrando grafo general de la relación...")
            analizador.mostrar_grafo_general()

    except ValueError as e:
        print(f"Error: {e}")

def mostrar_clases_equivalencia(conjunto, relacion):
    """
    Función específica para analizar y mostrar clases de equivalencia.
    """
    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)

        print(f"Conjunto: {sorted(conjunto)}")
        print(f"Relación: {sorted(relacion)}")
        print()

        # Verificar si es relación de equivalencia
        es_equiv, justificacion = analizador.es_relacion_equivalencia()
        print("VERIFICACIÓN DE RELACIÓN DE EQUIVALENCIA:")
        print("=" * 45)
        print(justificacion)

        if es_equiv:
            # Mostrar análisis completo de equivalencia
            mostrar_analisis_equivalencia(analizador)

            # Retornar datos para el menú principal
            resultado_clases = analizador.generar_clases_equivalencia()
            if resultado_clases[0]:
                datos = resultado_clases[1]
                return {
                    'clases': datos['clases'],
                    'num_clases': len(datos['clases'])
                }
        else:
            print("\n" + "="*50)
            print("Esta relación NO es de equivalencia.")
            print("No se pueden generar clases de equivalencia.")

        return None

    except ValueError as e:
        print(f"Error: {e}")
        return None
