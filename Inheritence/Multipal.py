# Multipal Inheritance

class A:
    def readA(self):
        print("Hello A")

class B:
    def readB(self,name):
        print("Heelo B",name)

class C(A,B):
    def readC(self):
        print("Hello C")



obj=C()
obj.readA()
obj.readB("Akshay")
obj.readC()
