class Person:
    __name="siddharth"
    #ab yh ak private class bn gya h so we cannot print outside class
    def __hello(self):
        print("hello person")
#isko bahr call nhi kr sktw kuki __private  h ye wala method
    def welcome(self):
        self.__hello()
p1=Person()
#print(p1.__name)
#print(p1.__hello())
#ye uper dono m error ayga kuki private h
print(p1.welcome())
# yha par welcome hello ko call islie kr pa rha h kuki hello internal function h or private method ya 
# object  ko internal function hi call kr skta h.

