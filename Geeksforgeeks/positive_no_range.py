#positive_numbers_range

'''list=[]

for i in range (-4,5+1):
    if i>=0:
        list.append(i)
print(list)'''

#negative_numbers_range

'''list=[]

for i in range (-4,5+1):
    if i<0:
        list.append(i)
print(list)'''

#count_negative_positive_numbers

list=[]
count_positive=0
count_negative=0

for i in range (-4,5+1):
    if i>=0:
        count_positive+=1
    else:
        count_negative+=1
        
print("no. of positive numbers are:", count_positive)
print("no. of negative numbers are:", count_negative)
