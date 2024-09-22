def init_db():
    # Initializing the database schema
    print("Database initialized.")

def menu():
    print("\nPetCare Hub Menu:")
    print("1. Add Owner")
    print("2. Add Pet")
    print("3. Add Care Schedule")
    print("4. Add Vet Visit")
    print("0. Exit")

def main():
    init_db()  # Initialize database schema
  
    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            # Add owner functionality
            print("Adding owner...")
            pass
        elif choice == "2":
            # Add pet functionality
            print("Adding pet...")
            pass
        elif choice == "3":
            # Add care schedule functionality
            print("Adding care schedule...")
            pass
        elif choice == "4":
            # Add vet visit functionality
            print("Adding vet visit...")
            pass
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
