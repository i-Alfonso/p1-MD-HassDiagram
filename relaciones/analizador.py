class AnalizadorRelaciones:
    """
    Clase para analizar propiedades de relaciones matemáticas en conjuntos.
    Ahora incluye análisis de equivalencia y generación de grafos generales.
    """

    def __init__(self, conjunto, relacion):
        """
        Inicializa el analizador con un conjunto y una relación.
        """
        self.conjunto = set(conjunto)
        self.relacion = set(relacion)
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
        """
        pares_reflexivos = [(a, a) for a in self.conjunto if (a, a) in self.relacion]
        if pares_reflexivos:
            return False, f"La relación NO es asimétrica: contiene pares reflexivos {pares_reflexivos}"

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
        for (a, b) in self.relacion:
            for (x, c) in self.relacion:
                if x == b:
                    if (a, c) not in self.relacion:
                        pares_faltantes.append((a, c))

        pares_faltantes = list(set(pares_faltantes))

        if not pares_faltantes:
            return True, "La relación es transitiva: si (a,b) y (b,c) están en R, entonces (a,c) está en R"
        else:
            return False, f"La relación NO es transitiva: faltan los pares {pares_faltantes}"

    def es_orden_parcial(self):
        """
        Determina si la relación es un orden parcial.
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

    def es_equivalencia(self):
        """
        Determina si la relación es de equivalencia.
        Una relación de equivalencia debe ser reflexiva, simétrica y transitiva.
        """
        reflexiva, just_ref = self.es_reflexiva()
        simetrica, just_sim = self.es_simetrica()
        transitiva, just_trans = self.es_transitiva()

        es_equiv = reflexiva and simetrica and transitiva

        justificacion = f"""
Análisis para relación de equivalencia:
- Reflexiva: {'✓' if reflexiva else '✗'} {just_ref}
- Simétrica: {'✓' if simetrica else '✗'} {just_sim}
- Transitiva: {'✓' if transitiva else '✗'} {just_trans}

Resultado: {'ES una relación de equivalencia' if es_equiv else 'NO ES una relación de equivalencia'}
"""
        return es_equiv, justificacion

    def calcular_clases_equivalencia(self):
        """
        Calcula las clases de equivalencia si la relación es de equivalencia.
        """
        es_equiv, _ = self.es_equivalencia()

        if not es_equiv:
            return False, "No se pueden calcular clases de equivalencia: la relación no es de equivalencia"

        # Usar unión-búsqueda para encontrar componentes conectados
        padre = {elem: elem for elem in self.conjunto}

        def encontrar(x):
            if padre[x] != x:
                padre[x] = encontrar(padre[x])
            return padre[x]

        def unir(x, y):
            px, py = encontrar(x), encontrar(y)
            if px != py:
                padre[px] = py

        # Unir elementos relacionados
        for (a, b) in self.relacion:
            if a != b:  # No necesitamos procesar pares reflexivos
                unir(a, b)

        # Agrupar elementos por su representante
        clases = {}
        for elem in self.conjunto:
            rep = encontrar(elem)
            if rep not in clases:
                clases[rep] = []
            clases[rep].append(elem)

        # Convertir a lista de conjuntos ordenados
        clases_equivalencia = [sorted(clase) for clase in clases.values()]
        clases_equivalencia.sort()

        return True, {
            'clases': clases_equivalencia,
            'num_clases': len(clases_equivalencia),
            'particion': clases_equivalencia
        }

    def generar_grafo_general(self):
        """
        Genera un grafo general para cualquier relación.
        """
        grafo = {elemento: [] for elemento in self.conjunto}

        for (a, b) in self.relacion:
            if a != b:  # Excluir aristas reflexivas para claridad visual
                grafo[a].append(b)

        return {
            'grafo': grafo,
            'aristas': [(a, b) for (a, b) in self.relacion if a != b],
            'elementos': self.conjunto,
            'total_aristas': len(self.relacion),
            'aristas_no_reflexivas': len([(a, b) for (a, b) in self.relacion if a != b])
        }

    def generar_diagrama_hasse(self):
        """
        Genera el diagrama de Hasse para un orden parcial.
        """
        es_orden, _ = self.es_orden_parcial()

        if not es_orden:
            return False, "No se puede generar diagrama de Hasse: la relación no es un orden parcial"

        relacion_sin_reflexivos = {(a, b) for (a, b) in self.relacion if a != b}
        hasse_relacion = set()

        for (a, b) in relacion_sin_reflexivos:
            es_transitiva = False
            for c in self.conjunto:
                if c != a and c != b:
                    if (a, c) in relacion_sin_reflexivos and (c, b) in relacion_sin_reflexivos:
                        es_transitiva = True
                        break

            if not es_transitiva:
                hasse_relacion.add((a, b))

        hasse_grafo = {elemento: [] for elemento in self.conjunto}
        for (a, b) in hasse_relacion:
            hasse_grafo[a].append(b)

        return True, {
            'grafo': hasse_grafo,
            'aristas': hasse_relacion,
            'elementos': self.conjunto
        }

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
            'equivalencia': self.es_equivalencia()
        }

    def mostrar_grafo_completo(self):
        """
        Muestra el grafo completo incluyendo todas las aristas (reflexivas y no reflexivas).
        """
        try:
            import matplotlib.pyplot as plt
            import networkx as nx
        except ImportError:
            print("Error: Instala matplotlib y networkx: pip install matplotlib networkx")
            return False

        G = nx.DiGraph()
        G.add_nodes_from(self.conjunto)
        G.add_edges_from(self.relacion)  # Incluye TODAS las aristas, incluso reflexivas

        plt.figure(figsize=(10, 8))

        # Posicionamiento circular para mejor visualización
        pos = nx.spring_layout(G, k=2, iterations=50)

        plt.title("Grafo Completo de la Relación (con aristas reflexivas)", fontsize=14, fontweight='bold')

        # Separar aristas reflexivas de no reflexivas
        aristas_reflexivas = [(a, b) for (a, b) in self.relacion if a == b]
        aristas_normales = [(a, b) for (a, b) in self.relacion if a != b]

        # Dibujar nodos
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800, alpha=0.8)

        # Dibujar aristas normales
        if aristas_normales:
            G_normal = nx.DiGraph()
            G_normal.add_edges_from(aristas_normales)
            nx.draw_networkx_edges(G_normal, pos, arrows=True, arrowsize=20,
                                   edge_color='gray', width=2, alpha=0.7)

        # Dibujar aristas reflexivas como bucles
        if aristas_reflexivas:
            for nodo in [a for (a, b) in aristas_reflexivas]:
                x, y = pos[nodo]
                # Crear un pequeño círculo para representar el bucle reflexivo
                circle = plt.Circle((x + 0.15, y + 0.15), 0.08, fill=False,
                                    color='red', linewidth=2, alpha=0.7)
                plt.gca().add_patch(circle)
                # Añadir una pequeña flecha
                plt.annotate('', xy=(x + 0.23, y + 0.15), xytext=(x + 0.15, y + 0.23),
                             arrowprops=dict(arrowstyle='->', color='red', lw=2, alpha=0.7))

        # Dibujar etiquetas
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

        plt.axis('off')
        plt.tight_layout()

        # Agregar leyenda
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], color='gray', lw=2, label='Aristas normales'),
            Line2D([0], [0], color='red', lw=2, label='Aristas reflexivas')
        ]
        plt.legend(handles=legend_elements, loc='upper right')

        plt.show()
        return True

    def mostrar_grafo_general(self):
        """
        Muestra un grafo general para cualquier relación.
        """
        try:
            import matplotlib.pyplot as plt
            import networkx as nx
            import numpy as np
        except ImportError:
            print("Error: Instala matplotlib y networkx: pip install matplotlib networkx")
            return False

        datos_grafo = self.generar_grafo_general()

        G = nx.DiGraph()
        G.add_nodes_from(datos_grafo['elementos'])
        G.add_edges_from(datos_grafo['aristas'])

        plt.figure(figsize=(10, 8))

        # Verificar si es relación de equivalencia para colorear por clases
        es_equiv, _ = self.es_equivalencia()

        if es_equiv:
            # Colorear nodos por clases de equivalencia
            _, datos_equiv = self.calcular_clases_equivalencia()
            colores = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow',
                       'lightpink', 'lightgray', 'lightcyan', 'wheat']

            node_colors = {}
            for i, clase in enumerate(datos_equiv['clases']):
                color = colores[i % len(colores)]
                for elem in clase:
                    node_colors[elem] = color

            color_list = [node_colors[node] for node in G.nodes()]
            titulo = "Grafo de Relación de Equivalencia (colores = clases)"
        else:
            color_list = 'lightblue'
            titulo = "Grafo General de la Relación"

        # Posicionamiento circular para mejor visualización
        pos = nx.spring_layout(G, k=2, iterations=50)

        plt.title(titulo, fontsize=14, fontweight='bold')

        # Dibujar nodos y aristas
        nx.draw_networkx_nodes(G, pos, node_color=color_list, node_size=800, alpha=0.8)
        nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20,
                               edge_color='gray', width=2, alpha=0.7)
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

        plt.axis('off')
        plt.tight_layout()
        plt.show()
        return True

    def mostrar_diagrama_hasse(self):
        """
        Genera y muestra un diagrama de Hasse para órdenes parciales.
        """
        try:
            import matplotlib.pyplot as plt
            import networkx as nx
        except ImportError:
            print("Error: Instala matplotlib y networkx: pip install matplotlib networkx")
            return False

        es_hasse, resultado = self.generar_diagrama_hasse()
        if not es_hasse:
            print(resultado)
            return False

        aristas = resultado['aristas']
        elementos = resultado['elementos']

        G = nx.DiGraph()
        G.add_nodes_from(elementos)
        G.add_edges_from(aristas)

        pos = self._calcular_posiciones(resultado)

        plt.figure(figsize=(8, 6))
        plt.title("Diagrama de Hasse", fontsize=14, fontweight='bold')

        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
        nx.draw_networkx_edges(G, pos, arrows=False, width=2)
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

        plt.axis('off')
        plt.tight_layout()
        plt.show()
        return True

    def _calcular_niveles_hasse(self, grafo, elementos):
        """
        Calcula los niveles de cada elemento en el diagrama de Hasse.
        """
        tiene_predecesor = set()
        for origen in grafo:
            for destino in grafo[origen]:
                tiene_predecesor.add(destino)

        elementos_minimales = elementos - tiene_predecesor
        niveles = {0: list(elementos_minimales)}
        nivel_elemento = {elem: 0 for elem in elementos_minimales}

        nivel_actual = 0
        while True:
            siguiente_nivel = []

            for elem in niveles.get(nivel_actual, []):
                for sucesor in grafo[elem]:
                    if sucesor not in nivel_elemento:
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

    def _calcular_posiciones(self, hasse_data):
        """
        Calcula posiciones para los nodos del diagrama de Hasse.
        """
        grafo = hasse_data['grafo']
        elementos = hasse_data['elementos']
        niveles = self._calcular_niveles_hasse(grafo, elementos)

        pos = {}
        for nivel, elementos_nivel in niveles.items():
            elementos_ordenados = sorted(elementos_nivel)
            for i, elemento in enumerate(elementos_ordenados):
                x = i - len(elementos_ordenados)/2 + 0.5 if len(elementos_ordenados) > 1 else 0
                pos[elemento] = (x, nivel)
        return pos

    def mostrar_grafo_completo_con_reflexivos(self):
        """
        Muestra un grafo dirigido COMPLETO incluyendo TODAS las aristas reflexivas.
        Para relaciones generales que no son orden parcial ni equivalencia.
        """
        try:
            import matplotlib.pyplot as plt
            import networkx as nx
        except ImportError:
            print("Error: Instala matplotlib y networkx: pip install matplotlib networkx")
            return False

        # Crear grafo dirigido con TODAS las aristas (incluidas reflexivas)
        G = nx.DiGraph()
        G.add_nodes_from(self.conjunto)
        G.add_edges_from(self.relacion)  # Agregar TODAS las aristas sin filtrar

        # Configurar layout
        plt.figure(figsize=(10, 8))

        # Usar layout spring para distribución natural
        pos = nx.spring_layout(G, k=3, iterations=50)

        # Título descriptivo
        plt.title("Grafo Dirigido Completo de la Relación", fontsize=16, fontweight='bold')

        # Dibujar nodos
        nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                               node_size=1000, alpha=0.8)

        # Separar aristas reflexivas de no reflexivas para mejor visualización
        aristas_reflexivas = [(a, b) for (a, b) in self.relacion if a == b]
        aristas_normales = [(a, b) for (a, b) in self.relacion if a != b]

        # Dibujar aristas normales
        if aristas_normales:
            nx.draw_networkx_edges(G, pos, edgelist=aristas_normales,
                                   arrows=True, arrowsize=20,
                                   edge_color='gray', width=2, alpha=0.7)

        # Dibujar aristas reflexivas con estilo diferente
        if aristas_reflexivas:
            nx.draw_networkx_edges(G, pos, edgelist=aristas_reflexivas,
                                   arrows=True, arrowsize=15,
                                   edge_color='red', width=1.5, alpha=0.6,
                                   connectionstyle="arc3,rad=0.3")  # Curvatura para reflexivos

        # Etiquetas de nodos
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

        # Información adicional
        info_text = f"Nodos: {len(self.conjunto)}\n"
        info_text += f"Aristas totales: {len(self.relacion)}\n"
        info_text += f"Reflexivas: {len(aristas_reflexivas)}\n"
        info_text += f"No reflexivas: {len(aristas_normales)}"

        plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes,
                 verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

        # Leyenda
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], color='gray', lw=2, label='Aristas normales'),
            Line2D([0], [0], color='red', lw=1.5, label='Aristas reflexivas')
        ]
        plt.legend(handles=legend_elements, loc='upper right')

        plt.axis('off')
        plt.tight_layout()
        plt.show()
        return True
