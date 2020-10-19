list = ['p', 'q']
n =5
#Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
list1=[]

for i in range (1,n+1):
    for j in list:
        list1.append(j+str(i))

print(list1)

