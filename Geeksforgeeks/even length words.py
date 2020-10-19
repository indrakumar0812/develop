s ="i am muskan"

def printeven(s):
    
    s1 = s.split(' ')
    for i in s1:
        if len(i)%2==0:
           print(i)
           
            
printeven(s)
