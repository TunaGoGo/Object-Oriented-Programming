# 1. 了解异常
当检测到错误时，解释器就无法继续执行，反而出现了一些错误的提示

# 2. 异常的写法
```python
try:
    可能发生的错误
except:
    如果出现异常执行的代码
```

## 2.1 捕获指定异常
```python
try:
    可能发生的错误

except 异常类型: 
    如果出现异常执行的代码
```

    注意：

    1、如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
    2、一般try下方只放一行尝试执行的代码

## 2.2 捕获多个指定异常
当捕获多个指定异常时，可以把要捕获异常类型的名字，放在except之后，并使用元组的方式进行书写
```python
try:
    可能发生的错误

except (异常类型1,异常类型2): 
    如果出现异常执行的代码
```
## 2.3 捕获异常描述信息
```python
try:
    可能发生的错误

except (异常类型1,异常类型2) as result: 
    print(result)
```

## 2.3 捕获所有异常
Exception是所有程序异常类的父类
```python
try:
    可能发生的错误

except Exception as result: 
    print(result)
```

## 2.4 异常else

```python
try:
    可能发生的错误

except Exception as result: 
    print(result)

else:
    print("code without exception")
```

## 2.4 异常finally
finally 表示无论异常都要执行的代码，例如关闭文件
```python
try:
    f = open("text.txt","r")

except Exception as result: 
    f = open("text.txt","w")

else:
    print("code without exception")

finally: #释放内存
    f.close()
```