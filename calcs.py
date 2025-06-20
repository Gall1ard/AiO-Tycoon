from random import randint
from typing import List
from objects import Product


def profit(products: List[Product], adjustment) -> int: #Change in budget

        decline = 0
            
        for el in products:
            tmp = el.info()

            decline += randint(tmp["total income"] - randint(100, 1000),
                                tmp["total income"] + randint(100, 1000)) * tmp["amount"]
                
        
            decline -= randint(tmp["total price"] - randint(100, 400),
                                tmp["total price"] + randint(1000, 1200)) * tmp["amount"]
                
        return decline + int(decline * (adjustment-1))