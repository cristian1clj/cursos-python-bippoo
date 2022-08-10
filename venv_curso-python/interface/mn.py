from os import system
from time import sleep
from typing import Dict, Tuple

# Defines the menus options
MENUS: Dict[str, Tuple[str]] = {
    "MAIN":(
        "Product management.", 
        "Supplier management.", 
        "Customer management.", 
        "Products entries.", 
        "Products sales.", 
        "Information reports.", 
        "Exit."
    ), 
    "PRODUCTS":(
        "Add product.", 
        "Modify product.", 
        "Delete product.", 
        "Search product.", 
        "Show all products.", 
        "Back to main menu."
    ), 
    "SUPPLIERS":(
        "Add supplier.", 
        "Modify supplier.", 
        "Delete supplier.", 
        "Search supplier.", 
        "Show all suppliers.", 
        "Back to main menu."
    ), 
    "CUSTOMERS":(
        "Add customer.", 
        "Modify customer.", 
        "Delete customer.", 
        "Search customer.", 
        "Show all customers.", 
        "Back to main menu."
    ), 
    "INFO REPORTS":(
        "Current inventory.",
        "All entries in a date range.",
        "All sales in a date range.",
        "Total value of entries in a date range.",
        "Total value of sales in a date range.",
        "All records of one product in a date range.",
        "Product with more records",
        "Date with more records",
        "All sales of one customer in a date range.",
        "All sales of one customer and one product in a date range.",
        "All entries of one supplier in a date range.",
        "All entries of one supplier and one product in a date range."
    )
}


# Menus interface structure
def menu(identifier: str) -> str:
    print(f"|{'-' * 25} {identifier} MENU {'-' * 25}|\n")
    
    try:
        for i, op in enumerate(MENUS[identifier]):
            print(f"[{i+1}] {op}")
        option: str = input("Choose the option: ")

        if option == "":
            raise ValueError("error: Enter any menu option.")
        
        elif not option.isnumeric():
            raise ValueError("error: Only numeric values are accepted.")
        
        elif int(option) < 1 or int(option) > len(MENUS[identifier]):
            raise ValueError("error: Choose a valid option.")

    except ValueError as ve:
        print(ve)
        sleep(3)
        system("cls")

    system("cls")
    return option
