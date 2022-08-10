import csv
from datetime import datetime
from typing import Dict, List
from models.data import InformationManagement, InventaryManagement, DATA_SCHEMA
from files import FILES


class InformationMovement:
    def __init__(self, file: str, identifier: str, data1: str, data2: str, data3: str):
        self.file = file
        self.identifier = identifier
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3

    def add(self):
        d = datetime.now()
        obj: object = InformationManagement(FILES["PRODUCTS"], self.data2, None, None)
        data4: Dict[str, str] = obj.search()

        inventary: List[Dict[str]]
        with open(FILES["INVENTORY"], "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=DATA_SCHEMA["Inv"])
            inventary = [row for row in reader]
        
        for values in inventary:
            if self.data2 == values['id']:
                if self.identifier == "ENTRY":
                    inv: object = InventaryManagement(self.data2, int(values['amount']) + int(self.data3))
                    inv.modify()
                
                elif self.identifier == "SALE":
                    inv: object = InventaryManagement(self.data2, int(values['amount']) - int(self.data3))
                    inv.modify()

        information: Dict[str, str] = dict(zip(DATA_SCHEMA["E-S"], [d.strftime('%d-%m-%Y__%H:%M:%S'), self.data1, self.data2, self.data3, data4['ad_pr']]))
        with open(self.file, "a", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=DATA_SCHEMA["E-S"])
                writer.writerow(information)
