import csv
import random

def algo():
    
    try:
        with open("admin_access.csv", "r", encoding="utf-8") as archivo:
            
            archivo.readline()
            
            linea = archivo.readline()
            linea = linea.strip().split(",")
            
            usuario = input("Ingrese su usuario: ").strip()
            contrasena = input("Ingrese su contraseña: ").strip()
  
            if usuario == linea[0].strip() and contrasena == linea[1].strip():
                print("Acceso concedido")
            else:
                print("Acceso denegado")
                
    except:  # noqa: E722
        print("Error al leer el archivo")

algo()


def  usuario():
    try:
        id_visitante = random.randint(1000, 9999)
        
        # Pedir todos los datos
        nombre = input("Di tu nombre: ")
        especie = input("Dime tu especie: ")
        estado = input("Estado (Activo/Retirado): ")
        
        # Abrir archivo en modo append y escribir
        with open("visitantes.csv", "a", encoding="utf-8", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([id_visitante, nombre, especie, estado])
        
        print(f"Visitante registrado con ID: {id_visitante}")
    
    except Exception as e:
        print(f"Error: {e}")
        
usuario()