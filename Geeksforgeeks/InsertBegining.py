'''list = [1,2,3,4]
string1 ="emp"
#Exp = ['emp1', 'emp2', 'emp3', 'emp4']
string2=""

a= [string1+str(i) for i in [1,2,3,4]]

print(a)'''

lists = [[1,2,3],[4,5,6],[10,11,12],[7,8,9]]

n= (max(lists,key=sum))

print(n)
#Expected Output: [10, 11, 12]
'''list1=[]
for i in lists:
    sum = 0
    for j in i:
        sum+=j
    list1.append(sum)
print(max(list1))'''




