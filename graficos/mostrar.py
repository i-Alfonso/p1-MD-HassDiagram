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
            if propiedad != 'orden_parcial':
                status = "✓ SÍ" if resultado else "✗ NO"
                print(f"{propiedad.upper()}: {status}")
                print(f"  Justificación: {justificacion}")
                print()

        # Mostrar análisis de orden parcial
        print("ANÁLISIS DE ORDEN PARCIAL:")
        print("-" * 30)
        print(propiedades['orden_parcial'][1])

        # Si es orden parcial, mostrar diagrama de Hasse
        es_orden_parcial = propiedades['orden_parcial'][0]
        if es_orden_parcial:
            print("\n" + "="*50)
            print("Generando diagrama de Hasse...")
            analizador.mostrar_diagrama_hasse()

    except ValueError as e:
        print(f"Error: {e}")
