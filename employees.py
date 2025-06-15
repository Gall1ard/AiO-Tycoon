from objects import Employee


f = open("sources/txts/staff.txt", "r")

def get_candidates():
    staff = []
    for line in f:
        temp = line.split("_")
        staff.append(Employee(temp[0],
                            int(temp[1]),
                            float(temp[2]),
                            int(temp[3][:-1])).info())
    return staff
    

