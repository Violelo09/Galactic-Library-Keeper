import csv

# Autenticacion de usuario
def leer_usuario():
    try:
        admin_access = {}
        
        with open('admin_access.csv', "r", newline="",encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for datos in lector:
                print(datos) 
        
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

    if usuarioDelArchivoCSV == usuario and contrasenaDelArchivoCSV == contrasena:
        return True
    else:
        return False


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
            print("\nInicio de sesión exitoso!")
            return True
        else:
            intentos += 1
            intentos_restantes = max_intentos - intentos

            if intentos_restantes > 0:
                print(f"\nCredenciales incorrectas. Te quedan {intentos_restantes} intento(s).")
            else:
                print("\nCredenciales incorrectas. Se agotaron los intentos.")
    
    print("Cerrando el programa...")
    return False


inicio_sesion()
