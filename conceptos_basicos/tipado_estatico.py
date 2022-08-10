# Por medio del modulo "typing" se puede trabajar python (lenguaje dinamico) como un lenguaje de tipado estatico.

from typing import List, Dict, Tuple

positives: List[int] = [1, 2, 3, 4, 5]

users: Dict[str, int] = {
    'colombia': 1,
    'venezuela': 2,
    'ecuador': 3
}

countries: List[Dict[str, str]] = [
    {
        'name': 'colombia',
        'people': '345345345'
    }, 
    {
        'name': 'venezuela',
        'people': '67867868'
    }, 
    {
        'name': 'ecuador',
        'people': '54646465'
    }
]

numbers: Tuple = (1, 2, 3, 4)

def suma(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    print(suma(1, 2))