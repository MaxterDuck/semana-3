# Simulacro de Examen: Gestión de Inventario de una Librería en Python
inventory = [
    {"name": "El principito", "price": 20, "quantity": 100},
    {"name": "La vida es bella", "price": 15, "quantity": 50},
    {"name": "100 años de soledad", "price": 20, "quantity": 30},
    {"name": "Leopardos al sol", "price": 25, "quantity": 10},
    {"name": "La laguna azul", "price": 10, "quantity": 5}
]

# Enter numbers safely 
def input_num(prompt, tipo=int):
    while True:
        entrada = input(prompt)
        try:
            return tipo(entrada)
        except ValueError:
            print("Invalid entry. Please enter a valid number.")

# Add a new book
def add_books(name, price, quantity):
    for book in inventory:
        if book["name"].lower() == name.lower():  
            print("The book already exists in the inventory.")
            return
    
    
    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"Book '{name}' successfully added with price ${price} and quantity {quantity}.")

# Search books
def search_books(name):
    found = False
    for book in inventory:
        if book["name"].lower() == name.lower():  
            print(f"The book is : {book['name']} | The price is: ${book['price']} | Quantity: {book['quantity']}")
            found = True
            break
    
    if not found:
        print("Book not found. ")

# Update the price 
def update_price_books(name, new_price):
    for book in inventory:
        if book["name"].lower() == name.lower():
            book["price"] = new_price
            print(f"Price of the book'{name}' update to ${new_price}.")
            return
    
    print("Product not found to update.")

#Delete books in inventory 
def del_books(book):
    if book in inventory: 
        del inventory[book]
        print ("The Book {book} was removed from inventory")
    else:
        print ("Book not found")


# Options menu
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Update the price Books")
        print("4. Delete a book ")
        print("6. Leave")
        
        option = input("Choose the options (1-6): ")

        if option == "1":
            name = input("Give me the title of the book: ").strip()
            price = input_num("Give me the price of the book: ", int)
            quantity = input_num("Give me the number of books: ", int)
            add_books(name, price, quantity)
        
        elif option == "2":
            name = input("Name of the book to search for: ").strip()
            search_books(name)
        
        elif option == "3":
            name = input("Name of the book to be updated: ").strip()
            new_price = input_num("Nuevo precio: ", int)
            update_price_books(name, new_price)
        
        elif option == "4":
            name = input("Name of the book to delete: ").strip()
            print ("The book was deleted")

        elif option == "6":
            print("Leaving the program...")
            break
        
        else:
            print("Invalid option. Please choose an option between 1 and 6.")

if __name__ == "__main__":
    menu()



