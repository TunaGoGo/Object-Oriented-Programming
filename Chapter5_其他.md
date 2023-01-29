# 1. 面向对象三大特性

* 封装
  * 将属性和方法书写在类的里面的操作即为封装
  * 封装可以为属性和方法添加私有权限
* 继承
  * 子类默认继承父类的所有属性和方法
  * 子类可以重写父类属性和方法
* 多态
  * 传入不同的对象，产生不同的效果

# 2. 多态
## 2.1 了解多态
多态指的是一类事物有多重形态，（一个抽象类的多个子类，因而多态的概念依赖于继承）
  * 定义：多态是一种使用对象的方法，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行关系
  * 好处： 灵活调用，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变化
  * 实现步骤：
    * 定义父类，并提供公共方法
    * 定义子类，并重写父类方法
    * 传递子类对象给调用者，可以看到不同子类执行效果不同

  ## 2.2 实例
```python
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
``` 
# 3. 类属性和实例属性
## 3.1 类属性
### 3.1.1 设置和访问类属性
* 类属性是类对象所拥有的属性，它被该类的所有实例对象所拥有
* 类属性可以使用类对象或实例对象访问

```python
class Dog(object):
  tooth = 10

111 = Dog()

print(Dog.tooth)
print(111.tooth)
```

  类属性的有点
  * 记录的某项数据 始终保持一致，则定义类属性
  * 实例属性要求每个对象为其单独开辟一份内存空间来记录数据，而类属性为全类所共有，仅占用一份内存，更加节省空间

### 3.1.2 修改类属性
类属性只能通过类对象修改，不能通过实例对象修改，如果通过实例对象修改类属性，表示的是创建了一个实例属性

```python
class Dog(object):
  tooth = 10

111 = Dog()

Dog.tooth = 12 
print(Dog.tooth)
print(111.tooth)
```

# 4. 类方法和静态方法
## 4.1 类方法
### 4.1.1 类方法特点
* 需要用装饰器`@classmethod`来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以`cls`作为第一个参数

### 4.1.2 类方法使用场景
* 当方法中需要使用类对象（如果访问私有类属性等）时，定义类方法
* 类方法一般和类属性配合使用

```python
class Dog(object):
  __tooth = 10

  @classmethod
  def get_tooth(cls):
    return cls.__tooth
```

## 4.2 静态方法
### 4.2.1 静态方法特点
* 需要通过装饰器`@staticmethod`来进行装饰，静态方法既不需要传递类对象也不需要传递实例对象(形参没有self/cls)
* 静态方法也能够通过实例对象和类对象访问
  
### 4.2.2 静态方法使用场景
* 当方法中既不需要使用实例对象(如实例对象，实例属性)，也不需要使用类对象(如类属性，类方法，创建实例等)时，定义静态方法
* 取消不需要的参数传递，又利于减少不必要的内存占用和性能消耗

```python
class Dog(object):
  @staticmethod
  def info_print():
    print("-------")
```