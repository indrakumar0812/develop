'''list = [16, 17, 4, 3, 5, 2]

list1=[]

for i in range(len(list)):
    count = 0
    for j in (list[i+1:]):
        if list[i]>=j:
            count+=1
    if count==len(list)-(i+1) or list[i]==list[-1]:
        print(list[i],end=' ')'''

'''N = 4
A= [1,2,3,2]
x = 1
y = 2

index_x = A.index(x,0,len(A))
list1=[]
count=0
for i in range(index_x+1,N):
    count += 1
    if A[i]==y:
        list1.append(count)

print(min(list1))'''

a =[3,1,3,3,2]

c=set(a)

#print(c)

b = len(a)//2

#print(b)

for i in c:
    if a.count(i)>b:
        print(i)
