# 字符串变量与操作

```python
s = "hello"
p = 'world'
r = s + p
print(r)
print(s + " " + p)
print("{s} {p}")
print('-' * 10)

splitter = "-" * 10
print(splitter)
```

练习：修改计算长方形的程序，可以由程序提问长和宽的值。


```python
l = input("length ?\n")
w = input("weight ?\n")

print("rectangle")
print("---------------")
print("length   : ", l)
print("width    : ", w)
print("area     : ", l * w)
print("perimete : ", (l + w) * 2)
```

error?

```python
l = input("length ?\n")
w = input("weight ?\n")

l = int(l)
w = int(w)

print("rectangle")
print("---------------")
print("length   : ", l)
print("width    : ", w)
print("area     : ", l * w)
print("perimete : ", (l + w) * 2)
```

练习：修改计算正方形面积的程序，使得用户可以手动输入边长

## 扩展

字符串操作函数

## practice

- 字符串分割和拼接
- 求子串
- 回文