"""
Trabajo Práctico Integrador 
Programación 1  
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas
"""
import csv


#Funciones
def cargar_datos():
    """Carga los Datos desde el Archivo CSV"""

    with open('Información Geografica.csv', mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            pais = {f"nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]}
            paises.append(pais)

    return paises

def mostrar_paises(paises):
    """Muestra todos los países"""

    for pais in paises:
        print(pais)


#Funciones de Validación
def validar_opcion(opcion):
    """Valida que la Opción del Menú"""

    while opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Error: Opción inválida.")
        opcion = input("Seleccione una opción: ")

    return opcion


#Funciones del Menú
def muestra_menu():
    """Esta Función Muestra el Menú Principal"""
    print("Menu")
    print("1. Agregar País")
    print("2. Actualizar País")
    print("3. Buscar País")
    print("4. Filtrar Países")
    print("5. Ordenar Países")
    print("6. Mostrar estadísticas")
    print("7. Salir")

def pedir_opcion():
    """Solicita una Opción del Menú"""

    opcion = input("Seleccione una opción: ")
    return opcion


#Programa Principal
paises = [] #Lista con el Contenido


while True: #Menú Interactivo
    muestra_menu()
    opcion = pedir_opcion()
    opcion = validar_opcion(opcion)


    if opcion == "7":
        print("Programa Cerrado")
        break
