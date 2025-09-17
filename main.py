import os
from data.iodata import pedir_relacion, pedir_conjunto, mostrar_ejemplos
from graficos.mostrar import mostrar_analisis_completo

def menu():
    os.system('clear')
    while True:
        print("\n\033[96m" + "="*30)
        print("         MENÚ PRINCIPAL")
        print("    PROPIEDADES DE RELACIONES")
        print("="*30 + "\033[0m")
        print("\033[93m1.\033[0m Analizar relación propia")
        print("\033[93m2.\033[0m Ver ejemplos")
        print("\033[93m3.\033[0m Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            conjunto = pedir_conjunto()
            relacion = pedir_relacion(conjunto)
            mostrar_analisis_completo(conjunto, relacion)
        elif opcion == "2":
            mostrar_ejemplos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
