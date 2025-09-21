import os
from data.iodata import pedir_relacion, pedir_conjunto, mostrar_ejemplos
from graficos.mostrar import mostrar_analisis_completo, mostrar_solo_grafo, mostrar_clases_equivalencia

def menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    while True:
        print("\n" + "="*40)
        print("         MENÚ PRINCIPAL")
        print("    ANALIZADOR DE RELACIONES")
        print("="*40)
        print("1. Analizar relación propia")
        print("2. Ver ejemplos")
        print("3. Análisis rápido de grafo")
        print("4. Solo clases de equivalencia")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            analizar_relacion_propia()
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            analisis_rapido_grafo()
        elif opcion == "4":
            analisis_equivalencia()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

def analizar_relacion_propia():
    print("\n" + "="*50)
    print("ANÁLISIS COMPLETO DE RELACIÓN")
    print("="*50)

    conjunto = pedir_conjunto()
    relacion = pedir_relacion(conjunto)

    print("\n" + "="*50)
    mostrar_analisis_completo(conjunto, relacion)

    input("\nPresiona Enter para continuar...")

def analisis_rapido_grafo():
    print("\n" + "="*50)
    print("VISUALIZACIÓN RÁPIDA DE GRAFO")
    print("="*50)
    print("Genera solo el grafo sin análisis detallado")

    conjunto = pedir_conjunto()
    relacion = pedir_relacion(conjunto)

    print("\n" + "="*30)
    mostrar_solo_grafo(conjunto, relacion)

    input("\nPresiona Enter para continuar...")

def analisis_equivalencia():
    print("\n" + "="*50)
    print("ANÁLISIS DE CLASES DE EQUIVALENCIA")
    print("="*50)
    print("Verifica si es relación de equivalencia y muestra clases")

    conjunto = pedir_conjunto()
    relacion = pedir_relacion(conjunto)

    print("\n" + "="*30)
    datos = mostrar_clases_equivalencia(conjunto, relacion)

    if datos:
        print(f"\nPartición del conjunto en {datos['num_clases']} clases:")
        for i, clase in enumerate(datos['clases'], 1):
            print(f"  Clase {i}: {{{', '.join(map(str, clase))}}}")

    input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu()
