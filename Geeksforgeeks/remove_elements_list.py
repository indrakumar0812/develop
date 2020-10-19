'''a = [12,15,3,10,4]
b =[]
tot_num = int(input("enter the total no of elements to be removed from list:"))

for num in range (1,tot_num+1):
    c = int(input("enter the nos to be removed from list:"))
    b.append(c)
 
for i in b:
    a.pop(a.index(i))

print(a)'''


a = [12,15,3,10,4]
b = [12,3]

for i in b:
    a.remove(i)

print(a)
