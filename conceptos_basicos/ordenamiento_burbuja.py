import random

def sort_list(list, counter = 0):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            counter += 1
        
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            
    return (list, counter)

if __name__ == '__main__':
    list_size = int(input('Enter the list size: '))
    
    list = [random.randint(0, 100) for i in range(list_size)]
    
    print("- list: ")
    print(list)
    
    (new_list, counter) = sort_list(list)
    
    print("\n   - New list: ")
    print(new_list)
    print(f'the numero of steps are: {counter}')
