def main():
    init_db()  # Initialize database schema
    session = Session()
    
    while True:
        print("PetCare Hub Menu:")
        print("1. Add Owner")
        print("2. Add Pet")
        print("3. Add Care Schedule")
        print("4. Add Vet Visit")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            # Add owner functionality
            pass
        elif choice == "2":
            # Add pet functionality
            pass
        elif choice == "3":
            # Add care schedule functionality
            pass
        elif choice == "4":
            # Add vet visit functionality
            pass
        else:
            print("Invalid choice. Please try again.")
