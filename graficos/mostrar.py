from relaciones.analizador import AnalizadorRelaciones

def mostrar_analisis_completo(conjunto, relacion):
    """
    Función auxiliar para mostrar un análisis completo de una relación.
    EXTENSIÓN: Ahora incluye análisis de relaciones de equivalencia y diagramas de partición.

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

        # Mostrar todas las propiedades excepto los análisis especiales
        propiedades_basicas = ['reflexiva', 'irreflexiva', 'simetrica', 'asimetrica', 'antisimetrica', 'transitiva']

        for propiedad in propiedades_basicas:
            if propiedad in propiedades:
                resultado, justificacion = propiedades[propiedad]
                status = "✓ SÍ" if resultado else "✗ NO"
                print(f"{propiedad.upper()}: {status}")
                print(f"  Justificación: {justificacion}")
                print()

        # Determinar tipo de relación especial
        tipo_relacion, descripcion = analizador.determinar_tipo_relacion()

        print("ANÁLISIS DE TIPO DE RELACIÓN:")
        print("-" * 40)
        print(f"TIPO: {tipo_relacion}")
        print(f"Descripción: {descripcion}")
        print()

        # Análisis específico según el tipo
        es_orden_parcial = propiedades['orden_parcial'][0]
        es_equivalencia = propiedades['relacion_equivalencia'][0]

        if es_orden_parcial:
            print("ANÁLISIS DE ORDEN PARCIAL:")
            print("-" * 30)
            print(propiedades['orden_parcial'][1])

            print("\n" + "="*50)
            print("Generando diagrama de Hasse...")
            analizador.mostrar_diagrama_hasse()

        if es_equivalencia:
            print("ANÁLISIS DE RELACIÓN DE EQUIVALENCIA:")
            print("-" * 40)
            print(propiedades['relacion_equivalencia'][1])

            # Mostrar clases de equivalencia
            exito, resultado_clases = analizador.generar_clases_equivalencia()
            if exito:
                print("\nCLASES DE EQUIVALENCIA:")
                print("-" * 25)
                clases = resultado_clases['clases']
                for i, clase in enumerate(clases, 1):
                    elementos_ordenados = sorted(list(clase))
                    print(f"Clase {i}: {{{', '.join(map(str, elementos_ordenados))}}}")

                print(f"\nEstadísticas:")
                print(f"- Número de clases: {resultado_clases['numero_clases']}")
                print(f"- Elementos totales: {resultado_clases['elementos_totales']}")
                print(f"- Partición completa: {'Sí' if resultado_clases['particion_completa'] else 'No'}")

                print("\n" + "="*50)
                print("Generando diagrama de partición...")
                analizador.mostrar_diagrama_particion()

        # Si no es ninguno de los dos tipos especiales
        if not es_orden_parcial and not es_equivalencia:
            print("ANÁLISIS GENERAL:")
            print("-" * 20)
            print("Esta relación no es ni un orden parcial ni una relación de equivalencia.")
            print("No se puede generar diagrama de Hasse ni diagrama de partición.")

            # Sugerir qué propiedades faltan para cada tipo
            reflexiva = propiedades['reflexiva'][0]
            antisimetrica = propiedades['antisimetrica'][0]
            simetrica = propiedades['simetrica'][0]
            transitiva = propiedades['transitiva'][0]

            print("\nPara ser orden parcial necesita:")
            if not reflexiva: print("  ✗ Ser reflexiva")
            if not antisimetrica: print("  ✗ Ser antisimétrica")
            if not transitiva: print("  ✗ Ser transitiva")

            print("\nPara ser relación de equivalencia necesita:")
            if not reflexiva: print("  ✗ Ser reflexiva")
            if not simetrica: print("  ✗ Ser simétrica")
            if not transitiva: print("  ✗ Ser transitiva")

    except ValueError as e:
        print(f"Error: {e}")

def mostrar_solo_equivalencia(conjunto, relacion):
    """
    Función específica para mostrar solo el análisis de relación de equivalencia.
    Útil cuando sabes que la relación es de equivalencia y solo quieres ese análisis.

    Args:
        conjunto: Conjunto de elementos
        relacion: Conjunto de pares ordenados que definen la relación
    """
    print(f"ANÁLISIS DE RELACIÓN DE EQUIVALENCIA")
    print("=" * 50)
    print(f"Conjunto: {sorted(conjunto)}")
    print(f"Relación: {sorted(relacion)}")
    print()

    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)

        # Verificar si es relación de equivalencia
        es_equiv, justificacion = analizador.es_relacion_equivalencia()
        print(justificacion)

        if es_equiv:
            # Generar y mostrar clases de equivalencia
            exito, resultado = analizador.generar_clases_equivalencia()
            if exito:
                clases = resultado['clases']
                print("CLASES DE EQUIVALENCIA:")
                print("-" * 25)
                for i, clase in enumerate(clases, 1):
                    elementos_ordenados = sorted(list(clase))
                    print(f"[{i}] = {{{', '.join(map(str, elementos_ordenados))}}}")

                print(f"\nRESUMEN:")
                print(f"- Número de clases: {resultado['numero_clases']}")
                print(f"- Elementos totales: {resultado['elementos_totales']}")

                # Mostrar diagrama de partición
                print("\n" + "="*50)
                print("Generando diagrama de partición...")
                analizador.mostrar_diagrama_particion()
        else:
            print("No se puede generar diagrama de partición: no es una relación de equivalencia")

    except ValueError as e:
        print(f"Error: {e}")

def mostrar_comparacion_tipos(conjunto, relacion):
    """
    Función que muestra una comparación directa entre orden parcial y relación de equivalencia.
    Útil para entender las diferencias entre ambos tipos de relaciones.

    Args:
        conjunto: Conjunto de elementos
        relacion: Conjunto de pares ordenados que definen la relación
    """
    print(f"COMPARACIÓN: ORDEN PARCIAL vs RELACIÓN DE EQUIVALENCIA")
    print("=" * 65)
    print(f"Conjunto: {sorted(conjunto)}")
    print(f"Relación: {sorted(relacion)}")
    print()

    try:
        analizador = AnalizadorRelaciones(conjunto, relacion)

        # Obtener análisis de ambos tipos
        es_orden, just_orden = analizador.es_orden_parcial()
        es_equiv, just_equiv = analizador.es_relacion_equivalencia()

        # Mostrar tabla comparativa
        print("COMPARACIÓN DE PROPIEDADES:")
        print("-" * 40)
        print(f"{'Propiedad':<15} {'Orden Parcial':<15} {'Equivalencia':<15}")
        print("-" * 40)

        # Obtener propiedades individuales
        reflexiva, _ = analizador.es_reflexiva()
        antisimetrica, _ = analizador.es_antisimetrica()
        simetrica, _ = analizador.es_simetrica()
        transitiva, _ = analizador.es_transitiva()

        print(f"{'Reflexiva':<15} {'Requerida':<15} {'Requerida':<15}")
        print(f"{'Actual:':<15} {'✓' if reflexiva else '✗':<15} {'✓' if reflexiva else '✗':<15}")
        print()
        print(f"{'Antisimétrica':<15} {'Requerida':<15} {'Prohibida':<15}")
        print(f"{'Actual:':<15} {'✓' if antisimetrica else '✗':<15} {'✗' if antisimetrica else '✓':<15}")
        print()
        print(f"{'Simétrica':<15} {'Prohibida':<15} {'Requerida':<15}")
        print(f"{'Actual:':<15} {'✗' if simetrica else '✓':<15} {'✓' if simetrica else '✗':<15}")
        print()
        print(f"{'Transitiva':<15} {'Requerida':<15} {'Requerida':<15}")
        print(f"{'Actual:':<15} {'✓' if transitiva else '✗':<15} {'✓' if transitiva else '✗':<15}")
        print()

        # Resultados finales
        print("RESULTADOS:")
        print("-" * 20)
        print(f"¿Es orden parcial?: {'SÍ' if es_orden else 'NO'}")
        print(f"¿Es relación de equivalencia?: {'SÍ' if es_equiv else 'NO'}")

        # Tipo final
        tipo, descripcion = analizador.determinar_tipo_relacion()
        print(f"\nTIPO FINAL: {tipo}")
        print(f"Descripción: {descripcion}")

    except ValueError as e:
        print(f"Error: {e}")
