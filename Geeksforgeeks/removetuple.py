'''list = [('','','8'), (), ('0', '00', '000'),('birbal', '', '45'),
        (''),(),('',''),()]

print("before removing:",list)
for i in list:
    if len(i)<1:
        list.remove(i)
        
print("after removing:",list)'''

def Remove(tuples): 
    tuples = [t for t in tuples if t] 
    return tuples 
  
# Driver Code 
tuples = [('','','8'), (), ('0', '00', '000'),('birbal', '', '45'), (''), (),  ('',''),()] 
print(Remove(tuples)) 
