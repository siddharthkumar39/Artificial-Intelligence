class Person:
    name="Aditya"

    def change_name(self,name):
        #self.name=name (not valid)
        #or mehthod-2 we can use
        #self.__class__.name="Rahul"
        Person.name=name
#agar self.name use krnge to y object k ander ye siddharth create kar dega
#or class ka name aditya hi rhega pr ham chhte h ki class ki name chnage karke siddharth kare
#islie person .name lnge
p1=Person()
p1.change_name("siddharth")
print(p1.name)
print(Person.name)

