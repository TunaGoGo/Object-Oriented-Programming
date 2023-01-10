# 1. 继承

## 1.1 继承的定义

* 拓展1：经典类和新式类

```python
class 类名:
    code
```

* 拓展2：新式类

```python
class 类名(object):
    code
```

Python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法，如下:
```python
#父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

class B(A):
    pass

result = B()
result.info_print()
```

# 2. 单继承

    故事主线：一个煎饼果子老师傅，在煎饼果子界摸爬滚打多年，研发了一套精湛的煎饼果子技术。师父要把这套技术传授给他的唯一的徒弟

分析：徒弟是不是要继承师父的所有技术？

```python
#师父类
class Master(object):
    def __init__(self):
        self.kongfu = ['煎饼果子酱料']

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#徒弟类
class Prentice(Master):
    pass

daqiu = Prentice()
daqiu.make_cake()
```

定义：

    一个子类只用有一个父类

# 3. 多继承
定义：
    多继承就是指一个子类可以拥有多个父类

```python
#师父类
class Master(object):
    def __init__(self):
        self.kongfu = ['煎饼果子酱料']

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#学校类
class School(object):
    def __init__(self):
        self.kongfu = ['学员班煎饼果子酱料']
    
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#徒弟类
class Prentice(School,Master):
    pass

daqiu = Prentice()
daqiu.make_cake()
```

    注意：当一个类有多个父类时，默认使用第一个父类的属性名和方法。

# 4. 子类重写父类同名方法和属性

    如果子类和父类有同名属性和方法，子类创建对象调用属性和方法时，调用的是子类中的同名属性和方法
```python
#师父类
class Master(object):
    def __init__(self):
        self.kongfu = ['煎饼果子酱料']

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#学校类
class School(object):
    def __init__(self):
        self.kongfu = ['学员班煎饼果子酱料']
    
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#徒弟类
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = ['自创班煎饼果子酱料']
    
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()
```

# `__mro__`
    快速查询类继承的父类的方法

```python
print(类名.__mro__)
```

# 5. 子类如何调用父类的同名方法和属性

```python
#师父类
class Master(object):
    def __init__(self):
        self.kongfu = ['煎饼果子酱料']

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#学校类
class School(object):
    def __init__(self):
        self.kongfu = ['学员班煎饼果子酱料']
    
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#徒弟类
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = ['自创班煎饼果子酱料']
    
    def make_cake(self):
        # 如果先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 调用父类方法，但是为保证调用到的也是父类的属性，必须在调用方法前调用父类的初始化
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
    
daqiu = Prentice()

daqiu.make_cake()
daqiu.make_master_cake()
daqiu.make_school_cake
```

# 5. 多层继承

# 6. super()调用父类方法

```python
def make_old_cake(self):
    # 方法一： 如果定义的类名修改，这里也要修改，麻烦，代码量庞大
    School.__init__(self)
    School.make_cake(self)
    Master.__init__(self)
    Master.make_cake(self)
    # 方法二： 
    ## 带参数 super(当前类名，self).函数()
    super(Prentice, self).__init__()
    super(Prentice, self).make_cake()
    ## 不带参数 super()
    super().__init__()
    super().make_cake()
    
```
    注意：使用super()可以自动查找父类。调用顺序遵循`__mro__`类属性的顺序。比较适合单类继承使用。

# 7. 私有权限
## 7.1 定义私有属性和方法
在python中，可以为实例属性和方法设置私有属性，即设置某个实例属性或实例方法不继承给子类。

设置私有权限的方法：在属性名和方法名前面加上两个下划线__

```python
#师父类
class Master(object):
    def __init__(self):
        self.kongfu = ['煎饼果子酱料']
        self.__money = 1000
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

#学校类
class School(object):
    def __init__(self):
        self.kongfu = ['学员班煎饼果子酱料']
    
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#徒弟类
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = ['自创班煎饼果子酱料']
    
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()
```
    注意：私有属性和私有方法只能在类内部访问和修改

## 7.2 获取和修改私有属性
在Python中，一般定义函数名`get_xx`用来获取私有属性，定义`set_xx`来修改私有属性值。

```python
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = ['自创班煎饼果子酱料']
        self.__money = 1000
    
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
    
    def get_money(self):
        return self.__money
    
    def set_money(self):
        self.__money = 500