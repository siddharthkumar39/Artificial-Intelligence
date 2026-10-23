class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"
    #isko use krke directly percentage return kar skte hai yahi iska fyda hai

stu1=Student(98,99,97)
print(stu1.percentage)

stu1.phy=86
print(stu1.phy)
print(stu1.percentage)
