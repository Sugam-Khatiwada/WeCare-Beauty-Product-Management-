import read
import write
import operation

def menu():
    """
    Display menu options and get user selection.
    
    Returns:
        int: User's choice (1-4)
    """
    print(f"+------------------------------+\n|{'1. Display Products':<30}|\n|{'2. Add Product':<30}|\n|{'3. Sell Product':<30}|\n|{'4. Exit':<30}|\n+------------------------------+")
    try:
        choice = int(input("\nEnter the number that you want to choose: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return menu()
    return choice

def main():
    """
    Main program function that runs the WeCare inventory system.
    
    Loads product data, displays menu options, and processes user choices
    until the user chooses to exit.
    
    Returns:
        None
    """
    print(f"+------------------------------+\n|{'WeCare':<30}|")
    products = read.load_products()
    
    while True:
        choice = menu()
        
        if choice == 1:
            operation.display_products(products)
        elif choice == 2:
            print(f"\n+-------------------------+\n|{'Add New Product':<25}|\n+-------------------------+\n")
            products = operation.add_product(products)
        elif choice == 3:
            print(f"\n+-------------------------+\n|{'Sell Product':<25}|\n+-------------------------+")
            products = operation.sell_product(products)
        elif choice == 4:
            print("\nExited the Program!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

main()
