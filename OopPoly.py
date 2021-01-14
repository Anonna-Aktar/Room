
#DuckTyping
class pyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")


class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)


# operator overloading
class students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = students(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = students(2, 3)
s2 = students(3,4)
s3 = s1 + s2
print(s3.m2)
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")



# Method overloading

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s= 0

        if a !=None and b != None and c != None:
            s = a+b+c
        elif None and b != None:
            s = a+b
        else:
            s = a
        return s


std1 = Student(10, 20)
print(std1.sum(1,2,3))
print(std1.__dict__)


# method overriding


class A:
    def show(self):
        print("i m in class A")


class B(A):
    pass


a = A()
b = B()
b.show()
