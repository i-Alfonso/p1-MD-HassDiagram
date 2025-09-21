from graficos.mostrar import mostrar_analisis_completo

def pedir_conjunto():
    entrada = input("Introduce los elementos del conjunto separados por coma (ejemplo: 1,2,3): ")
    elementos = [e.strip() for e in entrada.split(",")]
    try:
        elementos = [int(e) for e in elementos]
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
        print("EJEMPLOS DE RELACIONES")
        print("="*50)
        print("1. Orden parcial - Divisores de 12")
        print("2. Orden parcial - Inclusión de conjuntos")
        print("3. Equivalencia - Congruencia módulo 3")
        print("4. Equivalencia - Misma paridad")
        print("5. Relación general - Grafo arbitrario")
        print("6. Contraejemplo - No reflexiva")
        print("7. Contraejemplo - No antisimétrica")
        print("8. Volver al menú principal")

        opcion = input("Elige un ejemplo: ")

        if opcion == "1":
            ejemplo_divisores()
        elif opcion == "2":
            ejemplo_inclusion()
        elif opcion == "3":
            ejemplo_congruencia_modulo()
        elif opcion == "4":
            ejemplo_paridad()
        elif opcion == "5":
            ejemplo_grafo_general()
        elif opcion == "6":
            ejemplo_no_reflexiva()
        elif opcion == "7":
            ejemplo_no_antisimetrica()
        elif opcion == "8":
            break
        else:
            print("Opción no válida.")

def ejemplo_divisores():
    print("\nEJEMPLO 1: Divisores de 12 con relación 'divide a'")
    print("-" * 50)

    conjunto1 = {"1", "2", "3", "4", "6", "12"}
    relacion1 = {
        ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("6", "6"), ("12", "12"),
        ("1", "2"), ("1", "3"), ("1", "4"), ("1", "6"), ("1", "12"),
        ("2", "4"), ("2", "6"), ("2", "12"),
        ("3", "6"), ("3", "12"),
        ("4", "12"),
        ("6", "12")
    }

    print("A = {1, 2, 3, 4, 6, 12}")
    print("Relación: 'a divide a b' (a|b)")
    mostrar_analisis_completo(conjunto1, relacion1)

def ejemplo_inclusion():
    print("\nEJEMPLO 2: Inclusión de conjuntos")
    print("-" * 50)

    conjunto = {"∅", "{1}", "{2}", "{1,2}"}
    relacion = {
        ("∅", "∅"), ("{1}", "{1}"), ("{2}", "{2}"), ("{1,2}", "{1,2}"),
        ("∅", "{1}"), ("∅", "{2}"), ("∅", "{1,2}"),
        ("{1}", "{1,2}"),
        ("{2}", "{1,2}")
    }

    print("A = {∅, {1}, {2}, {1,2}}")
    print("Relación: inclusión de conjuntos (⊆)")
    mostrar_analisis_completo(conjunto, relacion)

def ejemplo_congruencia_modulo():
    print("\nEJEMPLO 3: Congruencia módulo 3")
    print("-" * 50)

    conjunto = {0, 1, 2, 3, 4, 5, 6, 7, 8}
    relacion = set()

    # Agregar pares reflexivos
    for a in conjunto:
        relacion.add((a, a))

    # Agregar pares equivalentes (mismo resto mod 3)
    for a in conjunto:
        for b in conjunto:
            if a % 3 == b % 3 and a != b:
                relacion.add((a, b))

    print("A = {0, 1, 2, 3, 4, 5, 6, 7, 8}")
    print("Relación: a ≡ b (mod 3)")
    print("Clases esperadas: [0,3,6], [1,4,7], [2,5,8]")
    mostrar_analisis_completo(conjunto, relacion)

def ejemplo_paridad():
    print("\nEJEMPLO 4: Misma paridad")
    print("-" * 50)

    conjunto = {1, 2, 3, 4, 5, 6, 7, 8}
    relacion = set()

    # Pares reflexivos
    for a in conjunto:
        relacion.add((a, a))

    # Pares con misma paridad
    for a in conjunto:
        for b in conjunto:
            if a % 2 == b % 2 and a != b:
                relacion.add((a, b))

    print("A = {1, 2, 3, 4, 5, 6, 7, 8}")
    print("Relación: misma paridad")
    print("Clases esperadas: [1,3,5,7] (impares), [2,4,6,8] (pares)")
    mostrar_analisis_completo(conjunto, relacion)

def ejemplo_grafo_general():
    print("\nEJEMPLO 5: Relación general")
    print("-" * 50)

    conjunto = {"A", "B", "C", "D", "E"}
    relacion = {
        ("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"),
        ("A", "B"), ("B", "C"), ("C", "D"),
        ("A", "E"), ("E", "B"),
        ("D", "E")
    }

    print("A = {A, B, C, D, E}")
    print("Relación: grafo arbitrario")
    print("Esta relación no es orden parcial ni equivalencia")
    mostrar_analisis_completo(conjunto, relacion)

def ejemplo_no_reflexiva():
    print("\nCONTRAEJEMPLO 1: Relación no reflexiva")
    print("-" * 50)

    conjunto = {"1", "2", "3", "4"}
    relacion = {
        ("1", "2"), ("1", "3"), ("1", "4"),
        ("2", "3"), ("2", "4"),
        ("3", "4")
    }

    print("A = {1, 2, 3, 4}")
    print("Relación: < (menor que estricto)")
    print("Falla por no ser reflexiva")
    mostrar_analisis_completo(conjunto, relacion)

def ejemplo_no_antisimetrica():
    print("\nCONTRAEJEMPLO 2: Relación no antisimétrica")
    print("-" * 50)

    conjunto = {"A", "B", "C", "D"}
    relacion = {
        ("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"),
        ("A", "B"), ("A", "C"),
        ("C", "D"),
        ("B", "D"), ("D", "B")  # Viola antisimetría
    }

    print("A = {A, B, C, D}")
    print("Relación: con ciclos bidireccionales")
    print("Falla por no ser antisimétrica")
    mostrar_analisis_completo(conjunto, relacion)
