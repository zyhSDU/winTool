from helper.ObjectHelper import print_object


class ClassA(object):
    def __init__(self, str1: str, str2: str):
        self.str1 = str1
        self.str2 = str2


class ClassB(ClassA):
    def __init__(self, str1: str, str2: str):
        super(ClassB, self).__init__(str1, str2)


class ClassC(ClassA):
    pass


a = ClassA("a1", "a2")
b = ClassB("b1", "b2")
c = ClassC("c1", "c2")

print_object(a)
print_object(b)
print_object(c)
