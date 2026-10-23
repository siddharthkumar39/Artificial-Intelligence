def check_for_word():
 word="learning"
 with open("practice.txt","r")as f:
    data=f.read()
    if(word in data):
        print("found")
    else:
        print("not found")


def check_for_line():
   word="learning"
   data=True
   #true islie lie kuki agr empty rha to loop run nhi krega
   line_no=1
   with open("practice.txt","r") as f:
      while data:
         #blank space menas true
         data=f.readline()
         if(word in data):
            print(line_no)
            return
            line_no+=1
        
check_for_line()


         #in check krega ki data line me hai ki nhi 


         

   
