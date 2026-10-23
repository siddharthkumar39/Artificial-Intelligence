#create an account with 2 attributes -balance and account no.
#create methods fot debit,creditand printing the balance
class Account:
    def __init__(self,bal,acc):#constructor
        self.balance=bal
        self.accountNo=acc
        #debit method
    def debit(self,amount):#1
        self.balance -= amount
        print("rs", amount,"was debited")
        print("total balance=",self.get_balance())#4 
        #credit method
    def credit(self,amount):#2
        self.balance += amount
        print("rs.",amount,"was credited")
        print("total balance =",self.get_balance())
    def get_balance(self):#3
        return self.balance
acc1=Account(10000,12345)#account
acc1.debit(1000)
acc1.credit(5000)