listgpa = [3,2.7,2.5,4]
def bonus (gpa):
    nominal = 500000
    bonus = gpa*nominal
    return bonus
for gpa in listgpa :
    if gpa > 3 :
        print("anda mendapatkan bonus sebesar :",bonus(gpa))
    else:
        print("belum saatnya")
