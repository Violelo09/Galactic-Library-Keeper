import csv

# Leer el programa (AQUÍ FALTABA EL "def")
def leer_visitantes():
    try:
        visitantes = []
        
        with open("visitantes.csv", "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) >= 4:
                    visitante = (fila[0], fila[1], fila[2], fila[3])
                    visitantes.append(visitante)
        
        return visitantes
    
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"\n✗ ERROR al leer visitantes: {e}")
        return []