list = [25,2,5,1,2,17,8,10]

for i in range (len(list)-1):
    m_min=i

    for j in range (i+1,len(list)):
        if list[j]<list[m_min]:
            m_min=j

    if list[i]!=list[m_min]:
        list[i],list[m_min]=list[m_min],list[i]

print(list)
        
