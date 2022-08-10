import csv
import json
import os

# txt flies
def read_txt_file():
    with open('.texto.txt', "r", encoding="utf-8") as f:
        names = [line[0:-1] for line in f]
    print (names)

def write_txt_file():
    names = ["cristian", "jiménez"]
    tmp_table_name = '.texto.tmp'
    with open(tmp_table_name, "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
            
    os.remove('.texto.txt')
    os.rename(tmp_table_name, '.texto.txt')

# csv flies
def read_csv_file():
    with open("texto.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, ["name", "email", "age"])
        people = [row for row in reader]
        
    print(people)

def write_csv_file(people):
    with open("texto.csv", "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, ["name", "email", "age"])
        writer.writerows(people)

# json flies
def read_json_file():
    with open("texto.json") as f:
        people = json.load(f)
        
    print(people)

def write_json_file(people):
    with open("texto.json", "w") as f:
        json.dump(people, f, indent=4)
        

def run():
    open('.texto.txt', 'w').close()
    write_txt_file()
    read_txt_file()


if __name__ == "__main__":
    run()
