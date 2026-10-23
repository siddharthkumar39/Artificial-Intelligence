# last page me is code ko ache se explain kia h .
class Complex:
    def __init__(self,real,img):
        # yah constructor hai- object ko ready krta hai
        self.real= real #realpart
        self.img=img     #imginary part
        

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def add(self,num2): #created function to add
        #self jo hai wo object 1 hai ya object 1 ko represent karta hai
        #num2 object 2 ko 
        newReal=self.real+num2.real #real part ko add krega
        newImg=self.img+num2.img    #img part ko call krega
        return Complex(newReal, newImg) # complex class ka naya obect bana ke return kar rha hai

    def __sub__(self,num2):
        # yaha subtraction function use kie hai to bina ye wla function calll kie ham yah operation - sigh use krek perform kr paynge 
        newReal=self.real-num2.real
        newImg= self.img-num2.img
        return  Complex(newReal, newImg)

num1= Complex(1, 3)
num1.showNumber()
#function call


num2= Complex(4, 6)
num2.showNumber()
#function call

num3=num1.add(num2)  #ye add wala objct ka fuction call kia
num3.showNumber()      #ye show no wala bject ka function call kia


num3=num1 - num2      # yha hame sub function ko call nhi krna pda kuki using dunder function hamne - operator ka overloading krwya jisse complex no ka minus krwa paye
num3.showNumber()