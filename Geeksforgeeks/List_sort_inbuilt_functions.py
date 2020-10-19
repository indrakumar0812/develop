

n=int(input("enter the no.of values:"))

list= [int(input("enter the numbers:")) for x in range (n)]


for i in range (len(list)-1): #-1 coz at the end only last value will be left so there's nothing to compare it with
    m_min = min(list[i:]) # need to search for the min value after the first element which is considered to be as min value(after sorting the list also)
    m_ind = list.index(m_min,i)# i is to replace the duplicate value, it will tell the start position and return the index of the first occurance of the value

    if list[i]!=list[m_ind]:
        list[i],list[m_ind]=list[m_ind],list[i] #swapping with the first element

print(list)

#list = [25,2,5,1,2,17,8,10]

#====this code is same as list comprehension=====
#list=[]
#for x in range (n):
#    a=int(input("enter the numbers:"))
#    list.append(a)

#====end====================================

