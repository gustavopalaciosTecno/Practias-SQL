import mysql.connector
from datetime import datetime

class Venta:
    def __init__(self, fecha, cliente, productos):
        self.fecha = fecha
        self.cliente = cliente
        self.productos = productos

    def to_dict(self):
        return {
            "fecha": self.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "cliente": self.cliente,
            "productos": self.productos
        }
#fgdsfdsfdsfds
class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos, plataforma):
        super().__init__(fecha, cliente, productos)
        self.plataforma = plataforma

    def to_dict(self):
        data = super().to_dict()
        data["plataforma"] = self.plataforma
        return data

class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos, sucursal):
        super().__init__(fecha, cliente, productos)
        self.sucursal = sucursal

    def to_dict(self):
        data = super().to_dict()
        data["sucursal"] = self.sucursal
        return data

class GestorVentas:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="titanoboa2023",
            database="ventassql"
        )
        self.cursor = self.conexion.cursor()

    def agregar_venta(self, venta):
        try:
            if isinstance(venta, VentaOnline):
                query = """
                    INSERT INTO ventas_online (fecha, cliente, productos, plataforma) 
                    VALUES (%s, %s, %s, %s)
                """
                values = (
                    venta.fecha.strftime("%Y-%m-%d %H:%M:%S"), 
                    venta.cliente, 
                    ','.join(venta.productos), 
                    venta.plataforma
                )
            elif isinstance(venta, VentaLocal):
                query = """
                    INSERT INTO ventas_local (fecha, cliente, productos, sucursal) 
                    VALUES (%s, %s, %s, %s)
                """
                values = (
                    venta.fecha.strftime("%Y-%m-%d %H:%M:%S"), 
                    venta.cliente, 
                    ','.join(venta.productos), 
                    venta.sucursal
                )
            self.cursor.execute(query, values)
            self.conexion.commit()
            print("Venta agregada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar venta: {err}")

    def listar_ventas(self):
        ventas = []
        try:
            
            self.cursor.execute("SELECT * FROM ventas_online")
            ventas_online = self.cursor.fetchall()
            for venta in ventas_online:
                id_venta, fecha, cliente, productos, plataforma = venta
                ventas.append({
                    "id": id_venta,
                    "fecha": fecha,
                    "cliente": cliente,
                    "productos": productos.split(','),
                    "plataforma": plataforma
                })

            
            self.cursor.execute("SELECT * FROM ventas_local")
            ventas_local = self.cursor.fetchall()
            for venta in ventas_local:
                id_venta, fecha, cliente, productos, sucursal = venta
                ventas.append({
                    "id": id_venta,
                    "fecha": fecha,
                    "cliente": cliente,
                    "productos": productos.split(','),
                    "sucursal": sucursal
                })
        except mysql.connector.Error as err:
            print(f"Error al listar ventas: {err}")
        return ventas

    def modificar_venta(self, index, nueva_venta):
        try:
            if isinstance(nueva_venta, VentaOnline):
                query = """
                    UPDATE ventas_online 
                    SET fecha = %s, cliente = %s, productos = %s, plataforma = %s 
                    WHERE id = %s
                """
                values = (
                    nueva_venta.fecha.strftime("%Y-%m-%d %H:%M:%S"), 
                    nueva_venta.cliente, 
                    ','.join(nueva_venta.productos), 
                    nueva_venta.plataforma, 
                    index
                )
            elif isinstance(nueva_venta, VentaLocal):
                query = """
                    UPDATE ventas_local 
                    SET fecha = %s, cliente = %s, productos = %s, sucursal = %s 
                    WHERE id = %s
                """
                values = (
                    nueva_venta.fecha.strftime("%Y-%m-%d %H:%M:%S"), 
                    nueva_venta.cliente, 
                    ','.join(nueva_venta.productos), 
                    nueva_venta.sucursal, 
                    index
                )
            self.cursor.execute(query, values)
            self.conexion.commit()
            print("Venta modificada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al modificar venta: {err}")

    def eliminar_venta(self, index):
        try:
            self.cursor.execute("DELETE FROM ventas_online WHERE id = %s", (index,))
            if self.cursor.rowcount == 0:
                self.cursor.execute("DELETE FROM ventas_local WHERE id = %s", (index,))
                if self.cursor.rowcount == 0:
                    print(f"No se encontró ninguna venta con ID {index}.")
                else:
                    print(f"Venta local con ID {index} eliminada exitosamente.")
            else:
                print(f"Venta online con ID {index} eliminada exitosamente.")
            self.conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error al eliminar venta: {err}")

def main():
    gestor = GestorVentas()

    
    venta1 = VentaOnline(datetime.now(), "Cliente 1", ["Producto A", "Producto B"], "Amazon")
    venta2 = VentaLocal(datetime.now(), "Cliente 2", ["Producto C", "Producto D"], "Sucursal 1")

   
    gestor.agregar_venta(venta1)
    gestor.agregar_venta(venta2)

    
    ventas = gestor.listar_ventas()
    for venta in ventas:
        print(venta)

if __name__ == "__main__":
    main()
