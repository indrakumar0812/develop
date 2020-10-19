tuples = [('','','8'), (), ('0', '00', '000'),('birbal', '', '45'), (''), (),  ('',''),()]

a=[]
'''
for i in tuples:
    if len(i)>=1:
        a.append(i)

print(a)'''

for i in tuples:
    if i is True:
        tuples.append(i)
print(tuples)
