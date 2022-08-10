from time import sleep
from function_execution_time import execution_time

@execution_time
def fibo_gen(max: int):
    n1 = 0
    n2 = 1
    count = 0
    
    while count <= max-1:
        yield n1
        n1, n2 = n2, n1+n2
        count += 1

def run():
    fibo = fibo_gen(5)
    
    for element in fibo:
        print(element)
        sleep(1)
    

if __name__ == '__main__':
    run()