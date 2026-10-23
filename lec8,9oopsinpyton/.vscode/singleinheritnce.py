class Car:
    @staticmethod
    def start():
        print("car started.")

    @staticmethod
    def stop():
        print("car stopped.")

class Toyota(Car):
    def __init__(self,name):
        self.name=name

car1=Toyota("fortuner")
car2=Toyota("Ertica")

print(car1.start())
#above class se inherit hua islie error mhi aya
