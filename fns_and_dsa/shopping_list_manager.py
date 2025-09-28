def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            print("Choice is a number")
        else:
            print("Choice is not a number")


        if choice == '1':
            # Prompt for and add an item
            item = input("Enter new Item: ")
            shopping_list.append(item)
            print(f"{item} has been added to shopping list. ")
        elif choice == '2':
            # Prompt for and remove an item
             remove_item = input("Enter Item to remove: ")
             for remove_item in shopping_list:
               shopping_list.remove(remove_item)
             print(f"{remove_item} has been removed from shopping list. ")
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()