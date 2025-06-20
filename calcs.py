from random import randint
from typing import List
from objects import Product
import cfg
from employees import get_candidates
from imgsinit import *



def profit(products: List[Product], adjustment) -> int: #Change in budget

        decline = 0
            
        for el in products:
            tmp = el.info()

            decline += randint(tmp["total income"] - randint(100, 1000),
                                tmp["total income"] + randint(100, 1000)) * tmp["amount"]
                
        
            decline -= randint(tmp["total price"] - randint(100, 400),
                                tmp["total price"] + randint(1000, 1200)) * tmp["amount"]
                
        return decline + int(decline * (adjustment-1))

def reset():
    cfg.INVALID_NAME = False
    cfg.EDITOR = False
    cfg.CNAME_TOGGLE = False
    cfg.CAN_SELECT = False
    cfg.PNAME_TOGGLE = False
    cfg.INSUFFICIENT_EMPLOYEES = True
    cfg.STAFF_MANAGING = False
    cfg.UPGRADE_OFFICE = False
    cfg.DEVELOP_BRANCHES = False
    cfg.HIRING_ERROR = False
    cfg.FRAUD_DETECTED = False
    cfg.BANKRUPCY = False
    cfg.WATCH_PRODUCTS = False
    
    cfg.player_name = ""
    cfg.company_name = ""
    cfg.income = 0
    cfg.staff =  []
    cfg.staff_limit = 1
    cfg.candidates = get_candidates()
    cfg.adjustment = 1
    cfg.branches = 0

    cfg.buffer = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    cfg.pBuffer = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    cfg.office_params = {500000: 5,
                  1200000: 10,
                  2880000: 24}

    cfg.curr_price = 500000
    cfg.products = []
    cfg.curr_product = {0: "-", 1: "-", 2: "-", 3: "-", 4: "-"}

    cfg.namm = ["Монитор", "Мышь", "Коврик", "Клавиатура", "Веб-камера"]

    cfg.staff_ind = 0
    cfg.tab_ind = 0
    cfg.prod_ind = 0
    cfg.currBtns = []
    cfg.info = {}

    cfg.rent = 30000
    cfg.expenses = 0

    cfg.tabnames = ["monitors", "mice", "mousepads", "keyboards", "webcameras"]
    cfg.cBg = 0
    cfg.dummies = [monitorDummy, mouseDummy, mousepadDummy, keyboardDummy, wcamDummy]
    cfg.budget = 1030000
    cfg.number_of_employees= len(cfg.staff) + 1