# Proyecto: Kiosco127Hrs
# Autor: José Torres Tortorella (95.704.279)
# Descripción: Sistema de gestión de inventario para una pequeña tienda, desarrollado en Python para el Curso Iniciación a la Programación con Pyhton.
# Instructor: Fede Liquin.
# Tutora: Natalia ThemTham.

import sqlite3
from colorama import init, Fore, Style, Back

# Inicialización del colorama la consola
init(autoreset=True)

# === Funciones de utilidad ===

def ejecutar_query(query, params=(), fetch_mode=None):
    """
    Ejecuta una consulta SQL en la base de datos.
    Args:
        query (str): Instrucción SQL.
        params (tuple): Parámetros para la consulta.
        fetch_mode (str): Modo de recuperación ('all', 'one' o None).
    Returns:
        list or bool: Resultado de la consulta o True si fue exitosa.
    """
    try:
        with sqlite3.connect("kiosco127hrs.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute(query, params)
            if fetch_mode == 'all':
                return cursor.fetchall()
            elif fetch_mode == 'one':
                return cursor.fetchone()
            conexion.commit()
            return True
    except sqlite3.Error as e:
        print(f"{Fore.RED}[Error SQL]: {e}")
        return False

def mensaje_exito(mensaje):
    print(f"{Fore.GREEN}{Style.BRIGHT}{mensaje}")

def mensaje_error(mensaje):
    print(f"{Fore.RED}{Style.BRIGHT}{mensaje}")

def mensaje_advertencia(mensaje):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{mensaje}")

# === Funciones principales ===

def inicializar_base_datos():
    """
    Crea la tabla de productos si no existe.
    """
    query = '''
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            cantidad INTEGER NOT NULL DEFAULT 0,
            precio REAL NOT NULL
        )
    '''
    if ejecutar_query(query):
        mensaje_exito("Base de datos inicializada correctamente.")

def mostrar_menu():
    """
    Muestra el menú principal de opciones y retorna la elección del usuario.
    Returns:
        int: Opcion seleccionada.
    """
    print(Fore.CYAN + Style.BRIGHT + "\n=== Menú de Inventario ===")
    print("1. Agregar un producto")
    print("2. Mostrar listado de productos")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Informe de bajo stock")
    print("6. Salir")
    return int(input("Seleccione una opción: "))

def validar_cantidad():
    """
    Valida que la cantidad ingresada sea un número entero positivo.
    Returns:
        int: Cantidad validada.
    """
    while True:
        try:
            cantidad = int(input('Ingrese la cantidad: '))
            if cantidad >= 0:
                return cantidad
            else:
                mensaje_error("La cantidad debe ser 0 o mayor. Intente nuevamente.")
        except ValueError:
            mensaje_error("Valor inválido. Ingrese un número entero.")

def agregar_producto():
    """
    Agrega un producto al inventario.
    """
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    cantidad = validar_cantidad()
    precio = float(input("Ingrese el precio del producto: "))
    query = '''
        INSERT INTO productos (nombre, categoria, cantidad, precio)
        VALUES (?, ?, ?, ?)
    '''
    params = (nombre, categoria, cantidad, precio)
    if ejecutar_query(query, params):
        mensaje_exito(f"Producto '{nombre}' agregado correctamente.")

def mostrar_productos():
    """
    Muestra el listado completo de productos.
    """
    query = "SELECT * FROM productos"
    productos = ejecutar_query(query, fetch_mode="all")
    if productos:
        encabezado = f"{'ID':<5} {'Nombre':<20} {'Categoría':<15} {'Cantidad':<10} {'Precio':<10}"
        print(Fore.GREEN + Style.BRIGHT + "\n=== Inventario ===")
        print(encabezado)
        print("-" * len(encabezado))
        for prod in productos:
            print(f"{prod[0]:<5} {prod[1]:<20} {prod[2]:<15} {prod[3]:<10} {prod[4]:<10.2f}")
    else:
        mensaje_advertencia("No hay productos registrados en el inventario.")

def modificar_producto():
    """
    Modifica los datos de un producto existente.
    """
    id_producto = int(input("Ingrese el ID del producto a modificar: "))
    producto = ejecutar_query("SELECT * FROM productos WHERE id_producto = ?", (id_producto,), "one")
    if producto:
        nuevo_nombre = input("Nuevo nombre (deje en blanco para mantener): ") or producto[1]
        nueva_categoria = input("Nueva categoría (deje en blanco para mantener): ") or producto[2]
        nueva_cantidad = validar_cantidad()
        nuevo_precio = float(input("Nuevo precio: "))
        query = '''
            UPDATE productos
            SET nombre = ?, categoria = ?, cantidad = ?, precio = ?
            WHERE id_producto = ?
        '''
        params = (nuevo_nombre, nueva_categoria, nueva_cantidad, nuevo_precio, id_producto)
        if ejecutar_query(query, params):
            mensaje_exito("Producto actualizado correctamente.")
    else:
        mensaje_error("Producto no encontrado.")

def eliminar_producto():
    """
    Elimina un producto del inventario.
    """
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    query = "DELETE FROM productos WHERE id_producto = ?"
    if ejecutar_query(query, (id_producto,)):
        mensaje_exito("Producto eliminado correctamente.")
    else:
        mensaje_error("No se pudo eliminar el producto. Verifique el ID.")

def informe_bajo_stock():
    """
    Genera un informe de productos con bajo stock.
    """
    limite = int(input("Ingrese el límite de stock: "))
    query = "SELECT nombre, cantidad FROM productos WHERE cantidad <= ?"
    productos = ejecutar_query(query, (limite,), "all")
    if productos:
        print(Fore.YELLOW + Style.BRIGHT + "\n=== Productos con Bajo Stock ===")
        for prod in productos:
            print(f"Producto: {prod[0]}, Cantidad: {prod[1]}")
    else:
        mensaje_advertencia(f"No hay productos con stock inferior o igual a {limite}.")

def kiosco_virtual():
    """
    Función principal para gestionar el inventario.
    """
    inicializar_base_datos()
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_productos()
        elif opcion == 3:
            modificar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            informe_bajo_stock()
        elif opcion == 6:
            print(Fore.BLUE + Style.BRIGHT + "Gracias por usar Kiosco127Hrs. Adiós!")
            input("Presione Enter para salir...")
            break
        else:
            mensaje_error("Opción inválida. Intente nuevamente.")

# === Ejecución principal ===
kiosco_virtual()
