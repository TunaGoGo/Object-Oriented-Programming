class Dog(object): #父类提供统一方法，哪怕是空方法直接pass
    def work(self):
        print("go!")

class ArmyDog(Dog): #继承Dog类
    def work(self): #子类重写父类同名方法
        print("gogo!")

class DrugDog(Dog):
    def work(self):
        print("find drug!")

class Person(object):
    def work_with_dog(self,dog):
        dog.work()
        
ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)