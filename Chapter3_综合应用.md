# 5. 综合应用（案例）
## 5.1 烤地瓜
### 5.1.1 需求

需求主线：

1. 被烤的时间和对应的地瓜状态
   
   0-3分钟：生的
   3-5分钟： 半生不熟
   5-8分钟： 熟的
   超过8分钟： 烤糊了

2. 添加调料：
   用户根据自己的意愿来添加调料

### 5.1.2 步骤分析
需求涉及一个事物：地瓜，故案例涉及一个类：地瓜类

#### 5.1.2.1 定义类
* 地瓜的属性
  * 被烤的时间
  * 地瓜的状态
  * 添加的调料
* 地瓜的方法
  * 被烤
    * 用户根据意愿设定每个烤地瓜的时间
    * 判断地瓜被烤的总时间是哪个区间，修改地瓜状态
  * 添加调料
    * 用户根据意愿添加调料
    * 将用户添加的调料储存
* 显示对象信息

### 5.1.3 代码实现
```python
# 1. 定义类
#     1.初始化属性
#     2.被烤，添加调料的方法
#     3.显示对象信息的__str__()
# 2. 创建对象并调用对应的实例方法
class SweetPotato():
    def __init__(self):
        #被烤时间
        self.cook_time = 0
        #被烤状态
        self.cook_static = '生的'
        #调料列表
        self.condiments = []
    
    def cook(self,time):
        """
        烤地瓜的方法
        """
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟的'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        elif 8 <= self.cook_time:
            self.cook_static = '烤糊了'
    
    def add_condiments(self,condiment):
        """
        添加调料
        """
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static},口味是{self.condiments}'

# 创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)
digua1.cook(2)
print(digua1)

digua1.add_condiments('spciy')
print(digua1)
```

## 5.2 搬家具
### 5.2.1 需求

将小于房子剩余面积的家具摆放到房子中

### 5.2.2 步骤分析
需求涉及两个事物：房子和家具，故案例涉及两个类：房子类和家具类

#### 5.2.2.1 定义类
* 房子类
  * 实例属性
    * 房子地理位置
    * 房子占地面积
    * 房子剩余面积
    * 房子内家具列表
  * 实例方法
    * 容纳家具
  * 显示房屋信息
* 家具类
  * 实例属性
    * 家具名称
    * 家具占地
  * 实例方法

### 5.2.3 代码实现


```python
#家具类
class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

# 房子类
class House():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []
    
    def add_furniture(self, item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.area -= item.area
        else:
            print('家具太大，剩余面积不足，不能容纳')

    def __str__(self):
        return f'房子位于{self.address},占地面积{self.area}, 剩余面积{self.free_area}, 现有家具{self.furniture}'

bed = Furniture('床', 10)
sofa = Furniture('沙发', 50)

home1 = House('北京',100)
home1.add_furniture(bed)
home1.add_furniture(sofa)

print(home1)
```

# 6. 总结
* 面向对象重要组成部分
  * 类
    * 创建类
  ```python
  class 类名():
    code
  ```
  * 对象
  ```python
  对象名 = 类名()
  ```
* 添加对象属性
  * 类外面
  ```python
  对象名.属性名
  ```
  * 类里面
  ```python
  self.属性名
  ```
* 魔法方法
  * `__init__()`: 初始化
  * `__str__()`: 输出对象信息
  * `__del__()`: 删除对象时调用