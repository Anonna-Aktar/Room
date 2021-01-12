
class Furniture:
    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width

    def action(self):
        print("No actions")


sofa = Furniture('sofa', 11, 20)
chair = Furniture('chair', 5, 9)
print(sofa.__dict__)
chair.action()


class Table(Furniture):
    pass

    def __init__(self, name, height, width):  # not necessary here as table inherits all of the functions
        super.__init__(name, height, width)


Dinning_table = Furniture('Dinning table', 11, 30)
print(Dinning_table.__dict__)
Dinning_table.action()
Reading_table = Furniture("Reading table", 5,15)
Reading_table.action()
print(Reading_table.__dict__)


class Gadgets:
    def __init__(self, brand_name, OS):
        self.brand_name = brand_name
        self.OS = OS

    def gadget_details(self):
        print(self.brand_name,self.OS)


Laptop = Gadgets("HP", "Windows")
Mobile = Gadgets("Apple", "IOS")
print(Laptop.__dict__)
print(Mobile.__dict__)
Digital_camera = Gadgets("Sony", "None")
Digital_camera.model_number = "Sony_1A34"
print(Digital_camera.__dict__)


class electronics:
    def __init__(self, name, brand, model_number):
        self.name = name
        self.brand = brand
        self.model_number = model_number


Electric_fan = electronics("Electric fan"," Vision", "1A")
Electric_bulb = electronics("Electric bulb", "Vision", "1CC")








