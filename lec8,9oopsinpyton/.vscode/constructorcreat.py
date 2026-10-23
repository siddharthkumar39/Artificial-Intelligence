class Student:
    college_name="st.thoms college"
    def __init__(self,name,marks):# 2.created a constructor in object
        self.name=name
        self.marks=marks
        print("adding new student in database")

s1=Student("Karan",97)#1.created an object
print(s1.name,s1.marks)
s2=Student("Arajun",98)#again constructor will be called
print(s2.name,s2.marks)

print(s2.college_name)

