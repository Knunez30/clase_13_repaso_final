import csv
import pandas as pd
import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola v1."""
    if os.name == "nt":  # Para Windows
        os.system("cls")
    else:  # Para Unix/Linux/Mac
        os.system("clear")
def menu ():
    """Función principal del menú del sistema de gestión de datos de ventas."""
    while True:
        limpiar_pantalla()
        print("\n --- Menu Principal ---")
        print("1. Cargar datos de ventas desde un archivo CSV")
        print("2. Mostrar estadísticas de ventas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break


if __name__ == "__main__":
    print ("Bienvenido al sistema de gestión de datos de ventas.")
    menu()