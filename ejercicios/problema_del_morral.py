def morral(capacidad_morral, pesos, valores, n):
    if n == 0 or capacidad_morral == 0:
        return 0
    
    if pesos[n - 1] > capacidad_morral:
        return morral(capacidad_morral, pesos, valores, n - 1)
    
    return max(valores[n - 1] + morral(capacidad_morral - pesos[n - 1], pesos, valores, n - 1), 
               morral(capacidad_morral, pesos, valores, n - 1))
    

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad_morral = 50
    n = len(valores)
    
    resultado = morral(capacidad_morral, pesos, valores, n)
    print(resultado)
