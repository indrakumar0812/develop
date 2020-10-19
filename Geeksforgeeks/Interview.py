'''a ="abcdyhfgy"
b="a(b)[{}[]cd]yhfgy{{"

var=['(',')','{','}','[',']']

d= dict()

for i in var:
        d[i]=b.count(i)
print(d)

for j in range(len(var)-1,2):
    if d[var[j]]==d[var[j+1]]:
        print("string is valid")
        break
else:
     print("string is not valid")'''

list=['abd','3','df','4','6']

length=len(list)

count_num=0
count_char=0
for i in list:
    if i.isdigit()==True:
        count_num+=1
    else:
        count_char+=1

print("No.of nums are:",count_num)
print("No.of characters are:",count_char)

