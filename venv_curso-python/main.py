from os import system
from interface.mn import menu
from interface.data_options import *
from models.data import InformationManagement
from models.records import InformationMovement
from files import *


# Main program stucture
def run():
    system("cls")
    
    create_files()

    while True:
        option: str = menu("MAIN")

        if option == '1':
            while True:
                option_products: str = menu("PRODUCTS")
                identifier: str = "PRODUCT"
                file: str = FILES["PRODUCTS"]

                if option_products == '1':
                    add_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '2':
                    modify_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '3':
                    delete_information(identifier, file, InformationManagement)
                    system("cls")
                    
                elif option_products == '4':
                    search_information(identifier, file, InformationManagement)
                    system("cls")
                    
                elif option_products == '5':
                    show_all_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '6':
                    break

        elif option == '2':
            while True:
                option_products: str = menu("SUPPLIERS")
                identifier: str = "SUPPLIER"
                file: str = FILES["SUPPLIERS"]

                if option_products == '1':
                    add_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '2':
                    modify_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '3':
                    delete_information(identifier, file, InformationManagement)
                    system("cls")
                    
                elif option_products == '4':
                    search_information(identifier, file, InformationManagement)
                    system("cls")
                    
                elif option_products == '5':
                    show_all_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '6':
                    break

        elif option == '3':
            while True:
                option_products: str = menu("CUSTOMERS")
                identifier: str = "CUSTOMER"
                file: str = FILES["CUSTOMERS"]

                if option_products == '1':
                    add_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '2':
                    modify_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '3':
                    delete_information(identifier, file, InformationManagement)
                    system("cls")
                    
                elif option_products == '4':
                    search_information(identifier, file, InformationManagement)
                    system("cls")
                    
                elif option_products == '5':
                    show_all_information(identifier, file, InformationManagement)
                    system("cls")

                elif option_products == '6':
                    break

        elif option == '4':
            identifier: str = "ENTRY"
            file: str = FILES["ENTRIES"]
            file_aux: str = FILES["SUPPLIERS"]

            register_movement(identifier, file, file_aux, InformationMovement)
            system("cls")

        elif option == '5':
            identifier: str = "SALE"
            file: str = FILES["SALES"]
            file_aux: str = FILES["CUSTOMERS"]

            register_movement(identifier, file, file_aux, InformationMovement)
            system("cls")

        elif option == '6':
            while True:
                option_info = menu("INFO REPORTS")
                
                if option_info == '1':
                    pass
                
                elif option_info == '2':
                    pass
                
                elif option_info == '3':
                    pass
                
                elif option_info == '4':
                    pass
                
                elif option_info == '5':
                    pass
                
                elif option_info == '6':
                    pass
                
                elif option_info == '7':
                    pass
                
                elif option_info == '8':
                    pass
                
                elif option_info == '9':
                    pass
                
                elif option_info == '10':
                    pass
                
                elif option_info == '11':
                    pass
                
                elif option_info == '12':
                    pass

        elif option == '7':
            print("\nExiting the program...")
            break


if __name__ == '__main__':
    run()
