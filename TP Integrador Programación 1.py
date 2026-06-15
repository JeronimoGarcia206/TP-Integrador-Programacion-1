"""
Trabajo Práctico Integrador 
Programación 1  
Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas
"""
import csv

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

def validar_opcion_filtros():
    """Solicita y Valida la Opción del Menú de Filtros"""

    while True:
        try:
            opcion = input("Seleccione una opción: ")

            if opcion not in ["1", "2", "3"]:
                raise ValueError("Debe ingresar una opción entre 1 y 3")

            return opcion

        except ValueError as e:
            print(f"Error de ingreso: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

def validar_opcion_orden():
    """Esta Función Solicita y Valida la Opción del Menú de Orden"""

    while True:
        try:
            opcion = input("Seleccione una opción: ")

            if opcion not in ["1", "2", "3"]:
                raise ValueError("Debe ingresar una opción entre 1 y 3")

            return opcion

        except ValueError as e:
            print(f"Error de ingreso: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

def validar_sentido():
    """Valida el Sentido del Orden"""

    while True:
        try:
            opcion = input("Seleccione una opción: ")

            if opcion not in ["1", "2"]:
                raise ValueError("Debe ingresar 1 o 2")

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

#Funciones De Los Menús
def menu_filtros():
    """Esta Función Muestra el Menú de Filtros"""

    print("Filtros")
    print("1. Continente")
    print("2. Rango de Población")
    print("3. Rango de Superficie")

def menu_orden():
    """Muestra el Menú de Orden"""

    print("Ordenar por")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

def menu_sentido():
    """Muestra el Sentido del Orden"""

    print("1. Ascendente")
    print("2. Descendente")


#Funciones De Las Opciones
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

def filtrar_continente():
    """Esta Función Filtra por Continente"""

    continente = validar_continente()

    encontrados = False

    for pais in paises:

        if pais["continente"] == continente:
            print(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron países.")

def filtrar_poblacion():
    """Esta Función Filtra por Población"""

    try:
        print("Ingrese la población mínima")
        minimo = validar_poblacion()
        print("Ingrese la población máxima")
        maximo = validar_poblacion()

        if minimo > maximo:
            print("El mínimo no puede ser mayor que el máximo.")
            return

        encontrados = False

        for pais in paises:

            if minimo <= pais["poblacion"] <= maximo:
                print(pais)
                encontrados = True

        if not encontrados:
            print("No se encontraron países.")

    except Exception as e:
        print(f"Error inesperado: {e}")

def filtrar_superficie():
    """Esta Función Filtra por Superficie"""
    
    try:
        print("Ingrese la superficie mínima")
        minimo = validar_superficie()
        print("Ingrese la superficie máxima")
        maximo = validar_superficie()

        if minimo > maximo:
            print("El mínimo no puede ser mayor que el máximo.")
            return

        encontrados = False

        for pais in paises:

            if minimo <= pais["superficie"] <= maximo:
                print(pais)
                encontrados = True

        if not encontrados:
            print("No se encontraron países.")

    except Exception as e:
        print(f"Error inesperado: {e}")


    """Muestra el Sentido del Orden"""

    print("1. Ascendente")
    print("2. Descendente")

def ordenar_nombre():
    """Esta Función Permite Ordenar por Nombre"""

    try:
        paises_ordenados = paises.copy()

        menu_sentido()
        sentido = validar_sentido()

        for i in range(len(paises_ordenados)):

            for j in range(i + 1, len(paises_ordenados)):

                if sentido == "1":

                    if paises_ordenados[i]["nombre"] > paises_ordenados[j]["nombre"]:

                        aux = paises_ordenados[i]
                        paises_ordenados[i] = paises_ordenados[j]
                        paises_ordenados[j] = aux

                else:

                    if paises_ordenados[i]["nombre"] < paises_ordenados[j]["nombre"]:

                        aux = paises_ordenados[i]
                        paises_ordenados[i] = paises_ordenados[j]
                        paises_ordenados[j] = aux

        mostrar_paises(paises_ordenados)

    except Exception as e:
        print(f"Error inesperado: {e}")

def ordenar_poblacion():
    """Esta Función Permite Ordenar por Población"""

    try:
        paises_ordenados = paises.copy()

        menu_sentido()
        sentido = validar_sentido()

        for i in range(len(paises_ordenados)):

            for j in range(i + 1, len(paises_ordenados)):

                if sentido == "1":

                    if paises_ordenados[i]["poblacion"] > paises_ordenados[j]["poblacion"]:

                        aux = paises_ordenados[i]
                        paises_ordenados[i] = paises_ordenados[j]
                        paises_ordenados[j] = aux

                else:

                    if paises_ordenados[i]["poblacion"] < paises_ordenados[j]["poblacion"]:

                        aux = paises_ordenados[i]
                        paises_ordenados[i] = paises_ordenados[j]
                        paises_ordenados[j] = aux

        mostrar_paises(paises_ordenados)

    except Exception as e:
        print(f"Error inesperado: {e}")

def ordenar_superficie():
    """Esta Función Permite Ordenar por Superficie"""

    try:
        paises_ordenados = paises.copy()

        menu_sentido()
        sentido = validar_sentido()

        for i in range(len(paises_ordenados)):

            for j in range(i + 1, len(paises_ordenados)):

                if sentido == "1":

                    if paises_ordenados[i]["superficie"] > paises_ordenados[j]["superficie"]:

                        aux = paises_ordenados[i]
                        paises_ordenados[i] = paises_ordenados[j]
                        paises_ordenados[j] = aux

                else:

                    if paises_ordenados[i]["superficie"] < paises_ordenados[j]["superficie"]:

                        aux = paises_ordenados[i]
                        paises_ordenados[i] = paises_ordenados[j]
                        paises_ordenados[j] = aux

        mostrar_paises(paises_ordenados)

    except Exception as e:
        print(f"Error inesperado: {e}")


#Funciones del Menú Principal
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

    try:
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

    except Exception as e:
            print(f"Error inesperado: {e}")

def actualizar_pais():
    """Esta Función Actualiza los Datos de Población y Superficie"""

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

def filtrar_paises():
    """Esta Función Permite Aplicar Distintos Filtros de Búsqueda"""

    menu_filtros()
    opcion = validar_opcion_filtros()

    if opcion == "1":
        filtrar_continente()

    elif opcion == "2":
        filtrar_poblacion()

    elif opcion == "3":
        filtrar_superficie()

def ordenar_paises():
    """Esta Función Permite Ordenar de Distintas Maneras"""

    menu_orden()

    opcion = validar_opcion_orden()

    if opcion == "1":
        ordenar_nombre()

    elif opcion == "2":
        ordenar_poblacion()

    elif opcion == "3":
        ordenar_superficie()

def mostrar_estadisticas():
    """Esta Función Muestra Estadísticas de los Países"""

    mayor = paises[0]
    menor = paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    continentes = {}

    for pais in paises:

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print(f"País con mayor población: {mayor['nombre']} - {mayor['poblacion']}")
    print(f"País con menor población: {menor['nombre']} - {menor['poblacion']}") 
    print(f"Promedio de población: {promedio_poblacion:.0f}")
    print(f"Promedio de superficie: {promedio_superficie:.0f}")

    print("Cantidad de países por continente")

    for continente, cantidad in continentes.items():
        print(continente, ":", cantidad)


#Programa Principal
paises = cargar_datos()  #Lista con el Contenido


#Menú Interactivo
while True: 
    muestra_menu() #Menú de Opciones
    opcion = validar_opcion()

    if opcion == "1": #Permite Agregar País
        agregar_pais()

    elif opcion == "2": #Permite Actualizar País
        actualizar_pais()

    elif opcion == "3": #Muestra el País Seleccionado
        mostrar_pais()

    elif opcion == "4": #Realiza Distintos Filtros
        filtrar_paises()

    elif opcion == "5": #Ordena de Distintas Maneras
        ordenar_paises()

    elif opcion == "6": #Muestra Estadisticas
        mostrar_estadisticas()

    elif opcion == "7": #Cierra el Programa
        print("Programa Cerrado")
        break
