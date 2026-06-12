# Inventory Management System

A Python-based application for managing products, handling sales, and generating invoices.

## Project Structure

- **`main.py`**: The main entry point of the application. Run this script to start the program.
- **`operation.py`**: Contains the core business logic and operations for handling products and transactions.
- **`read.py`**: Handles reading data from the data source (e.g., parsing `Product.txt`).
- **`write.py`**: Handles writing data, such as updating inventory and generating invoice files.
- **`Product.txt`**: The text-based database storing the current inventory of products.
- **`Add_Invoices/`**: Directory where generated generated purchase/restock invoices are saved.
- **`Sell_Invoices/`**: Directory where generated sales invoices are saved.

## How to Run

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt in the project directory.
3. Run the following command:
   ```bash
   python main.py
   ```

## Features

- Read and display current product inventory.
- Process sales and automatically deduct stock.
- Restock items and update inventory.
- Automatically generate text-based invoices for both sales and restocks.
