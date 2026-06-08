"""
Trabajo Práctico Integrador 
Programación 1  
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas
"""
import csv


#Funciones
def cargar_datos():
    """Carga los Datos desde el Archivo CSV"""

    paises = []

    try:
        with open('Información Geografica.csv', mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                pais = {f"nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]}
                paises.append(pais)

    except FileNotFoundError:
            print("Error: No se encontró el archivo.")

    except Exception as e:
            print(f"Error inesperado: {e}")

    return paises

def mostrar_paises(paises):
    """Muestra todos los países"""

    for pais in paises:
        print(pais)

def buscar_pais(paises, nombre):
    """Esta Función Busca Países en la Lista"""
    for pais in paises:
        if pais["nombre"] == nombre:
            return pais

    return None

#Funciones de Validación
def validar_opcion():
    """Solicita y valida la opción del menú"""

    while True:
        try:
            opcion = input("Seleccione una opción: ")

            if opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
                raise ValueError("Debe ingresar una opción entre 1 y 7")

            return opcion

        except ValueError as e:
            print(f"Error de ingreso: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

def validar_pais():
    """Solicita y valida el nombre del país"""

    while True:
        try:
            nombre = input("Ingrese el nombre del país: ").strip().title()

            if nombre == "":
                raise ValueError("El nombre no puede estar vacío")

            if not nombre.replace(" ", "").isalpha():
                raise ValueError("El nombre solo puede contener letras")

            if buscar_pais(paises, nombre) is not None:
                raise ValueError("El país ya existe")

            return nombre

        except ValueError as e:
            print(f"Error de ingreso: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

def validar_poblacion():
    """Solicita y valida la población"""

    while True:
        try:
            poblacion = int(input("Ingrese la cantidad de población: "))

            if poblacion <= 0:
                raise ValueError("Debe ingresar un número mayor que cero")

            return poblacion

        except ValueError as e:
            print(f"Error de ingreso: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

def validar_superficie():
    """Solicita y valida la superficie"""

    while True:
        try:
            superficie = int(input("Ingrese la cantidad de superficie: "))

            if superficie <= 0:
                raise ValueError("Debe ingresar un número mayor que cero")

            return superficie

        except ValueError as e:
            print(f"Error de ingreso: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

def validar_continente():
    """Solicita y valida el continente"""

    continentes = ["America", "Europa", "Asia", "Oceania", "Africa"]

    while True:
        try:
            continente = input("Ingrese el continente: ").strip().title()

            if continente == "":
                raise ValueError("El continente no puede estar vacío")

            if not continente.replace(" ", "").isalpha():
                raise ValueError("El continente solo puede contener letras")

            if continente not in continentes:
                raise ValueError("Continente inválido")

            return continente

        except ValueError as e:
            print(f"Error de ingreso: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

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

def agregar_pais():
    """Esta Función Agrega un País"""

    nombre = validar_pais()
    poblacion = validar_poblacion()
    superficie = validar_superficie()
    continente = validar_continente()

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    print("País agregado correctamente.")

def actualizar_pais():
    """Esta Función Actuliza los Datos de Población y Superficie"""

    try:
        nombre = input("Ingrese el país a actualizar: ").strip().title()
        pais = buscar_pais(paises, nombre)

        if pais is None:
            print("País no encontrado.")
            return

        nueva_poblacion = validar_poblacion()
        nueva_superficie = validar_superficie()

        pais["poblacion"] = nueva_poblacion
        pais["superficie"] = nueva_superficie

        print("País actualizado correctamente.")


    except Exception as e:
            print(f"Error inesperado: {e}")

def mostrar_pais():
    """Esta Función Muestra la Información del País"""

    try:
        nombre = input("Ingrese el nombre del país: ").strip().title()

        pais = buscar_pais(paises, nombre)

        if pais is None:
            print("País no encontrado.")
            return

        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']}")
        print(f"Continente: {pais['continente']}")

    except Exception as e:
        print(f"Error inesperado: {e}")


#Programa Principal
paises = cargar_datos()  #Lista con el Contenido


while True: #Menú Interactivo
    muestra_menu()
    opcion = validar_opcion()

    if opcion == "1": #Menú de Opciones
        agregar_pais()

    elif opcion == "2":
        actualizar_pais()

    elif opcion == "3":
        mostrar_pais()

    elif opcion == "7":
        print("Programa Cerrado")
        break

mostrar_paises(paises)