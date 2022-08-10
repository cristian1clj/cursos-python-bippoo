import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def generate_password():
    password = []

    while len(password) < 16:
        password.append(random.choice(characters))

    password = "".join(password)
    return str(password)

def run():
    repeat = True
    
    while repeat:
        opcion = input("""
            |---------------------------|
            |[1] Generate password.
            |[2] exit the program.
            |---------------------------|
        Choose an option: """)
        
        if opcion == '1':
            print ("Password: " + generate_password())

        elif opcion == '2':
            repeat = False
            print ("\nSuccessful exit.")

        else:
            print ("error: la opcion ingresada no esta disponible en el menu de opciones.")


if __name__ == "__main__":
    run()
