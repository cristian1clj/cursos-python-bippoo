import os
import time
import random

def normalize(s):
    remplaceable = (
        ('á','a'),
        ('é','e'),
        ('í','i'),
        ('ó','o'),
        ('ú','u')
    )

    for value in remplaceable:
        if s == value[0]:
            s = value[1]

    return s

def hangman_view(error_counter, status, word, points):
    hangman = [f"""
    ||==========      lives:{error_counter}    points:{points}
    ||         |
    ||         |
    ||         O
    ||        /|/
    ||         /7
    ||       ######
    ||#######      #######
    ||                  ||  word: {"".join(word)}
    ||                  ||
    """, f"""
    ||==========      lives:{error_counter}    points:{points}
    ||         |
    ||         |
    ||        \O/
    ||         |
    ||         /7
    || ######
    ||#######      #######
    ||                  ||  the word was: {"".join(word)}
    ||                  ||
    """, f"""
    ||==========      lives:{error_counter}    points:{points}
    ||         
    ||                          #     # ##### #    #
    ||        \O/               #  #  #   #   # #  #
    ||         |                #  #  #   #   #  # #
    ||         /7               ####### ##### #   ##
    ||       ######
    ||#######      #######
    ||                  ||  word: {"".join(word)}
    ||                  ||
    """]

    if error_counter != 0 and status == False:
        print (hangman[0])
    elif error_counter !=0 and status == True:
        print (hangman[2])
    else:
        print (hangman[1])

def random_word():
    with open("palabras_ahorcado.txt", "r", encoding="utf-8") as f:
        words = [line[0:-1] for line in f]

    word = random.choice(words)
    return word

def add_puntuaction(nickname, puntuaction):
    all_puntuactions = {}
    with open("puntuaciones.txt", "r", encoding="utf-8") as f:
        for line in f:
            aux = line.split()
            all_puntuactions[aux[0]] = [aux[1], aux[2]]

    for key, values in all_puntuactions.items():
        if int(values[1]) < int(puntuaction):
            all_puntuactions[key] = [nickname, puntuaction]
            nickname = values[0]
            puntuaction = values[1]

        if key == '10':
            break

    with open("puntuaciones.txt", "w", encoding="utf-8") as f:
        for key, values in all_puntuactions.items():
            f.write(f"{key} {values[0]} {values[1]}")
            f.write("\n")

def hangman_game(points):
    word = random_word()
    word_view = ['-' for value in word]
    word = [value for value in word]
    # print(word)
    win = False
    lives = 8

    while lives > 0 and not win:
        try:
            exist = False

            hangman_view(lives, win, word_view, points)
            character = input("Write: ").lower()

            if character == "":
                raise ValueError("error: Ingrese alguna letra.")
            elif character.isnumeric():
                raise ValueError("error: no se admiten valores numericos")

            for i in range(len(word)):
                if normalize(word[i]) == character and word_view[i] == '-':
                    exist = True
                    points += 100
                    word_view[i] = character

                elif normalize(word[i]) == character and word_view[i] == character:
                    exist = True
                    lives -= 1

            if not exist:
                lives -= 1

            for value in word_view:
                if value != '-':
                    win = True
                else:
                    win = False
                    break
                
            os.system("cls")

        except ValueError as ve:
            print(ve)
            time.sleep(3)
            os.system("cls")

    hangman_view(lives, win, word, points)
    input("Press enter key to proceed.")

    if not win:
        nickname = input("\nWrite your nickname: ")
        add_puntuaction(nickname, points)
        points = 0

    return points

def show_BS():
    all_puntuactions = {}
    with open("puntuaciones.txt", "r", encoding="utf-8") as f:
        for line in f:
            aux = line.split()
            all_puntuactions[aux[0]] = [aux[1], aux[2]]

    for key, values in all_puntuactions.items():
        print (f"{key}. {values[0]}  {values[1]}")

    input("Press any key to proceed.")

def menu():
    opcion = input("""
    [1] New game.
    [2] Best scores.
    [3] Exit.
    Choose the option: """)

    return opcion

def create_puntiaction_txt():
    if not os.path.isfile("puntuaciones.txt"):
        with open("puntuaciones.txt", "w", encoding="utf-8") as f:
            for i in range(1,11):
                f.write(f"{i} # 0")
                f.write("\n")

def run():
    create_puntiaction_txt()
    puntuaction = 0

    while True:
        try:
            opcion = menu()
            if opcion == "":
                raise ValueError("error: Ingrese alguna letra.")
            elif not opcion.isnumeric():
                raise ValueError("error: solo se admiten valores numericos")
                
            os.system("cls")

            if opcion == '1':
                puntuaction = hangman_game(puntuaction)
            elif opcion == '2':
                show_BS()
            elif opcion == '3':
                print ("\nBye...")
                break
            else:
                print ("\nerror: Choose a valid option.")

        except ValueError as ve:
            print (ve)
            time.sleep(3)
            os.system("cls")

if __name__ == "__main__":
    run()
