class AnalizadorRelaciones:
    """
    Clase para analizar propiedades de relaciones matemáticas en conjuntos.

    Esta clase permite determinar si una relación es reflexiva, irreflexiva,
    simétrica, asimétrica, antisimétrica o transitiva, y puede verificar
    si constituye un orden parcial.
    """

    def __init__(self, conjunto, relacion):
        """
        Inicializa el analizador con un conjunto y una relación.

        Args:
            conjunto (set): Conjunto de elementos sobre el cual se define la relación
            relacion (set): Conjunto de pares ordenados (tuplas) que representan la relación
        """
        self.conjunto = set(conjunto)  # Asegurar que es un conjunto
        self.relacion = set(relacion)  # Asegurar que es un conjunto de tuplas

        # Validar que todos los elementos de la relación están en el conjunto
        self._validar_relacion()

    def _validar_relacion(self):

        """
        Valida que todos los elementos de la relación pertenezcan al conjunto.

        Raises:
            ValueError: Si algún elemento de la relación no está en el conjunto
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

        Returns:
            tuple: (bool, str) - (resultado, justificación)
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

        Returns:
            tuple: (bool, str) - (resultado, justificación)
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

        Returns:
            tuple: (bool, str) - (resultado, justificación)
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
        Una relación R es antisimétrica si para todo (a,b) ∈ R y (b,a) ∈ R, entonces a = b.

        Returns:
            tuple: (bool, str) - (resultado, justificación)
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
        Una relación R es transitiva si para todo (a,b) ∈ R y (b,c) ∈ R, entonces (a,c) ∈ R.

        Returns:
            tuple: (bool, str) - (resultado, justificación)
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

        Returns:
            tuple: (bool, str) - (resultado, justificación detallada)
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

    def analizar_propiedades(self):
        """
        Realiza un análisis completo de todas las propiedades de la relación.

        Returns:
            dict: Diccionario con todas las propiedades analizadas
        """
        return {
            'reflexiva': self.es_reflexiva(),
            'irreflexiva': self.es_irreflexiva(),
            'simetrica': self.es_simetrica(),
            'asimetrica': self.es_asimetrica(),
            'antisimetrica': self.es_antisimetrica(),
            'transitiva': self.es_transitiva(),
            'orden_parcial': self.es_orden_parcial()
        }


    def generar_diagrama_hasse(self):
        """
        Genera el diagrama de Hasse para un orden parcial.
        Elimina las aristas transitivas y reflexivas para mostrar solo la estructura mínima.

        Returns:
            tuple: (bool, str/dict) - (es_orden_parcial, diagrama_o_error)
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

        Args:
            grafo (dict): Grafo del diagrama de Hasse
            elementos (set): Conjunto de elementos

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


