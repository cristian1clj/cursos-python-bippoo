# Funcion que recibe como parametro otra funcion, le añade cosas, y retorna una funcion diferente.

from datetime import datetime
import typing

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        
        print("\n + Pasaron " + str(time_elapsed.total_seconds()) + " segundos +\n")
        
    return wrapper

@execution_time
def multiplication_table(num: int, max: int):
    for i in range(max + 1):
        print(f"{num} * {i} = {num * i}")
        
def run():
    num: int = int(input("Multiplication table of: "))
    max: int = int(input("From 0 to: "))
    
    multiplication_table(num, max)
        
if __name__ == '__main__':
    run()