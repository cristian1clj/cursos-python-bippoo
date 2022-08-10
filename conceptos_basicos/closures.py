# Es una tecnica por la cual una variable en un scope superior puede ser recordada por una función en un
# scope inferior, incluso si el scope superior es eliminado despues.


# -------------------------------------------------------------------------------
# def make_multiplication(x: int):
#     def multiplication(n: int):
#         return x * n
    
#     return multiplication

# number1 = make_multiplication(10)
# print(number1(5))
# -------------------------------------------------------------------------------
# def make_repeater_of(n: int):
#     def repeater(s: str):
#         assert type(s) == str, "Only can put strings, no numbers"
#         print(s * n)
        
#     return repeater

# repeat_5 = make_repeater_of(5)
# repeat_5('platzi')
# -------------------------------------------------------------------------------

def make_division_by(n: int) -> int:
    def division(x: int) -> float:
        return x / n
    
    return division

if __name__ == '__main__':
    division_by_3 = make_division_by(18)
    print(division_by_3(54))
