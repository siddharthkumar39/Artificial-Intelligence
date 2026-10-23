class Car:
    @staticmethod
    def start():
        print("car started.")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyota(Car):#inheritance
    def __init__(self,brand):
        self.name=brand

class Fortuner(Toyota):
    def __init__(self,type):
        self.type=type

car1=Fortuner("diesel")
car1.start()
#mutilevel inheritance