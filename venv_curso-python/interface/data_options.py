import csv
from typing import Dict, List, Tuple
from models.data import InventaryManagement, DATA_SCHEMA, file_empty

INFORMATION_WORDS: Dict[str, Tuple[str]] = {
    "PRODUCT":(
        "code", 
        "name", 
        "unitary price"
    ), 
    "SUPPLIER":(
        "nit", 
        "name", 
        "address"
    ), 
    "CUSTOMER":(
        "nit", 
        "name", 
        "address"
    )
}
MOVEMENT_WORDS: Dict[str, Tuple[str]] = {
    "ENTRY":("SUPPLIER", "PRODUCT"), 
    "SALE":("CUSTOMER", "PRODUCT")
}


def add_information(identifier: str, file: str, data_management):
    print(f"|{'-' * 25} ADD {identifier} {'-' * 25}|\n")

    while True:
        data1: str = input(f"\nWrite the {identifier} {INFORMATION_WORDS[identifier][0]}: ")

        if _valid_numerical_value(data1):
            if not _exists_identifier(data1, file):
                break
            else:
                print("The entered value already exists.")

    while True:
        data2: str = input(f"\nWrite the {identifier} {INFORMATION_WORDS[identifier][1]}: ")
        
        if _valid_string_value(data2):
            break

    while True:
        data3: str = input(f"\nWrite the {identifier} {INFORMATION_WORDS[identifier][2]}: ")

        if identifier == "PRODUCT":
            if _valid_numerical_value(data3):
                break
        else:
            if _valid_string_value(data3):
                break

    obj: object = data_management(file, data1, data2, data3)
    obj.add()

    if identifier == "PRODUCT":
        inv_obj: object = InventaryManagement(data1, 0)
        inv_obj.add()

    print(f"\nThe {identifier} was stored correctly.")
    input("Press any key to continue...")


def modify_information(identifier: str, file: str, data_management):
    print(f"|{'-' * 25} MODIFY {identifier} {'-' * 25}|\n")

    while True:
        data1: str = input(f"\nWrite the {identifier} {INFORMATION_WORDS[identifier][0]}: ")

        if _valid_numerical_value(data1):
            if _exists_identifier(data1, file):
                break
            else:
                print("The entered value doesn't exists.")

    while True:
        data2: str = input(f"\nWrite the new {identifier} {INFORMATION_WORDS[identifier][1]}: ")
        
        if _valid_string_value(data2):
            break

    while True:
        data3: str = input(f"\nWrite the new {identifier} {INFORMATION_WORDS[identifier][2]}: ")

        if identifier == "PRODUCT":
            if _valid_numerical_value(data3):
                break
        else:
            if _valid_string_value(data3):
                break

    obj: object = data_management(file, data1, data2, data3)
    obj.modify()
    
    print(f"\nThe {identifier} was modified correctly.")
    input("Press any key to continue...")


def delete_information(identifier: str, file: str, data_management):
    print(f"|{'-' * 25} DELETE {identifier} {'-' * 25}|\n")

    while True:
        data1: str = input(f"\nWrite the {identifier} {INFORMATION_WORDS[identifier][0]}: ")

        if _valid_numerical_value(data1):
            if _exists_identifier(data1, file):
                break
            else:
                print("The entered value doesn't exists.")

    while True:
        confirmation: str = input(f"Are you sure to delete this {identifier}? (Y/N): ")
        
        if confirmation.upper() == 'Y':
            obj: object = data_management(file, data1, None, None)
            obj.delete()

            if identifier == "PRODUCT":
                inv_obj: object = InventaryManagement(data1, None)
                inv_obj.delete()

            print(f"\nThe {identifier} was deleted correctly.")
            break
        
        elif confirmation.upper() == 'N':
            print("\nOK, cancelated successfully.")
            break
        
        else:
            print("error: Choose a valid option.")

    input("Press any key to continue...")


def search_information(identifier: str, file: str, data_management):
    print(f"|{'-' * 25} SEARCH {identifier} {'-' * 25}|\n")

    while True:
        data1: str = input(f"\nWrite the {identifier} {INFORMATION_WORDS[identifier][0]}: ")

        if _valid_numerical_value(data1):
            if _exists_identifier(data1, file):
                break
            else:
                print("The entered value doesn't exists.")

    obj: object = data_management(file, data1, None, None)
    information: Dict[str, str] = obj.search()

    print(f"\n\t+ {INFORMATION_WORDS[identifier][0]}: {information['id']}")
    print(f"\t+ {INFORMATION_WORDS[identifier][1]}: {information['name']}")
    print(f"\t+ {INFORMATION_WORDS[identifier][2]}: {information['ad_pr']}")
    input("Press any key to continue...")


def show_all_information(identifier: str, file: str, data_management):
    print(f"|{'-' * 25} SHOW ALL {identifier} {'-' * 25}|\n")

    obj: object = data_management(file, None, None, None)
    information: List[Dict[str, str]] = obj.show_all()

    for values in information:
        print(f"\n\t+ {INFORMATION_WORDS[identifier][0]}: {values['id']}")
        print(f"\t+ {INFORMATION_WORDS[identifier][1]}: {values['name']}")
        print(f"\t+ {INFORMATION_WORDS[identifier][2]}: {values['ad_pr']}")
    input("Press any key to continue...")


def register_movement(identifier: str, file: str, file_aux: str, data_management):
    print(f"|{'-' * 25} REGISTER {identifier} {'-' * 25}|\n")

    while True:
        data1: str = input(f"\nWrite the {MOVEMENT_WORDS[identifier][0]} {INFORMATION_WORDS[MOVEMENT_WORDS[identifier][0]][0]}: ")

        if _valid_numerical_value(data1):
            if _exists_identifier(data1, file_aux):
                break
            else:
                print("The entered value doesn't exists.")
    
    while True:
        data2: str = input(f"\nWrite the {MOVEMENT_WORDS[identifier][1]} {INFORMATION_WORDS[MOVEMENT_WORDS[identifier][1]][0]}: ")

        if _valid_numerical_value(data2):
            if _exists_identifier(data2, "Information files/products.csv"):
                break
            else:
                print("The entered value doesn't exists.")

    while True:
        data3: str = input(f"\nWrite the {MOVEMENT_WORDS[identifier][1]} amount: ")

        if _valid_numerical_value(data3):
            break

    if identifier == "ENTRY":
        obj: object = data_management(file, identifier, data1, data2, data3)
        obj.add()
        print(f"\nThe {identifier} was stored correctly.")

    elif identifier == "SALE":
        if _exists_amount("Information files/inventory.csv", data2, data3):
            obj: object = data_management(file, identifier, data1, data2, data3)
            obj.add()
            print(f"\nThe {identifier} was stored correctly.")

    input("Press any key to continue...")


# Validations
def _valid_numerical_value(value: str) -> bool:
    try:
        if value == "":
            raise ValueError("error: Enter any value.")
        elif not value.isnumeric():
            raise ValueError("error: Only numeric values are accepted.")
        elif int(value) < 0:
            raise ValueError("error: Only positive numeric values.")

    except ValueError as ve:
        print(ve)
        return False

    return True


def _valid_string_value(value: str) -> bool:
    try:
        if value.replace(" ", "") == "":
            raise ValueError("error: Enter any value.")

    except ValueError as ve:
        print(ve)
        return False

    return True


def _exists_identifier(value: str, file: str) -> bool:
    if not file_empty(file):
        information: List[Dict[str, str]]
        
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
            information = [row for row in reader]
    
        for values in information:
            if value == values['id']:
                return True

    return False


def _exists_amount(file: str, data1: str, data2: str) -> bool:
    information: List[Dict[str, str]]
    
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Inv"])
        information = [row for row in reader]

    for values in information:
        if values['id'] == data1 and int(values['amount']) < int(data2):
            print(f"There isn't enough amount.\namount: {values['amount']}")
            return False

    return True
