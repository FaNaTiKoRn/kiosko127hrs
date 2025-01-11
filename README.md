# Kiosco127Hrs

## Descripción
Kiosco127Hrs es un sistema de gestión de inventario diseñado para pequeñas tiendas. Permite agregar, modificar, eliminar y consultar productos, además de generar informes de stock bajo.

---

## Autor
- **José Torres Tortorella**
- **DNI:** 95.704.279

---

## Instrucciones de Uso

### 1. Requisitos
- Python 3.x
- Biblioteca `colorama` (instalable con `pip install colorama`)

### 2. Instalación
1. Clona o descarga el repositorio.
2. Asegúrate de tener instalado Python y las dependencias necesarias.

### 3. Configuración Inicial
1. Ejecuta el archivo `makedb.py` para crear la base de datos inicial.
```bash
python makedb.py
```
2. Ejecuta el archivo principal para iniciar el programa:
```bash
python kiosco127hrs.py
```

---

## Funcionalidades

1. **Agregar Producto**
   - Permite añadir nuevos productos al inventario especificando nombre, categoría, precio y cantidad.

2. **Mostrar Productos**
   - Lista todos los productos actualmente almacenados en el inventario.

3. **Modificar Producto**
   - Modifica los detalles de un producto existente.

4. **Eliminar Producto**
   - Elimina un producto del inventario.

5. **Informe de Bajo Stock**
   - Genera un informe de productos con stock inferior o igual a un límite especificado.

6. **Salir**
   - Finaliza el programa.

---

## Detalles Técnicos

### Base de Datos
- **Nombre:** `kiosco127hrs.db`
- **Tabla:** `productos`

| Campo         | Tipo     | Restricciones                |
|---------------|----------|-----------------------------|
| `id_producto` | INTEGER  | PRIMARY KEY, AUTOINCREMENT  |
| `nombre`      | TEXT     | NOT NULL                    |
| `categoria`   | TEXT     | NOT NULL                    |
| `precio`      | REAL     | NOT NULL                    |
| `stock`       | INTEGER  | NOT NULL, CHECK(stock >= 0) |

### Librerías Utilizadas
- `sqlite3` para la gestión de la base de datos.
- `colorama` para estilizar la salida en consola.

---

## Créditos del Curso
- **Instructor:** Fede Liquin
- **Tutora:** Natalia ThemTham

---

## Notas para el Usuario
- El sistema está diseñado para ser ejecutado en terminal.
- Asegúrate de mantener actualizada la base de datos según las necesidades de la tienda.
