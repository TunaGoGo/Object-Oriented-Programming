# 1. 理解面向对象编程
## 1.1 定义：

1. 是一种抽象化的语言，作用是简化代码

2. 面向对象是将编程当成一种事物，对外界来说，事物是可以直接使用的，不用去管他内部的情况，而编程就是设置内部事物能够做什么

# 2. 类和对象
## 2.1 定义：

用类去创建一个对象（对象：电脑，类：电脑的设计图纸）

## 2.2 类：
类是对一系列具有相同特征和行为的事物的统称，是一个抽象的概念，不是一个真实存在的事物。

    命名原则参考大驼峰表示法

1. 特征及是属性（变量）
2. 行为及是方法（函数）

## 2.3 对象
对象是类创建出来真实存在的事物，如电脑
    
    注意：开发中，先有类，再有对象

## 2.4 面向对象实现方法
### 2.4.1 定义类

```python
class 类名():
    code
```
### 2.4.2 定义对象
* 语法
```python
对象名 = 类名()
```
* 体验
```python
#创建对象
haier1 = Washer()

print(haier1)

# haier对象调用实例方法
haier1.wash()
```

### 2.4.3 实例
```python
#需求：洗衣机，功能：洗衣服
# 1.定义洗衣机类
"""
class 类名():
    code
"""
class Washer():
    def wash(self):
        print('能洗衣服')

# 2.创建对象
# 对象名 = 类名()
haier1 = Washser()

# 3.验证
#打印haier对象
print(haier1)

# 使用wash功能 --实例方法/对象方法 --对象名.Wash()
haier1.wash()
```

## 2.4 Self
self指的是调用该函数的对象。

```python
class Washer():
    def wash(self):
        print('洗衣服')
        print(self)
        
haier = Washer()

# 由于打印对象和self得到的地址是相同的，则self指的是调用该函数的对象

```
  1. 一个类可以创建多个对象
  2. 多个对象都调用这个函数的时候，self地址也是不同的
```python
class Washer():
    def wash(self):
        print('能洗衣服')
        print(self)

haier1 = Washer()
haier1.wash()
# 能洗衣服
# <__main__.Washer object at 0x0000028D03396310>

haier2 = Washer()
haier2.wash()
# 能洗衣服
# <__main__.Washer object at 0x0000028D0377A310>
```

# 3. 添加和获取对象属性

属性及是特征，比如：洗衣机的重量，高度。。。

对象属性既可以在类外面添加和获取，也可以在类的内部添加和获取

    不同对象属性不同，所以有必要对不用对象添加不同的属性

## 3.1 类外面添加对象属性

* 语法
```python
对象名.属性名 = 值
```

* 体验
```python
haier1.width = 100
haier1.height = 800
```

```python
class Washer():
    def wash(self):
        print('能洗衣服')
        print(self)

haier1 = Washer()
# 在外部为对象添加属性  对象名.属性名 = 值
haier1.width = 500
haier1.height = 600
```

## 3.2 类外面获取对象属性
* 语法
```python
对象名.属性名
```

* 体验
```python
print(haier1.width)
print(haier1.height)
```

## 3.3 类内部获取对象属性

* 语法
```python
self.属性名
```

* 体验
```python
class Washer():
    def wash(self):
        print('能洗衣服')
    
    #获取实例属性
    def print_info(self):
        print(self.width)
        print(self.height)

haier1 = Washer()

# 添加属性
haier1.width = 400
haier1.height = 800

# 对象属性调用方法
haier1.print_info()
```


