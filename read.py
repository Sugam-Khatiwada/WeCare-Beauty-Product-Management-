def load_products():
    """
    Load product data from Product.txt file.
    
    Returns:
        list: Products as lists [id, name, brand, price, quantity, country]
    """
    products = []
    try:
        # Open and read product data from file
        with open("Product.txt", 'r') as file:
            lines = file.readlines()
        
        # Parse each line into product data
        for i in range(len(lines)):
            product = lines[i].strip().split(", ")
            products.append(product)
        return products
    except Exception as e:
        # Handle file not found or other errors
        print(f"An error occurred while loading products: {e}")
        return []