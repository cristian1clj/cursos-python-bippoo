import csv
from os import stat
from typing import Dict, List, Tuple
from files import FILES

file_empty = lambda file: stat(file).st_size == 0

DATA_SCHEMA: Dict[str, Tuple[str]] = {
    'Prd-Spl-Cst':('id', 'name', 'ad_pr'),
    'E-S':('date', 'nit', 'id', 'amount', 'price'),
    'Inv':('id', 'amount')
}


class InformationManagement:
    def __init__(self, file: str, data1: str, data2: str, data3: str):
        self.file = file
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3

    def add(self):
        information: List[Dict[str, str]]
        
        if not file_empty(self.file):
            with open(self.file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
                information = [row for row in reader]

            information.append(dict(zip(DATA_SCHEMA["Prd-Spl-Cst"], [self.data1, self.data2, self.data3])))
            information.sort(key=lambda element: int(element['id']))

            with open(self.file, "w", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
                writer.writerows(information)
        
        else:
            information = [dict(zip(DATA_SCHEMA["Prd-Spl-Cst"], [self.data1, self.data2, self.data3]))]
            
            with open(self.file, "w", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
                writer.writerows(information)

    def modify(self):
        information: List[Dict[str, str]]

        with open(self.file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
            information = [row for row in reader]

        information = [dict(zip(DATA_SCHEMA["Prd-Spl-Cst"], [self.data1, self.data2, self.data3])) if self.data1 == element['id'] else element for element in information]

        with open(self.file, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
            writer.writerows(information)

    def delete(self):
        information: List[Dict[str, str]]

        with open(self.file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
            information = [row for row in reader]

        information = [element for element in information if self.data1 != element['id']]

        with open(self.file, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
            writer.writerows(information)

    def search(self) -> Dict[str, str]:
        information: List[Dict[str, str]]

        with open(self.file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
            information = [row for row in reader]

        for value in information:
            if self.data1 == value['id']:
                return value

    def show_all(self) -> List[Dict[str, str]]:
        information: List[Dict[str]]

        with open(self.file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Prd-Spl-Cst"])
            information = [row for row in reader]
            
        return information


class InventaryManagement:
    def __init__(self, data1: str, data2: int):
        self.file = FILES["INVENTORY"]
        self.data1 = data1
        self.data2 = str(data2)

    def add(self):
        if not file_empty(self.file):
            information: List[Dict[str, str]]

            with open(self.file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Inv"])
                information = [row for row in reader]

            information.append(dict(zip(DATA_SCHEMA["Inv"], [self.data1, self.data2])))
            information.sort(key=lambda element: int(element['id']))

            with open(self.file, "w", encoding="utf-8") as f:
                writer = csv.DictWriter(f, DATA_SCHEMA["Inv"])
                writer.writerows(information)
        
        else:
            information = [dict(zip(DATA_SCHEMA["Inv"], [self.data1, self.data2]))]
            
            with open(self.file, "w", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=DATA_SCHEMA["Inv"])
                writer.writerows(information)

    def modify(self):
        information: List[Dict[str, str]]

        with open(self.file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Inv"])
            information = [row for row in reader]

        information = [dict(zip(DATA_SCHEMA["Inv"], [self.data1, self.data2])) if self.data1 == element['id'] else element for element in information]

        with open(self.file, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=DATA_SCHEMA["Inv"])
            writer.writerows(information)

    def delete(self):
        information: List[Dict[str, str]]

        with open(self.file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Inv"])
            information = [row for row in reader]

        information = [element for element in information if self.data1 != element['id']]

        with open(self.file, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=DATA_SCHEMA["Inv"])
            writer.writerows(information)

    def search(self) -> Dict[str, str]:
        information: List[Dict[str, str]]

        with open(self.file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Inv"])
            information = [row for row in reader]

        for value in information:
            if self.data1 == value['id']:
                return value
