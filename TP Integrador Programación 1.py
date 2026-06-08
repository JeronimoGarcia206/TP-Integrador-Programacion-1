"""
Trabajo Práctico Integrador 
Programación 1  
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas
"""

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

while True:
    muestra_menu()
    opcion = pedir_opcion()
    opcion = validar_opcion(opcion)


    if opcion == "7":
        print("Programa Cerrado")
        break