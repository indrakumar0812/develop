def outer():
    print("inside outer function")

    def inner():
        print("inside inner function")
    return inner

m = outer()
print(m)
m()
