from graficos.mostrar import mostrar_analisis_completo

def pedir_conjunto():
    entrada = input("Introduce los elementos del conjunto separados por coma (ejemplo: 1,2,3): ")
    elementos = [e.strip() for e in entrada.split(",")] # Limpiar espacios y guardar en lista
    try:
        elementos = [int(e) for e in elementos] #Convertir a enteros si es posible
    except ValueError:
        pass
    return set(elementos)

def pedir_relacion(conjunto):
    print("Introduce los pares de la relación uno por uno. Ejemplo para (1,2): 1,2")
    print("Escribe 'fin' para terminar.")
    relacion = set()
    while True:
        entrada = input("Par: ")
        if entrada.lower() == "fin":
            break
        try:
            a, b = [e.strip() for e in entrada.split(",")]
            try:
                a, b = int(a), int(b)
            except ValueError:
                pass
            if a in conjunto and b in conjunto:
                relacion.add((a, b))
            else:
                print("Ambos elementos deben estar en el conjunto.")
        except Exception:
            print("Formato incorrecto. Usa: elemento1,elemento2")
    return relacion

def mostrar_ejemplos():
    while True:
        print("\n" + "="*50)
        print("           MENÚ DE EJEMPLOS")
        print("="*50)
        print("1. Ejemplos de Órdenes Parciales")
        print("2. Ejemplos de Relaciones de Equivalencia")
        print("3. Contraejemplos")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_ejemplos_orden_parcial()
        elif opcion == "2":
            mostrar_ejemplos_equivalencia()
        elif opcion == "3":
            mostrar_contraejemplos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def mostrar_ejemplos_orden_parcial():
    print("\n" + "="*60)
    print("EJEMPLOS DE ÓRDENES PARCIALES")
    print("="*60)

    print("\nEJEMPLO 1: Divisores de 12 con relación 'divide a'")
    print("-" * 50)
    conjunto1 = {"1", "2", "3", "4", "6", "12"}
    relacion1 = {
        # Reflexiva
        ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("6", "6"), ("12", "12"),
        # Divisibilidad
        ("1", "2"), ("1", "3"), ("1", "4"), ("1", "6"), ("1", "12"),
        ("2", "4"), ("2", "6"), ("2", "12"),
        ("3", "6"), ("3", "12"),
        ("4", "12"), ("6", "12")
    }
    mostrar_analisis_completo(conjunto1, relacion1)

    print("\n" + "="*70 + "\n")

    print("EJEMPLO 2: Inclusión de conjuntos")
    print("-" * 40)
    conjunto2 = {"∅", "{1}", "{2}", "{1,2}"}
    relacion2 = {
        # Reflexiva
        ("∅", "∅"), ("{1}", "{1}"), ("{2}", "{2}"), ("{1,2}", "{1,2}"),
        # Inclusión
        ("∅", "{1}"), ("∅", "{2}"), ("∅", "{1,2}"),
        ("{1}", "{1,2}"), ("{2}", "{1,2}")
    }
    mostrar_analisis_completo(conjunto2, relacion2)

def mostrar_ejemplos_equivalencia():
    print("\n" + "="*60)
    print("EJEMPLOS DE RELACIONES DE EQUIVALENCIA")
    print("="*60)

    print("\nEJEMPLO 1: Congruencia módulo 3")
    print("-" * 35)
    conjunto1 = {"0", "1", "2", "3", "4", "5"}
    relacion1 = {
        # Reflexiva
        ("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"),
        # Clases de equivalencia módulo 3
        ("0", "3"), ("3", "0"),    # Clase [0]: resto 0
        ("1", "4"), ("4", "1"),    # Clase [1]: resto 1
        ("2", "5"), ("5", "2")     # Clase [2]: resto 2
    }
    print("Relación: a ≡ b (mod 3)")
    mostrar_analisis_completo(conjunto1, relacion1)

    print("\n" + "="*70 + "\n")

    print("EJEMPLO 2: Misma longitud en palabras")
    print("-" * 40)
    conjunto2 = {"a", "ab", "abc", "xy", "z", "def"}
    relacion2 = {
        # Reflexiva
        ("a", "a"), ("ab", "ab"), ("abc", "abc"), ("xy", "xy"), ("z", "z"), ("def", "def"),
        # Misma longitud
        ("a", "z"), ("z", "a"),           # Longitud 1
        ("ab", "xy"), ("xy", "ab"),       # Longitud 2
        ("abc", "def"), ("def", "abc")    # Longitud 3
    }
    print("Relación: misma longitud")
    mostrar_analisis_completo(conjunto2, relacion2)

    print("\n" + "="*70 + "\n")

    print("EJEMPLO 3: Misma paridad")
    print("-" * 25)
    conjunto3 = {"1", "2", "3", "4", "5", "6"}
    relacion3 = {
        # Reflexiva
        ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"),
        # Misma paridad
        ("1", "3"), ("3", "1"), ("1", "5"), ("5", "1"), ("3", "5"), ("5", "3"), # Impares
        ("2", "4"), ("4", "2"), ("2", "6"), ("6", "2"), ("4", "6"), ("6", "4")  # Pares
    }
    print("Relación: misma paridad (par/impar)")
    mostrar_analisis_completo(conjunto3, relacion3)

def mostrar_contraejemplos():
    print("\n" + "="*60)
    print("CONTRAEJEMPLOS")
    print("="*60)

    print("\nCONTRAEJEMPLO 1: No es orden parcial (falta reflexividad)")
    print("-" * 55)
    conjunto1 = {"1", "2", "3", "4"}
    relacion1 = {
        # Orden estricto (NO reflexivo)
        ("1", "2"), ("1", "3"), ("1", "4"),
        ("2", "3"), ("2", "4"),
        ("3", "4")
    }
    mostrar_analisis_completo(conjunto1, relacion1)

    print("\n" + "="*70 + "\n")

    print("CONTRAEJEMPLO 2: No es orden parcial (falta antisimetría)")
    print("-" * 55)
    conjunto2 = {"A", "B", "C", "D"}
    relacion2 = {
        # Reflexiva
        ("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"),
        # Relaciones con ciclo
        ("A", "B"), ("A", "C"), ("C", "D"),
        ("B", "D"), ("D", "B")  # Ciclo que viola antisimetría
    }
    mostrar_analisis_completo(conjunto2, relacion2)

    print("\n" + "="*70 + "\n")

    print("CONTRAEJEMPLO 3: No es equivalencia (falta transitividad)")
    print("-" * 55)
    conjunto3 = {"1", "2", "3", "4"}
    relacion3 = {
        # Reflexiva
        ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),
        # Simétrica pero NO transitiva
        ("1", "2"), ("2", "1"),
        ("2", "3"), ("3", "2"),
        ("3", "4"), ("4", "3")
        # Falta transitividad: (1,3), (3,1), (2,4), (4,2), (1,4), (4,1)
    }
    mostrar_analisis_completo(conjunto3, relacion3)
