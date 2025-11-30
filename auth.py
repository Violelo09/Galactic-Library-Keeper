"""
auth.py → inicio de sesión
"""

import csv

# Autenticacion de usuario
def leer_usuario():
    try:
        admin_access = {}
        
        with open("admin_access.csv", "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) >= 2:
                    admin_access[fila[0]] = fila[1]
        
        return admin_access
    
    except FileNotFoundError:
        print("Error: No se encontrado el archivo admin_access.csv")
        return {}
    except Exception as e:
        print(f"Error al leer usuarios: {e}")
        return {}


# Validar credenciales
def validar_credenciales(usuario, contrasena):
    usuarios = leer_usuario()
    return usuario in usuarios and usuarios[usuario] == contrasena


# Inicio de sesion 
def inicio_sesion():
    intentos = 0
    max_intentos = 3

    print("\n" + "="*50)
    print("INICIO DE SESIÓN")
    print("="*50)
    
    while intentos < max_intentos:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        if validar_credenciales(usuario, contrasena):
            print("\n✓ Inicio de sesión exitoso!")
            return True
        else:
            intentos += 1
            intentos_restantes = max_intentos - intentos

            if intentos_restantes > 0:
                print(f"\n✗ Credenciales incorrectas. Te quedan {intentos_restantes} intento(s).")
            else:
                print("\n✗ Credenciales incorrectas. Se agotaron los intentos.")
    
    print("Cerrando el programa...")
    return False