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
    print("EJEMPLO 1: Relación de orden parcial")
    print("=" * 50)
    conjunto1 = {1, 2, 3, 4}
    relacion1 = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (1, 3), (1, 4), (2, 4)}
    mostrar_analisis_completo(conjunto1, relacion1)

    print("\n" + "=" * 70 + "\n")

    print("EJEMPLO 2: Relación simétrica (no es orden parcial)")
    print("=" * 50)
    conjunto2 = {'a', 'b', 'c'}
    relacion2 = {('a', 'a'), ('b', 'b'), ('c', 'c'), ('a', 'b'), ('b', 'a')}
    mostrar_analisis_completo(conjunto2, relacion2)

    print("\n" + "=" * 70 + "\n")

    print("EJEMPLO 3: Relación asimétrica")
    print("=" * 50)
    conjunto3 = {1, 2, 3}
    relacion3 = {(1, 2), (2, 3)}
    mostrar_analisis_completo(conjunto3, relacion3)