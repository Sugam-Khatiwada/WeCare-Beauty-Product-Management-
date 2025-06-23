import write

def display_products(products):
    """
    Display all products in a formatted table.
    
    Args:
        products (list): List of product data to display
    """
    print("+"+"-" * 100 + "+")
    print(f"|{'ID':<5}| {'Name':<30}| {'Brand':<20}| {'Price':<10}| {'Quantity':<10}| {'Country':<15}|")
    print("+"+"-" * 100 + "+")
    
    for product in products:
        id = product[0]
        name = product[1][:29] if len(product[1]) > 29 else product[1]
        brand = product[2][:19] if len(product[2]) > 19 else product[2]
        price = str(int(product[3])*2)
        quantity = str(int(int(product[4])*(3/4)))
        country = product[5][:14] if len(product[5]) > 14 else product[5]
        
        print(f"|{id:<5}| {name:<30}| {brand:<20}| {price:<10}| {quantity:<10}| {country:<15}|")
    print("+" + "-" * 100 + "+")
    
def add_summary(shopping_cart):
    """
    Display a summary of products added to the cart.
    
    Args:
        shopping_cart (list): List of products in the cart
    """
    print("+" + "-" * 100 + "+")
    print(f"|{'Checkout Summary':^100}|")
    print("+" + "-" * 100 + "+")
    print(f"|{'Name of Product':<50}| {'Price':<22}| {'Quantity':<24}| ")
    print("+" + "-" * 100 + "+")
    total=0
    for cart in shopping_cart:
        name = cart[1][:49] if len(cart[1]) > 49 else cart[1]
        price = str(int(cart[3]))
        quantity = cart[4]
        print(f"|{name:<50}| {price:<22}| {quantity:<24}|")
        total += int(cart[3])*int(cart[4])
    print("+" + "-" * 100 + "+")
    print(f"|{'Total Amount:':<50} {total:<49}|")
    print("+" + "-" * 100 + "+")
    
def sell_summary(shopping_cart, free):
    """
    Display a summary of products sold with free items.
    
    Args:
        shopping_cart (list): List of products sold
        free (list): List of free items per product
    """
    print("+" + "-" * 100 + "+")
    print(f"|{'Checkout Summary':^100}|")
    print("+" + "-" * 100 + "+")
    print(f"|{'Name of Product':<50}| {'Price':<7}| {'Quantity':<10}| {'Free Item':<10}| {'Total Quantity':<15}|")
    print("+" + "-" * 100 + "+")
    total=0

    for i,cart in enumerate(shopping_cart):
        free_item=free[i]
        name = cart[1][:49] if len(cart[1]) > 49 else cart[1]
        price = str(int(cart[3]))
        quantity = cart[4]
        print(f"|{name:<50}| {price:<7}| {(int(quantity)-free_item):<10}| {free_item:<10}| {int(quantity):<15}|")
        total += int(cart[3])*int(int(cart[4])-free_item)
    print("+" + "-" * 100 + "+")
    print(f"|{'Total Amount:':<59} {total:<40}|")
    print("+" + "-" * 100 + "+")
    
def add_product(products):
    """
    Add new products or update quantities of existing products.
    
    This function allows:
    - Adding quantity to existing products
    - Creating new products with details
    - Generating invoices for the transaction
    
    Args:
        products (list): Current list of products
        
    Returns:
        list: Updated list of products
    """
    shopping_cart=[]
    while True:
        exist = False
        # Get and validate product name
        while True:
            try:
                name = str(input("Enter product name: "))
                name = name.upper()
                if len(name) == 0:
                    raise ValueError("Product name cannot be empty.")
                break
            except ValueError as e:
                if "Product name cannot be empty." in str(e):
                    print(f"Invalid input: {e}")
                else:
                    print("Invalid input. Please enter a valid product name.")
        
        # Check if product exists and update quantity
        for product in products:
            if product[1].strip() == name.strip():
                while True:
                    try:
                        quantity = int(input("Enter product quantity to add: "))
                        if int(quantity) <= 0:
                            raise ValueError("Enter positive integer.")
                        elif int(quantity) > 0:
                            quantity = str(int(quantity))
                            break
                    except ValueError as e:
                        if "Enter positive integer." in str(e):
                            print(f"Invalid input: {e}")
                        else:
                            print("Invalid input. Please enter a valid integer.")

                product[4] = str(int(product[4]) + int(quantity))
                exist = True
                cart=[product[0], product[1], product[2], product[3], quantity, product[5]]
                shopping_cart.append(cart)
                break
                
        # If product doesn't exist, get details and add new product
        if exist == False:
            id = str(len(products)+1)
            while True:
                try:
                    brand = str(input("Enter product brand: "))
                    brand = brand.upper()
                    if len(brand) == 0:
                        raise ValueError("Brand name cannot be empty.")
                    break
                except ValueError as e:
                    if "Brand name cannot be empty." in str(e):
                        print(f"Invalid input: {e}")
                    else:
                        print("Invalid input. Please enter a valid brand name.")

            while True:
                try:
                    price = int(input("Enter product price: "))
                    if int(price) < 0:
                        raise ValueError("Enter positive integer.")
                    elif int(price) > 0:
                        price = str(int(price))
                        break
                except ValueError as e:
                    if "Enter positive integer." in str(e):
                        print(f"Invalid input: {e}")
                    else:
                        print("Invalid input. Please enter a valid integer.")

            while True:
                try:
                    quantity = int(input("Enter product quantity: "))
                    if int(quantity) < 0:
                        raise("Enter positive integer.")
                    elif int(quantity) > 0:
                        quantity = str(int(quantity))
                        break
                except ValueError as e:
                    if "Enter positive integer." in str(e):
                        print(f"Invalid input: {e}")
                    else:
                        print("Invalid input. Please enter a valid integer.")

            while True:
                try:
                    country = str(input("Enter product country: "))
                    country = country.upper()
                    if len(country) == 0:
                        raise ValueError("Country name cannot be empty.")
                    for char in country:
                        if not(char.isalpha() or char.isspace()):
                            raise ValueError("Enter valid country name.")
                    break
                except ValueError as e:
                    if "Country name cannot be empty." in str(e):
                        print(f"Invalid input: {e}")
                    elif "Enter valid country name." in str(e):
                        print(f"Invalid input: {e}")
                    else:
                        print("Invalid input. Please enter a valid country name.")
            products.append([id, name, brand, price, quantity, country])
            cart=[id, name, brand, price, quantity, country]
            shopping_cart.append(cart)

        # Ask if user wants to add another product
        while True:
            continue_shopping = input("Do you want to add another product? (Y/N): ").strip().upper()
            if continue_shopping == 'N':
                break
            elif continue_shopping == 'Y':
                break
            else:
                print("Invalid choice. Please enter Y or N.")

        if continue_shopping == 'N':
            break

    write.save_products(products)
    add_summary(shopping_cart)
    
    # Get and validate vendor name
    while True:
        try:
            vendor = str(input("Enter the name of vendor: "))
            vendor = vendor.upper()
            if len(vendor) == 0:
                raise ValueError("Vendor name cannot be empty.")
            for char in vendor:
                if not(char.isalpha() or char.isspace()):
                    raise ValueError("Enter valid vendor name.")
            break
        except ValueError as e:
            if "Enter valid vendor name." in str(e):
                print(f"Invalid input: {e}")
            elif "Vendor name cannot be empty." in str(e):
                print(f"Invalid input: {e}")
            else:
                print("Invalid input. Please enter a valid vendor name.")

    write.add_invoices(shopping_cart,vendor)
    print("Product added successfully.")
    return products
    
def sell_product(products):
    """
    Sell products with buy 3 get 1 free promotion.
    
    This function handles:
    - Product selection by ID
    - Quantity validation and stock checking
    - Free item calculation (buy 3 get 1 free)
    - Multiple product purchase in one transaction
    - Invoice generation
    
    Args:
        products (list): Current list of products
        
    Returns:
        list: Updated list of products after sales
    """
    shopping_cart=[]
    free=[]
    display_products(products)
    
    while True:
        product_id = input("Enter the product ID to buy: ").strip()
        exist = False
        quantitynotFound = False
        # Find product by ID and handle purchase
        for product in products:
            if product[0] == product_id:
                exist = True
                while True:
                    try:
                        quantity = int(input("Enter quantity to buy: ").strip())
                        free_item=int(quantity)//3
                        available_quantity=int(int(product[4])*(3/4))
                        if int(quantity) <= 0:
                            print("Invalid quantity. Please enter a positive number.")
                        elif available_quantity == 0:
                            quantity = 0
                            free_item = 0
                            print("Product is out of stock.")
                            quantitynotFound = True
                            break
                        elif available_quantity < quantity:
                            print(f"Insufficient stock. Available quantity is {available_quantity}.")
                        elif available_quantity >= quantity:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
                # Update inventory and add to cart
                product[4] = str(int(product[4]) - int(quantity+free_item))
                cart=[product[0], product[1], product[2], int(product[3])*2, str(int(quantity)+free_item), product[5]]
                free.append(free_item)
                shopping_cart.append(cart)
                break

        if exist == False:
            print("Product not found. Select a valid product ID.")
            continue

        # Ask if user wants to buy another product
        if quantitynotFound == True or quantitynotFound == False:
            while True:
                continue_shopping = input("Do you want to buy another product? (Y/N): ").strip().upper()
                if continue_shopping == 'N':
                    break
                elif continue_shopping == 'Y':
                    break
                else:
                    print("Invalid choice. Please enter Y or N.")

            if continue_shopping == 'N':
                break

    i = 0
    while i < len(shopping_cart):
        if shopping_cart[i][4] == '0':
            shopping_cart.pop(i)
            free.pop(i)
            # Don't increment i since the next item has shifted to this position
        else:
            i += 1  # Move to next item only if we didn't remove anything

    if len(shopping_cart) == 0:
        print("no product bought.")
        return products
    
    elif len(shopping_cart) >= 1:
        # Save changes and generate invoice
        write.save_products(products)
        sell_summary(shopping_cart,free)

        # Get and validate customer name - must contain valid characters only
        while True:
            try:
                customer = str(input("Enter the name of customer: "))
                customer = customer.upper()
                if len(customer) == 0:
                    raise ValueError("Customer name cannot be empty.")
                for char in customer:
                    if not(char.isalpha() or char.isspace()):
                        raise ValueError("Enter valid customer name.")
                break
            except ValueError as e:
                if "Enter valid customer name." in str(e):
                    print(f"Invalid input: {e}")
                else:  
                    print("Invalid input. Please enter a valid customer name.")
        
        # Generate invoice and confirm purchase
        write.sell_invoices(shopping_cart,customer,free)
        print("Product sold successfully.")
        return products