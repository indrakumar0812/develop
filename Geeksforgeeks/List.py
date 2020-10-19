list = [1,2,3]
a=[]
def total():
    sum = 0
    for i in list:
        sum=sum+i
    return sum

def actual(n):
    for i in list:
     list1=n//i
     a.append(list1)
   
b = total()
actual(b)
print(a)
    
    
    
    
