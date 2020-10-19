nos = int(input("enter the number:"))
a=[]
def totalSum():
    sum = 0
    for i in range (1,nos+1):
        sum=sum+i
    return sum

def listData(n):
    for i in range (1,nos+1):
     list1=n//i
     a.append(list1)
  
   
b = totalSum()
listData(b)
print(a)

    
