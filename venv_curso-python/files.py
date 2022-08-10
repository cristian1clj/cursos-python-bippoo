from os import path, mkdir
from typing import Dict

# Defines files name and files direction
FILES: Dict[str, str] = {
    "PRODUCTS":".information-files/.products.csv", 
    "SUPPLIERS":".information-files/.suppliers.csv", 
    "CUSTOMERS":".information-files/.customers.csv", 
    "ENTRIES":".information-files/.PEntries.csv", 
    "SALES":".information-files/.PSales.csv", 
    "INVENTORY":".information-files/.inventory.csv"
}


# Creates the files if they dont exist
def create_files():
    if not path.isdir(".information-files"):
        mkdir(".information-files")

    if not path.isfile(FILES["PRODUCTS"]):
        open(FILES["PRODUCTS"], "w").close()
    if not path.isfile(FILES["SUPPLIERS"]):
        open(FILES["SUPPLIERS"], "w").close()
    if not path.isfile(FILES["CUSTOMERS"]):
        open(FILES["CUSTOMERS"], "w").close()
    if not path.isfile(FILES["ENTRIES"]):
        open(FILES["ENTRIES"], "w").close()
    if not path.isfile(FILES["SALES"]):
        open(FILES["SALES"], "w").close()
    if not path.isfile(FILES["INVENTORY"]):
        open(FILES["INVENTORY"], "w").close()
