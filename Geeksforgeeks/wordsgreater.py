str = "hello geeks for geeks is computer science portal"

k=4
a=[]

str_split = str.split(" ")

for i in str_split:
    if len(i)> k:
        a.append(i)

print(a)
        
