
'''a = [0, 1, 2, 3, 4, 5]

for i in range(len(a)):
    if a.index(i)%2!=0:
        temp=a[i]
        a[i]=a[i-1]
        a[i-1]=temp
print(a)'''

'''a = [11, 33, 50]
b =''

for i in a:
    b=b+str(i)

print(b)'''

a = [0,1,2,3,4,5]

for i in range(len(a)):
    if i%2!=0:
        temp=a[i]
        a[i]=a[i-1]
        a[i-1]=temp
print(a)

