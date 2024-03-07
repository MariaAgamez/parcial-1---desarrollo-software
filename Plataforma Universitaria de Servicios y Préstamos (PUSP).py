import os
from getpass import getpass
import time

# Base de datos de usuarios y contraseñas (diccionario)
USUARIOS = {
    'estudiante1': 'contrasena1',
    'estudiante2': 'contrasena2',
    'administrador1': 'adminpass1',
    'administrador2': 'adminpass2'
}

# Función para limpiar la pantalla de la terminal
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el mensaje de bienvenida
def mostrar_bienvenida():
    limpiar_pantalla()
    print("=" * 65)
    print("¡Bienvenido a la Plataforma Universitaria de Servicios y Préstamos!")
    print("=" * 65)

# Función para el inicio de sesión
def iniciar_sesion():
    mostrar_bienvenida()
    print("\nInicio de Sesión")
    tipo_usuario = input("Seleccione el tipo de usuario (estudiante/administrador): ").lower()

    if tipo_usuario not in ['estudiante', 'administrador']:
        input("\nError: Tipo de usuario no válido. Presione Enter para continuar...")
        return None

    usuario = input("Usuario: ")
    contrasena = getpass("Contraseña: ")

    if usuario in USUARIOS and USUARIOS[usuario] == contrasena:
        return tipo_usuario, usuario
    else:
        input("Error: Usuario o contraseña incorrectos. Presione Enter para continuar...")
        return None

# Función para mostrar el menú de opciones de estudiante
def mostrar_menu_estudiante():
    limpiar_pantalla()
    print("¡Bienvenido, estudiante!")
    print("\nMenú de Opciones:")
    print("1. Reservar-Alquilar Equipo")
    print("2. Realizar Pago")
    print("3. Verificar Disponibilidad")
    print("0. Cerrar Sesión")

# Función para mostrar el menú de opciones de administrador
def mostrar_menu_administrador():
    limpiar_pantalla()
    print("¡Bienvenido, administrador!")
    print("\nMenú de Opciones:")
    print("1. Gestionar Equipos")
    print("2. Gestionar Usuarios")
    print("3. Ver Estadísticas")
    print("0. Cerrar Sesión")

# Función para manejar la opción "Reservar Equipo" del menú de estudiante
bicicletas = {
    "865": {"Marca": "Marca1", "Modelo": "Modelo1", "Color": "Azul", "Tipo": "Montaña", "Precio": 20.00},
    "324": {"Marca": "Marca2", "Modelo": "Modelo2", "Color": "Rojo", "Tipo": "Urbana", "Precio": 25.00},
    "892": {"Marca": "Marca3", "Modelo": "Modelo3", "Color": "Verde", "Tipo": "Carrera", "Precio": 30.00},
    "738": {"Marca": "Marca4", "Modelo": "Modelo4", "Color": "Negro", "Tipo": "Híbrida", "Precio": 35.00},
    # Añadir más bicicletas si es necesario
}

computadoras = {
    "291": {"Marca": "Marca1", "Modelo": "Modelo1", "Procesador": "Intel i5", "RAM": "8GB", "Precio": 50.00},
    "132": {"Marca": "Marca2", "Modelo": "Modelo2", "Procesador": "AMD Ryzen 7", "RAM": "16GB", "Precio": 70.00},
    "412": {"Marca": "Marca3", "Modelo": "Modelo3", "Procesador": "Intel i7", "RAM": "32GB", "Precio": 90.00},
    "142": {"Marca": "Marca4", "Modelo": "Modelo4", "Procesador": "AMD Ryzen 5", "RAM": "16GB", "Precio": 60.00},
    # Añadir más computadoras si es necesario
}

def buscar_equipo(tipo_equipo, id_equipo):
    if tipo_equipo == 'bicicleta':
        equipo = bicicletas.get(id_equipo)
    elif tipo_equipo == 'computadora':
        equipo = computadoras.get(id_equipo)
    else:
        return None

    # Simulación de búsqueda
    print("Buscando...")
    time.sleep(2)  # Simular búsqueda
    
    return equipo

def reservar_equipo(usuario):
    print("Reservar Equipo\n")
    print("Seleccione el tipo de equipo:")
    print("1. Bicicleta")
    print("2. Computadora")
    tipo_equipo = input("Ingrese el número del tipo de equipo deseado: ")

    if tipo_equipo == '1':
        tipo_equipo = 'bicicleta'
        equipos_disponibles = bicicletas
    elif tipo_equipo == '2':
        tipo_equipo = 'computadora'
        equipos_disponibles = computadoras
    else:
        input("\nOpción no válida. Presione Enter para continuar...")
        return

    id_equipo = input("Ingrese el ID del equipo deseado: ")

    equipo_encontrado = buscar_equipo(tipo_equipo, id_equipo)

    if equipo_encontrado:
        print("\nEspecificaciones del equipo:")
        print("=" * 40)
        for especificacion, valor in equipo_encontrado.items():
            print("| {:<15} | {:<15} |".format(especificacion, valor))
        print("=" * 40)
        print("\nOpciones:")
        print("1. Alquilar")
        print("2. Reservar")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == '1':
            print("Alquilando equipo...")
            # Aquí iría la lógica para alquilar el equipo
        elif opcion == '2':
            print("Reservando equipo...")
            # Aquí iría la lógica para reservar el equipo
        else:
            input("\nOpción no válida. Presione Enter para continuar...")
    else:
        print("\nEquipo no encontrado. Intente nuevamente.")
        # Aquí se podría ofrecer al usuario la opción de volver a intentar o regresar al menú principal



# Función para manejar la opción "Realizar Pago" del menú de estudiante
def realizar_pago(usuario):
    limpiar_pantalla()
    print("Realizando Pago\n")
    print("Escaneando código QR...")

    # Simulación de escaneo de código QR
    time.sleep(2)

    # Simulación de barra de carga
    for i in range(1, 6):
        time.sleep(0.5)
        porcentaje = i * 20
        print("Procesando pago: [{}{}] {}%".format("#" * i, " " * (5 - i), porcentaje), end='\r')

    print("\n\nPago procesado con éxito.\n")

    # Simulación de tabla de factura
    # Definición de conceptos y montos
    conceptos = {
        "Lápices": 10.00,
        "Cuadernos": 5.00,
        "Plumas": 7.50,
        "Gomas": 3.00
    }

    # Cálculo del total
    total = sum(conceptos.values())

    # Aplicación de descuento (supongamos un descuento del 10%)
    descuento = total * 0.10
    total_con_descuento = total - descuento

    # Imprimir factura
    print("Factura:")
    print("=" * 40)
    print("|    Concepto       |   Monto   |")
    print("-" * 40)
    for concepto, monto in conceptos.items():
        print(f"|  {concepto:<15} |  ${monto:>6.2f}  |")
    print("-" * 40)
    print("|    Total sin descuento:   |  ${:>6.2f}  |".format(total))
    print("|    Descuento (10%):       |  ${:>6.2f}  |".format(descuento))
    print("|    Total con descuento:   |  ${:>6.2f}  |".format(total_con_descuento))
    print("=" * 40)
    a = input("presione una tecla para continuar...")
    

# Función para manejar la opción "Verificar Disponibilidad" del menú de estudiante
def verificar_disponibilidad(usuario):
    print("Verificar Disponibilidad\n")

    # Mostrar bicicletas disponibles
    print("Bicicletas Disponibles:")
    print("=" * 40)
    print("|    ID   |   Color   |   Tipo   |")
    print("-" * 40)
    for id_bicicleta, bicicleta in bicicletas.items():
        print("| {:>8} | {:>8} | {:>8} |".format(id_bicicleta, bicicleta["Color"], bicicleta["Tipo"]))
    print("=" * 40)

    # Mostrar computadoras disponibles
    print("\nComputadoras Disponibles:")
    print("=" * 40)
    print("|    ID   |  Procesador  |   RAM   |")
    print("-" * 40)
    for id_computadora, computadora in computadoras.items():
        print("| {:>8} | {:>11} | {:>7} |".format(id_computadora, computadora["Procesador"], computadora["RAM"]))
    print("=" * 40)
    a = input("presione una tecla para continuar...")

# Definición de estudiantes (Ejemplo)
estudiantes = {
    "1001": {"Nombre": "Juan", "Apellido": "Perez", "Edad": 20, "Carrera": "Ingeniería"},
    "1002": {"Nombre": "María", "Apellido": "Gómez", "Edad": 22, "Carrera": "Medicina"},
    "1003": {"Nombre": "Pedro", "Apellido": "Martínez", "Edad": 21, "Carrera": "Derecho"},
    # Puedes añadir más estudiantes según sea necesario
}

def mostrar_estudiantes():
    print("\nEstudiantes Registrados:")
    print("=" * 50)
    print("|  ID  |   Nombre   |   Apellido   |  Edad  |  Carrera  |")
    print("-" * 50)
    for id_estudiante, estudiante in estudiantes.items():
        print("| {:<5} | {:<10} | {:<12} | {:<6} | {:<10} |".format(id_estudiante, estudiante["Nombre"], estudiante["Apellido"], estudiante["Edad"], estudiante["Carrera"]))
    print("=" * 50)

def gestionar_usuarios():
    while True:
        # Mostrar estudiantes
        mostrar_estudiantes()

        # Opciones de gestión de usuarios
        print("\nOpciones:")
        print("1. Ver detalles de un estudiante")
        print("2. Modificar un estudiante")
        print("3. Eliminar un estudiante")
        print("0. Volver al menú principal")

        opcion_usuario = input("\nIngrese el número de la opción deseada: ")

        if opcion_usuario == '0':
            print("\nVolviendo al menú principal...")
            break
        elif opcion_usuario == '1':
            # Ver detalles de un estudiante
            id_estudiante = input("\nIngrese el ID del estudiante que desea ver: ")
            if id_estudiante in estudiantes:
                print("\nDetalles del estudiante:")
                print("=" * 50)
                for campo, valor in estudiantes[id_estudiante].items():
                    print("{:<10}: {}".format(campo, valor))
                print("=" * 50)
            else:
                print("\nNo se encontró ningún estudiante con ese ID.")
        elif opcion_usuario == '2':
            # Modificar un estudiante
            id_estudiante = input("\nIngrese el ID del estudiante que desea modificar: ")
            if id_estudiante in estudiantes:
                print("\nModificar estudiante:")
                # Aquí iría la lógica para modificar los detalles del estudiante
            else:
                print("\nNo se encontró ningún estudiante con ese ID.")
        elif opcion_usuario == '3':
            # Eliminar un estudiante
            id_estudiante = input("\nIngrese el ID del estudiante que desea eliminar: ")
            if id_estudiante in estudiantes:
                confirmacion = input("\n¿Está seguro que desea eliminar al estudiante {}? (s/n): ".format(estudiantes[id_estudiante]["Nombre"]))
                if confirmacion.lower() == 's':
                    del estudiantes[id_estudiante]
                    print("\nEstudiante eliminado exitosamente.")
            else:
                print("\nNo se encontró ningún estudiante con ese ID.")
        else:
            input("\nOpción no válida. Presione Enter para continuar...")

def gestionar_equipos():
    print("\nGestión de Equipos\n")
    lista_equipos = [
    {"ID": "1", "Nombre": "Laptop Dell", "Disponibilidad": "Disponible"},
    {"ID": "2", "Nombre": "Impresora HP", "Disponibilidad": "No disponible"},
    {"ID": "3", "Nombre": "Proyector Epson", "Disponibilidad": "Disponible"},
    # Agrega más equipos según sea necesario
    ]
    # Mostrar tabla con todos los equipos
    print("Lista de Equipos:")
    print("=" * 40)
    print("|   ID   |   Nombre   |   Disponibilidad   |")
    print("-" * 40)
    for equipo in lista_equipos:  # Suponiendo que lista_equipos es una lista de diccionarios con los datos de los equipos
        print("| {:>6} | {:>10} | {:>17} |".format(equipo["ID"], equipo["Nombre"], equipo["Disponibilidad"]))
    print("=" * 40)

    # Ingresar el ID del equipo a gestionar
    id_equipo = input("\nIngrese el ID del equipo que desea gestionar: ")

    # Buscar el equipo por su ID
    equipo = None
    for e in lista_equipos:
        if e["ID"] == id_equipo:
            equipo = e
            break

    if equipo:
        # Mostrar opciones para el equipo encontrado
        print("\nOpciones para el equipo {}:".format(equipo["Nombre"]))
        print("1. Eliminar equipo")
        print("2. Modificar disponibilidad")
        print("3. Ver detalles de equipo")
        opcion_equipo = input("Ingrese el número de la opción deseada: ")

        if opcion_equipo == '1':
            # Lógica para eliminar equipo
            lista_equipos.remove(equipo)
            print("El equipo {} ha sido eliminado correctamente.".format(equipo["Nombre"]))
        elif opcion_equipo == '2':
            # Lógica para modificar disponibilidad
            # Supongamos que aquí permites modificar la disponibilidad del equipo
            pass
        elif opcion_equipo == '3':
            # Mostrar detalles del equipo
            print("Detalles del equipo:")
            print(equipo)
        else:
            input("\nOpción no válida. Presione Enter para continuar...")
    else:
        print("Equipo no encontrado.")

def ver_estadisticas():
    equipos = {
    "291": {"Tipo": "Computadora", "Marca": "Marca1", "Modelo": "Modelo1", "Procesador": "Intel i5", "RAM": "8GB", "Precio": 50.00, "Disponibilidad": "Disponible"},
    "132": {"Tipo": "Computadora", "Marca": "Marca2", "Modelo": "Modelo2", "Procesador": "AMD Ryzen 7", "RAM": "16GB", "Precio": 70.00, "Disponibilidad": "No disponible"},
    "412": {"Tipo": "Computadora", "Marca": "Marca3", "Modelo": "Modelo3", "Procesador": "Intel i7", "RAM": "32GB", "Precio": 90.00, "Disponibilidad": "Disponible"},
    "142": {"Tipo": "Computadora", "Marca": "Marca4", "Modelo": "Modelo4", "Procesador": "AMD Ryzen 5", "RAM": "16GB", "Precio": 60.00, "Disponibilidad": "Disponible"},
    "865": {"Tipo": "Bicicleta", "Marca": "Marca1", "Modelo": "Modelo1", "Color": "Azul", "Tipo_Bicicleta": "Montaña", "Precio": 20.00, "Disponibilidad": "No disponible"},
    "324": {"Tipo": "Bicicleta", "Marca": "Marca2", "Modelo": "Modelo2", "Color": "Rojo", "Tipo_Bicicleta": "Urbana", "Precio": 25.00, "Disponibilidad": "Disponible"},
    "111": {"Tipo": "Bicicleta", "Marca": "Marca3", "Modelo": "Modelo3", "Color": "Verde", "Tipo_Bicicleta": "Carrera", "Precio": 30.00, "Disponibilidad": "No Disponible"},
    "222": {"Tipo": "Bicicleta", "Marca": "Marca4", "Modelo": "Modelo4", "Color": "Negro", "Tipo_Bicicleta": "Híbrida", "Precio": 35.00, "Disponibilidad": "Disponible"},
}
    # Contar el número total de equipos
    total_equipos = len(equipos)

    # Contar el número total de computadoras y bicicletas
    total_computadoras = sum(1 for equipo in equipos.values() if equipo["Tipo"] == "Computadora")
    total_bicicletas = sum(1 for equipo in equipos.values() if equipo["Tipo"] == "Bicicleta")

    # Contar la cantidad de equipos disponibles y no disponibles
    equipos_disponibles = sum(1 for equipo in equipos.values() if equipo["Disponibilidad"] == "Disponible")
    equipos_no_disponibles = sum(1 for equipo in equipos.values() if equipo["Disponibilidad"] == "No disponible")

    # Imprimir las estadísticas
    print("\nEstadísticas de Equipos:")
    print("-" * 50)
    print("Total de Equipos: {}".format(total_equipos))
    print("Total de Computadoras: {}".format(total_computadoras))
    print("Total de Bicicletas: {}".format(total_bicicletas))
    print("Equipos Disponibles: {}".format(equipos_disponibles))
    print("Equipos No Disponibles: {}".format(equipos_no_disponibles))

    # Crear un gráfico de barras para la distribución de disponibilidad por tipo de equipo
    import matplotlib.pyplot as plt

    tipos = ['Computadoras', 'Bicicletas']
    disponibles = [total_computadoras - equipos_no_disponibles, total_bicicletas - equipos_no_disponibles]
    no_disponibles = [equipos_no_disponibles, equipos_no_disponibles]

    plt.bar(tipos, disponibles, color='green', label='Disponibles')
    plt.bar(tipos, no_disponibles, bottom=disponibles, color='red', label='No Disponibles')

    plt.xlabel('Tipo de Equipo')
    plt.ylabel('Cantidad')
    plt.title('Distribución de Disponibilidad de Equipos por Tipo')
    plt.legend()
    plt.show()


# Función principal
def main():
    usuario_actual = None

    while True:
        if usuario_actual is None:
            usuario_actual = iniciar_sesion()
            if usuario_actual is None:
                continue
            else:
                tipo_usuario, usuario = usuario_actual

        if tipo_usuario == 'estudiante':
            mostrar_menu_estudiante()
        elif tipo_usuario == 'administrador':
            mostrar_menu_administrador()

        opcion = input("\nIngrese el número de la opción deseada: ")

        if opcion == '0':
            limpiar_pantalla()
            print("Cerrando sesión. ¡Hasta luego, {}!".format(usuario))
            usuario_actual = None
        elif tipo_usuario == 'estudiante':
            if opcion == '1':
                reservar_equipo(usuario)
            elif opcion == '2':
                realizar_pago(usuario)
            elif opcion == '3':
                verificar_disponibilidad(usuario)
            else:
                input("\nOpción no válida. Presione Enter para continuar...")
        elif tipo_usuario == 'administrador':
            if opcion == '1':
                gestionar_equipos()
            elif opcion == '2':
                gestionar_usuarios()
            elif opcion == '3':
                ver_estadisticas()
            else:
                input("\nOpción no válida. Presione Enter para continuar...")

if __name__ == "__main__":
    main()
