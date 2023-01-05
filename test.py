class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

class House():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []
    
    def add_furniture(self, item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，不能容纳')

    def __str__(self):
        return f'房子位于{self.address},占地面积{self.area}, 剩余面积{self.free_area}, 现有家具{self.furniture}'

bed = Furniture('床', 10)
sofa = Furniture('沙发', 50)

home1 = House('北京',100)
home1.add_furniture(bed)
home1.add_furniture(sofa)

basketball = Furniture('篮球场',1000)
home1.add_furniture(basketball)

print(home1)