str1='geeks'
str_set1=set(str1)
str2='geeksonly'
str_set2=set(str2)
count=0

for i in str_set1:
    for j in str_set2:
        if i==j:
            count+=1
print(count)
