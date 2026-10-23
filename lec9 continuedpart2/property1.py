class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3) + "%"
        # agar ham  physics ka marks change krne ke bad directly above se claculate same 98 percent wala
        #  hi wapas print ho jyga islie alag se function bnaye  niche 


    def calcpercentage(self):
        self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

stu1=Student(98,99,97)
print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
stu1.calcpercentage()
print(stu1.percentage)
