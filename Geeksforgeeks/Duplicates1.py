a ="India is great".lower()

a_list=list(a)
#print(a_list)

#a_rep= a.replace(" ","")

b = "in"
c_list=list(b)
#print(c_list)


list=[]

for i in a_list:
    for j in c_list:
        if j==i:
            a_list.remove(i)
print(a_list)

for i in a_list:
    print(''.join(i),end ="")








