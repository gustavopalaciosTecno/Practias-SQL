# Practicas-SQL  <@|@>

# Sistema de Gestión de Ventas
# Este proyecto es un sistema de gestión de ventas en Python que utiliza una base de datos MySQL para almacenar y organizar registros de ventas, clasificándolos como ventas en línea y ventas locales. Incluye funcionalidades para agregar, listar, modificar y eliminar ventas.

# Características
# Gestión de ventas: permite registrar ventas online y locales.
# Persistencia de datos: utiliza MySQL para almacenar registros de ventas.
# Clases de ventas: soporte para diferentes tipos de ventas mediante las clases 
# VentaOnline y VentaLocal.
# Operaciones CRUD: creación, lectura, actualización y eliminación de registros de ventas.
# Requisitos
# Python 3.x
# MySQL Connector para Python
# Servidor MySQL configurado y una base de datos llamada ventassql
# Estructura de la Base de Datos
# El sistema requiere dos tablas en la base de datos ventassql:

# sql
# Copiar código
# CREATE TABLE ventas_online (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    fecha DATETIME,
#    cliente VARCHAR(255),
#    productos TEXT,
#    plataforma VARCHAR(255)
# );

# CREATE TABLE ventas_local (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    fecha DATETIME,
#    cliente VARCHAR(255),
#    productos TEXT,
#    sucursal VARCHAR(255)
# );

# Uso
# Configura la conexión a la base de datos en la clase GestorVentas, especificando tus credenciales de MySQL (host, user, password, y database).
# Ejecuta el programa principal con el siguiente comando:
# bash
# Copiar código
# python SistemaVentasSQL.py
# Ejemplo de Código

# Clases
# Venta: Clase base que almacena la fecha, el cliente y los productos.
# VentaOnline: Subclase que incluye la plataforma de venta online.
# VentaLocal: Subclase que incluye la sucursal donde se realiza la venta.
# GestorVentas: Clase para gestionar las operaciones con la base de datos (agregar, listar, modificar y eliminar ventas).
# Contribuciones
# Las contribuciones son bienvenidas. Puedes realizar un fork del repositorio y enviar un pull request.

# Licencia
# Este proyecto se encuentra bajo la Licencia Pajarrito Online.