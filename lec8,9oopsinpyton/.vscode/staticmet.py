class Decorators:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def hello():
        print("hello")
s1=Decorators("siddharth")
s1.hello()