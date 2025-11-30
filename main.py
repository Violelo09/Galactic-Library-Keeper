"""
main.py → menú principal
"""

from auth import inicio_sesion
from visitors import (
    registrar_visitante,
    listar_visitantes,
    buscar_visitante_por_id,
    actualizar_estado,
    eliminar_visitante,
    mostrar_estadisticas
)


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*60)
    print(" "*10 + "SISTEMA DE VISITANTES INTERGALÁCTICOS")
    print("="*60)
    print("  [1] Registrar nuevo visitante")
    print("  [2] Listar todos los visitantes")
    print("  [3] Buscar visitante por ID")
    print("  [4] Actualizar estado de visitante")
    print("  [5] Eliminar visitante")
    print("  [6] Ver estadísticas del sistema")
    print("  [7] Salir")
    print("="*60)


def menu_principal():
    """
    Controla el flujo principal del programa
    Muestra el menú y ejecuta las opciones seleccionadas
    """
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            registrar_visitante()
        elif opcion == "2":
            listar_visitantes()
        elif opcion == "3":
            buscar_visitante_por_id()
        elif opcion == "4":
            actualizar_estado()
        elif opcion == "5":
            eliminar_visitante()
        elif opcion == "6":
            mostrar_estadisticas()
        elif opcion == "7":
            print("\n" + "="*60)
            print(" "*15 + "¡HASTA LUEGO!")
            print("  Gracias por usar el sistema TechLab")
            print("="*60)
            break
        else:
            print("\n✗ ERROR: Opción inválida. Por favor selecciona 1-7")
        
        # Pausa para que el usuario vea el resultado
        input("\nPresiona ENTER para continuar...")


def main():
    """
    Función principal del programa
    1. Autentica al usuario
    2. Si es exitoso, muestra el menú principal
    """
    print("\n" + "="*60)
    print(" "*15 + "SISTEMA TECHLAB")
    print(" "*10 + "Gestión de Visitantes Intergalácticos")
    print("="*60)
    
    # Autenticación requerida
    if inicio_sesion():
        print("\nBienvenido al sistema")
        menu_principal()
    else:
        print("\nAcceso denegado")
        print("El programa se cerrará por seguridad")


# Punto de entrada del programa (CORRECCIÓN: Faltaba llamar a main())
if __name__ == "__main__":
    main()