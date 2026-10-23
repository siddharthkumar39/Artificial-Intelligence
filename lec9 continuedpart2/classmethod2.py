class Person:
    name= "annonymous"
    @classmethod
    # yah classmethod decorartor hai
    def changename(cls,name):
    #cls=classs hai kind or keyword or shortcut bol sakte hai
        cls.name=name
p1=Person()
p1.changename("Rahul kumar")
print(p1.name)
print(Person.name)
