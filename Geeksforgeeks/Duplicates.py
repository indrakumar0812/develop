list =[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

list1=[]
list2 =[]
for i in list:
    if list.count(i)>1:
        if i not in list1:
            list1.append(i)
print(list1)

'''for j in list1:
    if j not in list2:
        list2.append(j)
print(list2)'''
