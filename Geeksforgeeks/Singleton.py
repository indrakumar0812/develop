def singleton(cls):
    print("hi")
    print("address of A", cls)
    instances = {}
    def inner():
        print("control entered into inner")
        print(instances)
        if cls not in instances:
            print("hello")
            instances[cls]=cls
        return instances[cls]
    return inner

@singleton
class A:
    pass

obj = A()
obj1 = A()
Obj2 = A()

print(obj)
print(obj1)
print(obj2)
