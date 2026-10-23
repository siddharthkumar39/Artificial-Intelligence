class Account:
    def __init__(self,acc_num,acc_pass):
        self.acc_no=acc_num
        self.__acc_Pass=acc_pass
        #private krne ka syntax __(uper 2 underscore h self. k bad)

    def reset_pass(self):
        print(self.__acc_Pass)

acc1=Account("12345","abcdef")
print(acc1.acc_no)
print(acc1.reset_pass())#func. call
#this will be print becz this fn is inside
#class
print(acc1.__acc_pass)#error becz this data
#is private that it can be used only 
#inside class
