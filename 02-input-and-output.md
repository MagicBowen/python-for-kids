# 输入与输出

## 输出

### print

```python
print(5)
print("Jerry")  # 双引号中的是字符串，基本按照原样输出
print("Jerry, ", 10, " years old")  # 多个输出，用逗号隔开
print() # 输出空行
print(5 + 3) # 输出计算结果
```

### print rectangle

```python
print("rectangle)
print("---------------)
print("length   : ", 5)
print("width    : ", 4)
print("area     : ", 5 * 4)
print("perimete : ", (5 + 4) * 2)
```

加入要计算宽为3的长方形，如何修改程序？

## 使用变量

```python
l = 5
w = 4

print("rectangle)
print("---------------)
print("length   : ", l)
print("width    : ", w)
print("area     : ", l * w)
print("perimete : ", (l + w) * 2)
```

变量就是一个盒子，起个名字叫做变量名。变量的名字可长可短，好记就行。但是有些要求，例如数字不能作为变量名的开头等等。
每个变量的盒子里面可以住一个值。`=`左边是变量的盒子的名字，右边是放进去的值。

使用变量的时候，会把里面的值拿出来，比如`(l + w) * 2`;

可以更换变量盒子里的值：

```python
w = 5
print(w)
w = 6
print(w)
w = w + 1
print(w)
```

练习： 参照上面的计算长方形的面积和周长的程序，写一个计算正方形周长和面积的程序；
比如对于一个边长为3的正方形，要能输入如下：

```
square
----------------
side : 3
area : 9
perimeter : 12
```

## 输入

### input

```python
name = input()

name = input("What is your name?")

age = input("How old are you?")
```

### 统计程序

```python
name = input("What is your name?")
age = input("How old are you?")
sex = input("Are you a boy or a girl?")

print("Haha, you are ", name, " , you are ", age, " years old, and you are a ", sex)
```

改进输出：


```python
name = input("What is your name?")
age = input("How old are you?")
sex = input("Are you a boy or a girl?")

print("Haha, you are {name}, you are {age} years old, and you are a {sex}")
```

练习：修改计算长方形的程序，可以由程序提问长和宽的值。
