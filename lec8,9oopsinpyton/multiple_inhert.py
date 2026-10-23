class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varc="welcome to class c"

c1=C()

print(c1.varA)
#islie varA and varB ko print krwa pa rhe due to multiple inheritance
print(c1.varB)
print(c1.varC)
 
