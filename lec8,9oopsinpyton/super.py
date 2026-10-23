#super method -calling parents method
#in derived
class Car:
    def __init__(self,type):
        self.type=type
        #above constructor bnye h
    @staticmethod
    def start():
        print("car started.")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyota(Car):#inheritance
    def __init__(self,name,type):
        super().__init__(type)
        #called parent type insdie this from first parent class using  constructor method=super method 
        self.name=name
        super().start()
        # super class ka start method call ho jyga

car1=Toyota("fortuner","electric")
print(car1.type)
