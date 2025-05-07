# Diccionario: clave = nombre, valor = (teléfono, correo)
agenda = {}

def añadir_contacto():
    nombre = input("Dame tu nombre: ")
    telefono = input("Dame tu teléfono: ")
    correo = input("Dame tu correo: ")
    agenda[nombre] = (telefono, correo)
    print(f"Contacto de {nombre} añadido correctamente :)")

def buscar_contacto(nombre):
    if nombre in agenda:
        telefono, correo = agenda[nombre]
        print(f"Nombre: {nombre} | Teléfono: {telefono} | Correo: {correo}")
    else: 
        print("❌ Contacto no encontrado.")

def actualizar_telefono(nombre, nuevo_telefono):
    if nombre in agenda:
        _, correo = agenda[nombre]  # Desempaquetamos y descartamos el teléfono anterior
        agenda[nombre] = (nuevo_telefono, correo)
        print(f"📞 Teléfono de '{nombre}' actualizado a {nuevo_telefono}.")
    else:
        print(f"❌ El contacto '{nombre}' no existe.")

def eliminar_contacto(nombre):
    if nombre in agenda: 
        del agenda[nombre]
        print(f"🗑️ El contacto de '{nombre}' fue eliminado de la agenda.")
    else:
        print("❌ Contacto no encontrado.")

def mostrar_todos():
    if agenda:
        print("📋 Contactos en la agenda:")
        for nombre, (telefono, correo) in agenda.items():
            print(f"-> {nombre}: Teléfono: {telefono}, Correo: {correo}")
    else:
        print("📭 Agenda vacía.")

# Menú interactivo
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Actualizar teléfono")
        print("4. Eliminar contacto")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            añadir_contacto()

        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            buscar_contacto(nombre)

        elif opcion == "3":
            nombre = input("Nombre a actualizar: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            actualizar_telefono(nombre, nuevo_telefono)

        elif opcion == "4":
            nombre = input("Nombre a eliminar: ")
            eliminar_contacto(nombre)

        elif opcion == "5":
            mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo del programa...")
            break

        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    menu()