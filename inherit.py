class A:
    def meth(self):
        print("Class a")

    def meth1(self):
        print("a meth1")

class B(A):
    def meth(self):
        print("class B")

k = B()
k.meth()
k.meth1()
print(type(k))