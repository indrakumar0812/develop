n = int(input("enter the value of n:"))

for i in range (2,n+1):
    while (n%i==0):
        print(n, "is not a prime number")
        break

    else:
        print(n, "is a prime number")
        break

    
