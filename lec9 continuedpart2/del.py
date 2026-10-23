class Student:
    def __init__(self,name):
        self.name=name

s1= Student("shradha")
print(s1.name)
del s1.name 
# del ye s1 object ko delete kr dega.
print(s1.name)