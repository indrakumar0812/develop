s1={'a','e','i','o','u','A','E','I','O','U'}
str="geeksforgeeks"

listconv = list(str)
count =0
for i in listconv:
    if i in s1:
        count+=1

print(count)
