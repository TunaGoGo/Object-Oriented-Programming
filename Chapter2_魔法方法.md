# 4. 魔法方法
    在python中，__xx__()的函数叫魔法方法，指的是具有特殊功能的函数

## 4.1 __init__()
* 作用

    初始化对象

```python
class Washer():
    # 定义__init__, 添加实例属性
    def __init__(self):
        # 添加实例属性
        self.width =500
        self.height =8000

    def print_info(self):
        print(self.width)

haier1 = Washer()
haier1.print_info()
```

* 注意事项
  * `__init__()`方法，在创建对象时默认被调用，不需要手动调用
  * `__init__(self)`中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去

### 4.1.2 带参数的`__init__()`
    一个类可以创建多个对象，如何对不同的对象设置不同的初始化属性？ ————通过传参数

```python
class Washer():
    # 规划带参数的init
    def __init__(self,width,height)
        self.width = width
        self.height = height

    def print_info(self):
        print(self.width)
        print(self.height)

# 在创建对象时自动调用
haier1 = Washer(400,500)
haier1.print_info()

haier2 = Washer(300,600)
haier2.print_info()
```

## 4.2 `__str()__`
当使用print输出对象时，默认打印对象的内存地址。如果类定义了`__str()__`方法，那么就会打印从在这个方法中return的数据

* 作用
  
  * 解释说明:类的说明或对象状态的说明

```python
class Washer():
    # 规划带参数的init
    def __init__(self,width,height)
        self.width = width
        self.height = height

    def __str__(self):
        return '这是洗衣机的说明书'

haier = Washer(4,5)
print(haier)
```

## 4.3 `__del__()`
当删除对象时，python解释器也会默认调用`__del__()`

```python
class Washer():
    # 规划带参数的init
    def __init__(self,width,height)
        self.width = width
        self.height = height

    def __del__0(self):
        print('对象已经删除')

haier = Washer(4,5)
print(haier)
```