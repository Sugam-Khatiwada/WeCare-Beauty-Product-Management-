from datetime import datetime

def save_products(products):
    """
    Save product data to file.
    
    Args:
        products (list): List of products to save
    """
    try:
        with open("Product.txt", 'w') as file:
            # Write each product as a comma-separated line
            for product in products:
                file.write(", ".join(product) + "\n")
    except Exception as e:
        print(f"An error occurred while saving products: {e}")

def add_invoices(shopping_cart, vendor):
    """
    Create invoice for added products.
    
    Args:
        shopping_cart (list): List of products added to inventory
        vendor (str): Name of the vendor supplying the products
    """
    
    # Generate unique invoice filename using timestamp
    invoice = datetime.now()
    invoice_name = str(invoice.year)+ "-" + str(invoice.month)+ "-" + str(invoice.day)+ "-" + str(invoice.hour)+ "-" + str(invoice.minute)+"-" + str(invoice.second)+"-"+ str(invoice.microsecond)
    dateOfPurchase = str(invoice.year)+"-"+str(invoice.month)+"-"+str(invoice.day)+" "+str(invoice.hour)+":"+str(invoice.minute)+":"+str(invoice.second)
    try:
        with open(f"Add_Invoices/{vendor}_{invoice_name}.txt", 'w') as file:
            # Create invoice header
            file.write("+" + "-" * 100 + "+\n")
            file.write(f"|{'INVOICE':^100}|\n")
            file.write(f"|{'WeCare Beauty Products':^100}|\n")
            file.write("+" + "-" * 100 + "+\n")
            file.write(f"| Name of Vendor: {vendor:<83}|\n")
            file.write(f"| Date of Purchase: {dateOfPurchase:<81}|\n")
            file.write("+" + "-" * 100 + "+\n")
            file.write(f"|{'ID':<5}| {'Name':<30}| {'Brand':<20}| {'Price':<10}| {'Quantity':<10}| {'Country':<15}|\n")
            file.write("+" + "-" * 100 + "+\n")
            
            # Calculate and write product details
            total_amount = 0
            for cart in shopping_cart:
                id = cart[0]
                name = cart[1][:29] if len(cart[1]) > 29 else cart[1]
                brand = cart[2][:19] if len(cart[2]) > 19 else cart[2]
                price = str(int(cart[3]))
                quantity = cart[4]
                country = cart[5][:14] if len(cart[5]) > 14 else cart[5]
                
                file.write(f"|{id:<5}| {name:<30}| {brand:<20}| {price:<10}| {quantity:<10}| {country:<15}|\n")
                
                total_amount += int(cart[3]) * int(quantity)
            
            # Write invoice footer with total amount    
            file.write("+" + "-" * 100 + "+\n")
            vat = (13 / 100) * total_amount
            file.write(f"|{'Total Amount:':<58} {total_amount:<41}|\n")
            file.write(f"|{'Vat(13%):':<58} {vat:<41}|\n")
            file.write(f"|{'Grand Total:':<58} {(total_amount+vat):<41}|\n")
            file.write("+" + "-" * 100 + "+")
        print(f"Invoice created successfully")
    except Exception as e:
        print(f"An error occurred while creating the invoice: {e}")


def sell_invoices(shopping_cart, customer, free):
    """
    Create invoice for sold products with free items.
    
    Args:
        shopping_cart (list): List of products sold
        customer (str): Name of the customer making the purchase
        free (list): List of free items given for each product
    """
    
    # Generate unique invoice filename using timestamp        
    invoice = datetime.now()
    invoice_name = str(invoice.year)+ "-" + str(invoice.month)+ "-" + str(invoice.day)+ "-" + str(invoice.hour)+ "-" + str(invoice.minute)+"-" + str(invoice.second)+"-"+ str(invoice.microsecond)
    dateOfPurchase = str(invoice.year)+"-"+str(invoice.month)+"-"+str(invoice.day)+" "+str(invoice.hour)+":"+str(invoice.minute)+":"+str(invoice.second)
    try:
        with open(f"Sell_Invoices/{customer}_{invoice_name}.txt", 'w') as file:
            # Create invoice header
            file.write("+" + "-" * 117 + "+\n")
            file.write(f"|{'INVOICE':^117}|\n")
            file.write(f"|{'WeCare Beauty Products':^117}|\n")
            file.write("+" + "-" * 117 + "+\n")
            file.write(f"| Name of Customer: {customer:<98}|\n")
            file.write(f"| Date of Purchase: {dateOfPurchase:<98}|\n")
            file.write("+" + "-" * 117 + "+\n")
            file.write(f"|{'ID':<5}| {'Name':<25}| {'Brand':<15}| {'Price':<10}| {'Quantity':<10}| {'Free Item':<10}| {'Total Quantity':<15}| {'Country':<13}|\n")
            file.write("+" + "-" * 117 + "+\n")
            
            # Calculate and write product details with free items
            total_amount = 0
            for i, cart in enumerate(shopping_cart):
                id = cart[0]
                name = cart[1][:29] if len(cart[1]) > 29 else cart[1]
                brand = cart[2][:19] if len(cart[2]) > 19 else cart[2]
                price = str(int(cart[3]))
                quantity = cart[4]
                country = cart[5][:14] if len(cart[5]) > 14 else cart[5]
                free_item = free[i]

                file.write(f"|{id:<5}| {name:<25}| {brand:<15}| {price:<10}| {(int(quantity)-int(free_item)):<10}| {free_item:<10}| {int(quantity):<15}| {country:<13}|\n")

                total_amount += int(cart[3]) * int(int(quantity)-free_item)

            # Write invoice footer with total amount
            file.write("+" + "-" * 117 + "+\n")
            vat = (13 / 100) * total_amount
            file.write(f"|{'Total Amount:':<58} {total_amount:<58}|\n")
            file.write(f"|{'Vat(13%):':<58} {vat:<58}|\n")
            file.write(f"|{'Grand Total:':<58} {(total_amount+vat):<58}|\n")
            file.write("+" + "-" * 117 + "+")
        print(f"Invoice created successfully")
    except Exception as e:
        print(f"An error occurred while creating the invoice: {e}")