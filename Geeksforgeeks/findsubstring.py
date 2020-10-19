s1 = 'geeks'
s2= 'geeks for geeks'

s3= s2.split(' ')
print(s3)

for i in range (len(s3)):
    if s3[i] == s1:
        print('string found at', i)


