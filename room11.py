# Class_Objcet
class Furniture:
    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width

    def action(self):
        print("Furniture have no actions")


sofa = Furniture('sofa', 11, 20)
chair = Furniture('chair', 5, 9)
print(sofa.__dict__)
chair.action()


# Inheritance


class Table(Furniture):

    def __init__(self, name, height, width):  # not necessary here as table inherits all of the functions
        super.__init__(name, height, width)


Dinning_table = Furniture('dt', 11, 45)
print(Dinning_table.__dict__)
Dinning_table.action()


# encapsulateion


class EasyEducation:
    def __init__(self):
        self.__course = "Python "  # course attribute is encapsulated here
        self.__code = 1122  # same here


ob = EasyEducation()
print(ob._EasyEducation__course)  # course attribute accessed here by name mangling




