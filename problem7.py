items= []
while True:
    print("\n 1. Add an item")
    print("2. Remove an item")
    print("3. display the list")
    print("4. Quit")

    choice = input("Enter your choice:").strip()
    if choice == "1":
        item = input("Enter the item to add:").strip
        items.append(item)
        print(item, "Added to the list")
    elif choice == "2":
        item = input("Enter the item to remove:").strip()
        if item in items:
            items.remove(item)
            print(item, "Removed from the list")
        else:
            print(item, "not found in the list")
    elif choice == "3":
        print("Current list:", items)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

       