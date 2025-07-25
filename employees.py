from objects import Employee
'''
u = open("sources/txts/staff.txt", "w")

lst = ["Оцеллина Вильсон_74_2.9_4_40000",
       "Медея Леконт_24_1.7_2_23000",
       "Клейт Мейсон_65_1.4_16_10000",
       "Отан Меладзе_38_3.8_2_90000",
       "Тея Шарль_72_7.2_11_12200",
       "Тессала Галбрейт_79_4.4_58_10000",
       "Бейба Милн_20_3.5_1_13000",
       "Феба Кендал_86_7.4_33_24400",
       "Адея Жарре_43_7.3_4_26600",
       "Варро Гудэнаф_58_3.3_13_56450",
       "Секстий Бутман_21_5.7_3_22200",
       "Боромир Аносов_83_2.0_4_17900",
       "Твердимир Нерознак_64_9.5_45_34900",
       "Эгнатий Невраль_45_7.8_10_65000",
       "Тейран Ромер_34_2.4_13_45000",
       "Иван Митусов_71_9.4_54_69000"]


for el in lst:
    u.write(f"{el}\n")
'''
f = open("sources/txts/staff.txt", "r")

def get_candidates():
    staff = []
    for line in f:
        temp = line.split("_")
        staff.append(Employee(temp[0],
                            int(temp[1]),
                            float(temp[2]),
                            int(temp[3]),
                            int(temp[4][:-1])).info())
    return staff
    

