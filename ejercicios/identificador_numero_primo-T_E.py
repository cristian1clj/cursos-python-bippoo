def es_primo(x: int) -> bool:
    if x > 1:
        for i in range(1, x):
            if (x % i == 0) and (i != 1 and i != x):
                return False
        
        return True
    
    return False

if __name__ == '__main__':
    numero: int = int(input("Ingrese un numero para saber si es primo: "))
    
    print(f"\nEl numero {numero} {'es' if es_primo(numero) else 'no es'} un numero primo.")
