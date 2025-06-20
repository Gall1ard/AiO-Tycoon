from imgsinit import monitorDummy, wcamDummy, mouseDummy,\
      computerDummy, keyboardDummy, mousepadDummy

from employees import get_candidates

GAME_SCENE = 0 #Start scene is 0. If it's not then it's for testing purposes
'''
0 - Main menu screen
1 - Login/Register screen (pops up if the player wasn't logged in)
2 - Main game scene
3 - Device constructor scene
-1 - คุณห่วยในการเล่นเกมนี้ ๕๕๕๕๕+
'''

INVALID_NAME = False
EDITOR = False
CNAME_TOGGLE = False
CAN_SELECT = False
PNAME_TOGGLE = False
INSUFFICIENT_EMPLOYEES = True
STAFF_MANAGING = False
UPGRADE_OFFICE = False
DEVELOP_BRANCHES = False
HIRING_ERROR = False
FRAUD_DETECTED = False
BANKRUPCY = False
WATCH_PRODUCTS = False

player_name = ""
company_name = ""
income = 0
staff =  []
staff_limit = 1
candidates = get_candidates()
adjustment = 1
branches = 0

buffer = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

pBuffer = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

office_params = {500000: 5,
                1200000: 10,
                2880000: 24}

curr_price = 500000

products = []
curr_product = {0: "-", 1: "-", 2: "-", 3: "-", 4: "-"}

namm = ["Монитор", "Мышь", "Коврик", "Клавиатура", "Веб-камера"]

staff_ind = 0
tab_ind = 0
prod_ind = 0
currBtns = []
info = {}

rent = 30000
expenses = 0

tabnames = ["monitors", "mice", "mousepads", "keyboards", "webcameras"]
cBg = 0


dummies = [monitorDummy, mouseDummy, mousepadDummy, keyboardDummy, wcamDummy]

budget: float = 1030000
number_of_employees: int = len(staff) + 1