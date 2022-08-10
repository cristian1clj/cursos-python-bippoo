from function_execution_time import execution_time
import typing

@execution_time
def table(num: int, max: int):
    for i in range(max + 1):
        print(f"{num} * {i} = {num * i}")
        
def run():
    num = int(input("Tabla del: "))
    max = int(input("Del 0 al: "))
    
    table(num, max)
    
if __name__ == '__main__':
    run()
