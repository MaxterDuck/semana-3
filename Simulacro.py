#Simulacro de Examen: Gestión de Inventario de una Librería en Python
inventory = [
    {"El principito ": "Book 1", "price": 20, "quantity": 100},
    {"La vida es bella": "Book 2", "price": 15, "quantity": 50},
    {"100 años de soledad": "Book 3", "price": 20, "quantity": 30},
    {"Leopardos al sol": "Book 4", "price": 25, "quantity": 10},
    {"La laguna azul": "Book 5", "price": 10, "quantity": 5}
]
def input_num(prompt, tipo=int):
    while True:
        entrada = input(prompt)
        try:
            return tipo(entrada)
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número valido.")
#This function does register a new book 
def add_books():
    for book in inventory:
        price = 0 
        quantity = 0
        name = input("Dame el nombre del libro: ")
        price = input_num("Dame el precio del libro: ", int)
        quantity = input_num("Dame la cantidad de libros: ", int)
        if name in inventory:
            print ("El libro ya existe en el inventario")
        if price <= 0:                      
            print ("Precio no valido. Ingresa un precio en numeros positivos")                                                                                                                                                                                                                          
        if quantity<0:
                print ("Precio no valido. Ingresa un precio en numeros positivos")
        else:
            print ("Precio registrado correctamente")
            
        print (f"Libro añadido correctamente| Con el precio de:{price}| Con Cantidad de: {quantity} Libros")

#This function does search a book
def search_books(name,price,quantity):
    book = inventory.__add__(name,price,quantity)
    if book:
        print(f"El libro es : {name} | El precio es de : ${price} | Cantidad: {quantity[1]}") 
    else:
        print("Libro  no encontrado.")

#This function does update the pruce
def update_price_books(name,new_price):
    if name in inventory:
        quantity = inventory[name]
        inventory[name] = (new_price, quantity)
        print(f" Precio del Libro'{name}' actualizado a ${new_price}.")
    else:
        print(" Producto no encontrado para actualizar.")
        


#Menu 
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. ADD Book")
        print ("2. Search Books") 
        print ("3.Update price Books")
        option = input("Choose any option (1-3): ")

        if option == "1":
            name = input(str("Darme el titulo de el libro: "))
            price = input (int("Dame el precio de el libro: "))
            quantity = input (int("Dame la cantidad que deseas registrar: "))

            add_books()
        elif option == "2":
            name = input("Libro a buscar: ")
            search_books(name)
        elif option == "3":
            name = input("Nombre del libro a actualizar: ").strip()
            new_price = input_num("Nuevo precio: ", int)
            update_price_books(name, new_price)
        

if __name__ == "__main__":
        menu()
