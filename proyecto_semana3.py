# inventario_tienda.py

# Diccionario para almacenar productos: clave = nombre, valor = (precio, cantidad)
inventario = {}

# Función para validar entrada numérica
def input_numerico(prompt, tipo=float):
    while True:
        entrada = input(prompt)
        try:
            return tipo(entrada)
        except ValueError:
            print("❌ Entrada no válida. Por favor ingresa un número.")

# Función para añadir productos
def añadir_producto(nombre, precio, cantidad):
    if nombre in inventario:
        print("⚠️ El producto ya existe. Usa actualizar si deseas cambiar el precio o cantidad.")
    else:
        inventario[nombre] = (precio, cantidad)
        print(f"✅ Producto '{nombre}' añadido correctamente.")

# Función para consultar producto
def consultar_producto(nombre):
    producto = inventario.get(nombre)
    if producto:
        print(f"Producto: {nombre} | Precio: ${producto[0]} | Cantidad: {producto[1]}")
    else:
        print("❌ Producto no encontrado.")

# Función para actualizar precio
def actualizar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        _, cantidad = inventario[nombre]
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f" Precio del producto '{nombre}' actualizado a ${nuevo_precio}.")
    else:
        print("❌ Producto no encontrado para actualizar.")

# Función para eliminar producto
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f" Producto '{nombre}' eliminado del inventario.")
    else:
        print("❌ Producto no encontrado para eliminar.")

# Función lambda para calcular el valor total del inventario
calcular_valor_total = lambda inv: sum(precio * cantidad for precio, cantidad in inv.values())

# Menú interactivo
def menu():
    while True:
        print("\n MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Mostrar todos los productos")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            precio = input_numerico("Precio del producto: ", float)
            cantidad = input_numerico("Cantidad disponible: ", int)
            añadir_producto(nombre, precio, cantidad)
        
        elif opcion == "2":
            nombre = input("Nombre del producto a consultar: ").strip()
            consultar_producto(nombre)
        
        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ").strip()
            nuevo_precio = input_numerico("Nuevo precio: ", float)
            actualizar_precio(nombre, nuevo_precio)
        
        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(nombre)
        
        elif opcion == "5":
            total = calcular_valor_total(inventario)
            print(f" Valor total del inventario: ${total:.2f}")
        
        elif opcion == "6":
            if inventario:
                print("\n Listado de productos:")
                for nombre, (precio, cantidad) in inventario.items():
                    print(f"- {nombre}: ${precio} x {cantidad}")
            else:
                print("⚠️ El inventario está vacío.")
        
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()
