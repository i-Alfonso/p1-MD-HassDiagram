class AnalizadorRelaciones:
    """
    Clase para analizar propiedades de relaciones matemáticas en conjuntos.

    Esta clase permite determinar si una relación es reflexiva, irreflexiva,
    simétrica, asimétrica, antisimétrica o transitiva, y puede verificar
    si constituye un orden parcial o relación de equivalencia.
    """

    def __init__(self, conjunto, relacion):
        """
        Inicializa el analizador con un conjunto y una relación.
        """
        self.conjunto = set(conjunto)  # Asegurar que es un conjunto
        self.relacion = set(relacion)  # Asegurar que es un conjunto de tuplas

        # Validar que todos los elementos de la relación están en el conjunto
        self._validar_relacion()

    def _validar_relacion(self):
        """
        Valida que todos los elementos de la relación pertenezcan al conjunto.
        """
        for (a, b) in self.relacion:
            if a not in self.conjunto or b not in self.conjunto:
                raise ValueError(f"El par ({a}, {b}) contiene elementos no presentes en el conjunto")

    def es_reflexiva(self):
        """
        Determina si la relación es reflexiva.
        Una relación R es reflexiva si para todo elemento a del conjunto, (a,a) ∈ R.
        """
        elementos_faltantes = []

        for elemento in self.conjunto:
            if (elemento, elemento) not in self.relacion:
                elementos_faltantes.append(elemento)

        if not elementos_faltantes:
            return True, "La relación es reflexiva: todos los elementos se relacionan consigo mismos"
        else:
            return False, f"La relación NO es reflexiva: faltan los pares {[(x, x) for x in elementos_faltantes]}"

    def es_irreflexiva(self):
        """
        Determina si la relación es irreflexiva.
        Una relación R es irreflexiva si para ningún elemento a del conjunto, (a,a) ∈ R.
        """
        pares_reflexivos = []

        for elemento in self.conjunto:
            if (elemento, elemento) in self.relacion:
                pares_reflexivos.append((elemento, elemento))

        if not pares_reflexivos:
            return True, "La relación es irreflexiva: ningún elemento se relaciona consigo mismo"
        else:
            return False, f"La relación NO es irreflexiva: contiene los pares reflexivos {pares_reflexivos}"

    def es_simetrica(self):
        """
        Determina si la relación es simétrica.
        Una relación R es simétrica si para todo (a,b) ∈ R, también (b,a) ∈ R.
        """
        pares_faltantes = []

        for (a, b) in self.relacion:
            if (b, a) not in self.relacion:
                pares_faltantes.append((b, a))

        if not pares_faltantes:
            return True, "La relación es simétrica: para cada par (a,b) existe el par (b,a)"
        else:
            return False, f"La relación NO es simétrica: faltan los pares {pares_faltantes}"

    def es_asimetrica(self):
        """
        Determina si la relación es asimétrica.
        Una relación R es asimétrica si para todo (a,b) ∈ R con a≠b, (b,a) ∉ R.
        Además, no debe contener pares reflexivos.
        """
        # Verificar que no hay pares reflexivos
        pares_reflexivos = [(a, a) for a in self.conjunto if (a, a) in self.relacion]
        if pares_reflexivos:
            return False, f"La relación NO es asimétrica: contiene pares reflexivos {pares_reflexivos}"

        # Verificar que no hay pares simétricos
        pares_simetricos = []
        for (a, b) in self.relacion:
            if a != b and (b, a) in self.relacion:
                pares_simetricos.append(((a, b), (b, a)))

        if not pares_simetricos:
            return True, "La relación es asimétrica: no contiene pares reflexivos ni simétricos"
        else:
            return False, f"La relación NO es asimétrica: contiene pares simétricos {pares_simetricos}"

    def es_antisimetrica(self):
        """
        Determina si la relación es antisimétrica.
        """
        violaciones = []

        for (a, b) in self.relacion:
            if (b, a) in self.relacion and a != b:
                violaciones.append(((a, b), (b, a)))

        if not violaciones:
            return True, "La relación es antisimétrica: si (a,b) y (b,a) están en R, entonces a=b"
        else:
            return False, f"La relación NO es antisimétrica: violaciones {violaciones}"

    def es_transitiva(self):
        """
        Determina si la relación es transitiva.
        """
        pares_faltantes = []

        # Para cada par (a,b) en la relación
        for (a, b) in self.relacion:
            # Buscar todos los pares (b,c) en la relación
            for (x, c) in self.relacion:
                if x == b:  # Encontramos (b,c)
                    # Verificar si (a,c) está en la relación
                    if (a, c) not in self.relacion:
                        pares_faltantes.append((a, c))

        # Eliminar duplicados
        pares_faltantes = list(set(pares_faltantes))

        if not pares_faltantes:
            return True, "La relación es transitiva: si (a,b) y (b,c) están en R, entonces (a,c) está en R"
        else:
            return False, f"La relación NO es transitiva: faltan los pares {pares_faltantes}"

    def es_orden_parcial(self):
        """
        Determina si la relación es un orden parcial.
        Un orden parcial debe ser reflexivo, antisimétrico y transitivo.
        """
        reflexiva, just_ref = self.es_reflexiva()
        antisimetrica, just_anti = self.es_antisimetrica()
        transitiva, just_trans = self.es_transitiva()

        es_orden = reflexiva and antisimetrica and transitiva

        justificacion = f"""
Análisis para orden parcial:
- Reflexiva: {'✓' if reflexiva else '✗'} {just_ref}
- Antisimétrica: {'✓' if antisimetrica else '✗'} {just_anti}
- Transitiva: {'✓' if transitiva else '✗'} {just_trans}

Resultado: {'ES un orden parcial' if es_orden else 'NO ES un orden parcial'}
"""

        return es_orden, justificacion

    def es_relacion_equivalencia(self):
        """
        Determina si la relación es una relación de equivalencia.
        Una relación de equivalencia debe ser reflexiva, simétrica y transitiva.
        """
        reflexiva, just_ref = self.es_reflexiva()
        simetrica, just_sim = self.es_simetrica()
        transitiva, just_trans = self.es_transitiva()

        es_equivalencia = reflexiva and simetrica and transitiva

        justificacion = f"""
Análisis para relación de equivalencia:
- Reflexiva: {'✓' if reflexiva else '✗'} {just_ref}
- Simétrica: {'✓' if simetrica else '✗'} {just_sim}
- Transitiva: {'✓' if transitiva else '✗'} {just_trans}

Resultado: {'ES una relación de equivalencia' if es_equivalencia else 'NO ES una relación de equivalencia'}
"""

        return es_equivalencia, justificacion

    def generar_clases_equivalencia(self):
        """
        Genera las clases de equivalencia para una relación de equivalencia.
        Retorna las clases y el conjunto cociente.
        """
        es_equiv, _ = self.es_relacion_equivalencia()

        if not es_equiv:
            return False, "No se pueden generar clases de equivalencia: la relación no es de equivalencia"

        # Algoritmo para encontrar clases de equivalencia
        clases_equivalencia = []
        elementos_procesados = set()

        for elemento in self.conjunto:
            if elemento not in elementos_procesados:
                # Encontrar todos los elementos relacionados con 'elemento'
                clase = set()
                for (a, b) in self.relacion:
                    if a == elemento:
                        clase.add(b)
                    elif b == elemento:
                        clase.add(a)

                clases_equivalencia.append(clase)
                elementos_procesados.update(clase)

        # El conjunto cociente A/R
        conjunto_cociente = [f"[{min(clase)}]" for clase in clases_equivalencia]

        return True, {
            'clases': clases_equivalencia,
            'conjunto_cociente': conjunto_cociente,
            'elementos': self.conjunto
        }

    def generar_matriz_relacion(self):
        """
        Genera la matriz de la relación.
        Retorna una matriz donde M[i][j] = 1 si (ai, aj) ∈ R, 0 en caso contrario.
        """
        elementos_ordenados = sorted(list(self.conjunto))
        n = len(elementos_ordenados)

        # Crear matriz inicializada en 0
        matriz = [[0 for _ in range(n)] for _ in range(n)]

        # Llenar la matriz
        for (a, b) in self.relacion:
            i = elementos_ordenados.index(a)
            j = elementos_ordenados.index(b)
            matriz[i][j] = 1

        return {
            'matriz': matriz,
            'elementos': elementos_ordenados,
            'tamaño': n
        }

    def mostrar_grafo_equivalencia(self):
        """
        Genera y muestra un grafo de equivalencia hermoso con colores por clases.
        """
        try:
            import matplotlib.pyplot as plt
            import networkx as nx
            import numpy as np
        except ImportError:
            print("Error: Instala matplotlib y networkx: pip install matplotlib networkx")
            return False

        es_equiv, _ = self.es_relacion_equivalencia()
        if not es_equiv:
            print("No se puede generar grafo de equivalencia: la relación no es de equivalencia")
            return False

        # Obtener clases de equivalencia
        resultado_clases = self.generar_clases_equivalencia()
        clases = resultado_clases[1]['clases']

        # Crear grafo no dirigido
        G = nx.Graph()
        G.add_nodes_from(self.conjunto)
        aristas_no_reflexivas = [(a, b) for (a, b) in self.relacion if a != b]
        G.add_edges_from(aristas_no_reflexivas)

        # Layout mejorado
        pos = nx.spring_layout(G, seed=42, k=1.5, iterations=50)

        plt.figure(figsize=(12, 9))
        plt.title("Grafo de Relación de Equivalencia", fontsize=18, fontweight='bold', pad=20)

        # Colores bonitos para las clases
        colores_clases = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3', '#54A0FF', '#5F27CD']

        # Dibujar nodos por clases con colores diferentes
        for i, clase in enumerate(clases):
            color = colores_clases[i % len(colores_clases)]
            nx.draw_networkx_nodes(G, pos, nodelist=list(clase),
                                 node_color=color, node_size=1500, alpha=0.9,
                                 edgecolors='white', linewidths=3)

        # Dibujar aristas simétricas con mejor estilo
        nx.draw_networkx_edges(G, pos, width=3, alpha=0.7, edge_color='#2C3E50')

        # Dibujar aristas reflexivas mejoradas
        reflexivas = [a for a in self.conjunto if (a, a) in self.relacion]
        for nodo in reflexivas:
            x, y = pos[nodo]
            # Bucle reflexivo más elegante
            circle = plt.Circle((x + 0.04, y + 0.08), 0.05, fill=False, color='#E74C3C', linewidth=3)
            plt.gca().add_patch(circle)

        # Etiquetas de nodos más elegantes
        nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold', font_color='white')

        # Información de clases con estilo similar a la leyenda y sin chocar con título
        clases_info = "Clases de Equivalencia: "
        for i, clase in enumerate(clases):
            elementos = sorted(clase)
            representante = min(clase)
            clases_info += f"[{representante}] = {{{', '.join(map(str, elementos))}}}   "

        plt.figtext(0.5, 0.02, clases_info, ha='center', fontsize=11, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.8))

        # Leyenda mejorada
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], color='#2C3E50', lw=3, label='Aristas simétricas'),
            Line2D([0], [0], color='#E74C3C', lw=3, label='Aristas reflexivas'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF6B6B',
                   markersize=15, label='Nodos por clases de equivalencia')
        ]
        plt.legend(handles=legend_elements, loc='upper right', fontsize=11,
                  frameon=True, fancybox=True, shadow=True)

        plt.axis('off')
        plt.tight_layout()
        plt.show()
        return True

    def mostrar_grafo_general(self):
        """
        Genera y muestra un grafo general de la relación (para cualquier tipo de relación).
        """
        try:
            import matplotlib.pyplot as plt
            import networkx as nx
        except ImportError:
            print("Error: Instala matplotlib y networkx: pip install matplotlib networkx")
            return False

        # Crear grafo dirigido
        G = nx.DiGraph()
        G.add_nodes_from(self.conjunto)

        # Agregar aristas no reflexivas
        aristas_no_reflexivas = [(a, b) for (a, b) in self.relacion if a != b]
        G.add_edges_from(aristas_no_reflexivas)

        # Configurar el layout
        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(10, 8))
        plt.title("Grafo de la Relación", fontsize=16, fontweight='bold')

        # Dibujar nodos
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1200, alpha=0.9)

        # Dibujar aristas no reflexivas
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray', arrows=True, arrowsize=20)

        # Dibujar aristas reflexivas
        reflexivas = [a for a in self.conjunto if (a, a) in self.relacion]
        for nodo in reflexivas:
            x, y = pos[nodo]
            # Bucle
            circle = plt.Circle((x + 0.06, y + 0.06), 0.06, fill=False, color='red', linewidth=2)
            plt.gca().add_patch(circle)

        # Dibujar etiquetas
        nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')

        # Agregar leyenda si hay aristas reflexivas
        if reflexivas:
            from matplotlib.lines import Line2D
            legend_elements = [
                Line2D([0], [0], color='gray', lw=2, label='Aristas de la relación'),
                Line2D([0], [0], color='red', lw=2, label='Aristas reflexivas')
            ]
            plt.legend(handles=legend_elements, loc='upper right')

        plt.axis('off')
        plt.tight_layout()
        plt.show()
        return True

    def analizar_propiedades(self):
        """
        Realiza un análisis completo de todas las propiedades de la relación.
        """
        return {
            'reflexiva': self.es_reflexiva(),
            'irreflexiva': self.es_irreflexiva(),
            'simetrica': self.es_simetrica(),
            'asimetrica': self.es_asimetrica(),
            'antisimetrica': self.es_antisimetrica(),
            'transitiva': self.es_transitiva(),
            'orden_parcial': self.es_orden_parcial(),
            'relacion_equivalencia': self.es_relacion_equivalencia()
        }

    def generar_diagrama_hasse(self):
        """
        Genera el diagrama de Hasse para un orden parcial.
        Elimina las aristas transitivas y reflexivas para mostrar solo la estructura mínima.
        """
        es_orden, _ = self.es_orden_parcial()

        if not es_orden:
            return False, "No se puede generar diagrama de Hasse: la relación no es un orden parcial"

        # Crear copia de la relación sin los pares reflexivos
        relacion_sin_reflexivos = {(a, b) for (a, b) in self.relacion if a != b}

        # Eliminar aristas transitivas (reducción transitiva)
        hasse_relacion = set()

        for (a, b) in relacion_sin_reflexivos:
            # Verificar si hay un camino indirecto de a a b
            es_transitiva = False
            # Busca en todo el conjunto un posible elemento intermediario c que cree un camino indirecto a-c-b
            for c in self.conjunto:
                # Solo considera elementos c diferentes de a y b
                if c != a and c != b:
                    # Si ambas existen → Hay un camino indirecto a→c→b → La arista a→b es transitiva (redundante).
                    if (a, c) in relacion_sin_reflexivos and (c, b) in relacion_sin_reflexivos:
                        es_transitiva = True
                        break

            # Si no hay camino indirecto, es una arista del diagrama de Hasse
            if not es_transitiva:
                hasse_relacion.add((a, b))

        # Crear grafo del diagrama de Hasse Diccionario : lista
        hasse_grafo = {elemento: [] for elemento in self.conjunto}
        # Para cada arista a→b en el diagrama de Hasse, agrega b a la lista de sucesores de a
        for (a, b) in hasse_relacion:
            hasse_grafo[a].append(b)

        return True, {
            'grafo': hasse_grafo,
            'aristas': hasse_relacion,
            'elementos': self.conjunto
        }

    def _calcular_niveles_hasse(self, grafo, elementos):
        """
        Calcula los niveles de cada elemento en el diagrama de Hasse.
        Los elementos minimales están en nivel 0.
        Returns:
            dict: Diccionario {nivel: [elementos]}
        """
        # Encontrar elementos sin predecesores (minimales)
        tiene_predecesor = set()
        for origen in grafo:
            for destino in grafo[origen]:
                tiene_predecesor.add(destino)

        elementos_minimales = elementos - tiene_predecesor

        # Asignar niveles
        niveles = {0: list(elementos_minimales)}
        nivel_elemento = {elem: 0 for elem in elementos_minimales}

        nivel_actual = 0
        while True:
            siguiente_nivel = []

            for elem in niveles.get(nivel_actual, []):
                for sucesor in grafo[elem]:
                    if sucesor not in nivel_elemento:
                        # Verificar que todos los predecesores ya tienen nivel asignado
                        predecesores_listos = True
                        for origen in grafo:
                            if sucesor in grafo[origen] and origen not in nivel_elemento:
                                predecesores_listos = False
                                break

                        if predecesores_listos:
                            nivel_elemento[sucesor] = nivel_actual + 1
                            siguiente_nivel.append(sucesor)

            if not siguiente_nivel:
                break

            niveles[nivel_actual + 1] = siguiente_nivel
            nivel_actual += 1

        return niveles

    def mostrar_diagrama_hasse(self):
        """
        Genera y muestra un diagrama de Hasse simple con networkx y matplotlib.
        """
        try:
            import matplotlib.pyplot as plt
            import networkx as nx
        except ImportError:
            print("Error: Instala matplotlib y networkx: pip install matplotlib networkx")
            return False

        es_hasse, resultado = self.generar_diagrama_hasse() # Retorna true y el diccionario
        if not es_hasse:
            print(resultado)
            return False

        aristas = resultado['aristas']
        elementos = resultado['elementos']

        # Crear grafo y posiciones
        G = nx.DiGraph()
        G.add_nodes_from(elementos)
        G.add_edges_from(aristas)

        pos = self._calcular_posiciones(resultado)

        # Dibujar diagrama
        plt.figure(figsize=(8, 6))
        plt.title("Diagrama de Hasse", fontsize=14, fontweight='bold')

        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
        nx.draw_networkx_edges(G, pos, arrows=False, width=2)
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

        plt.axis('off')
        plt.tight_layout()
        plt.show()
        return True

    def _calcular_posiciones(self, hasse_data):
        """
        Calcula posiciones para los nodos del diagrama.
        """
        # Obtiene la estructura: {0: [1], 1: [2,3], 2: [4,6], 3: [12]}
        grafo = hasse_data['grafo']
        elementos = hasse_data['elementos']
        niveles = self._calcular_niveles_hasse(grafo, elementos)

        # fórmula de distribución centrada.
        pos = {}
        for nivel, elementos_nivel in niveles.items():
            elementos_ordenados = sorted(elementos_nivel)
            for i, elemento in enumerate(elementos_ordenados):
                x = i - len(elementos_ordenados)/2 + 0.5 if len(elementos_ordenados) > 1 else 0
                pos[elemento] = (x, nivel)
        return pos
