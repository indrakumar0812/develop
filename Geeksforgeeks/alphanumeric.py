import re

'''a = "123AM256CD"

print(re.sub(r'\d{3}','',a))
print(re.sub(r'[A-Za-z]','',a))'''


'''a = "123AM256CD"

num=a[0:2+1]+a[5:7+1]

print(num)

char = a[3:4+1]+a[8:9+1]

print(char)'''

a = "123AM256CD"

num_split =re.split(r'\d{3}',a)
print(''.join(num_split))

char_split = re.split(r'[a-zA-Z]',a)
print(''.join(char_split))
