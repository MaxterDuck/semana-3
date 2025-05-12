# Simulacro de Examen: Gestión de Inventario de una Librería en Python

inventory = [
    {"name": "El principito", "price": 20, "quantity": 100},
    {"name": "La vida es bella", "price": 15, "quantity": 50},
    {"name": "100 años de soledad", "price": 20, "quantity": 30},
    {"name": "Leopardos al sol", "price": 25, "quantity": 10},
    {"name": "La laguna azul", "price": 10, "quantity": 5}
]

# Input seguro
def input_num(prompt, tipo=float):
    while True:
        entrada = input(prompt)
        try:
            valor = tipo(entrada)
            if valor <= 0:
                print("Must be a positive number.")
                continue
            return valor
        except ValueError:
            print("Invalid entry. Please enter a valid number.")

# 1. Añadir libros
def add_books(name, price, quantity):
    for book in inventory:
        if book["name"].lower() == name.lower():  
            print("The book already exists in the inventory.")
            return
    inventory.append({"name": name, "price": round(price, 2), "quantity": int(quantity)})
    print(f"Book '{name}' successfully added with price ${price:.2f} and quantity {quantity}.")

# 2. Consultar libro
def search_books(name):
    for book in inventory:
        if book["name"].lower() == name.lower():  
            print(f"{book['name']} | Price: ${book['price']:.2f} | Quantity: {book['quantity']}")
            return
    print("Book not found.")

# 3. Actualizar precio
def update_price_books(name, new_price):
    for book in inventory:
        if book["name"].lower() == name.lower():
            book["price"] = round(new_price, 2)
            print(f"Price of '{name}' updated to ${new_price:.2f}.")
            return
    print("Book not found.")

# 4. Eliminar libro
def del_books(name):
    for book in inventory:
        if book["name"].lower() == name.lower():
            inventory.remove(book)
            print(f"The book '{name}' was removed from inventory.")
            return
    print("Book not found.")

# 5. Calcular total inventario
def total_inventory_value():
    total = sum(book["price"] * book["quantity"] for book in inventory)
    print(f"Total inventory value: ${total:.2f}")

# Menú de opciones
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Update Book Price")
        print("4. Delete a Book")
        print("5. Calculate Inventory Value")
        print("6. Leave")

        option = input("Choose an option (1-6): ")

        if option == "1":
            name = input("Book title: ").strip()
            price = input_num("Book price: ")
            quantity = input_num("Quantity: ", int)
            add_books(name, price, quantity)

        elif option == "2":
            name = input("Book title to search: ").strip()
            search_books(name)

        elif option == "3":
            name = input("Book title to update: ").strip()
            new_price = input_num("New price: ")
            update_price_books(name, new_price)

        elif option == "4":
            name = input("Book title to delete: ").strip()
            del_books(name)

        elif option == "5":
            total_inventory_value()

        elif option == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please choose between 1 and 6.")

# Iniciar el programa
if __name__ == "__main__":
    menu()



