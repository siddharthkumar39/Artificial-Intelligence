#to create student class that takes names of 3 subject as arguments in constructor
#then create a method to print the average
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your average marks=",sum/3)
        
s1=Student("virat kohli",[98,99,100])
s1.get_average()
s1.name="chiku"#we can directly change value of attribute
s1.get_average()