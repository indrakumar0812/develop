a = ["can", "you", "can", "a", "can" "?"]

word = input("enter the word:")
n = int(input("enter the no. of occurance:"))
count = 0

for i in range(0,len(a)):
    if (a[i] == word):
        count+=1
        if (count==n):
            a.pop(i)
            break

print(a)
