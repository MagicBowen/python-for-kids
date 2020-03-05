# 流程图

框： 

- begin，end
- input
- statement
- condition
- line

循序语句： 箭头向下走
条件语句： 菱形，向下True和False，没有从下向上的返回箭头
循环语句： 菱形，向下True和False，有从下向上的返回箭头
break：跳出向下； continue：向上返回

注意：for循环的自增语句的位置

练习：

- 画出一下程序的流程图

```python
n = int(input("max?"))

sum = 0

# for i in range(1, 101):
#     if i % 3 == 0:
#         sum = sum + i
i = 1
while i <= n:
    if i % 3 == 0:
        sum = sum + i
    i = i + 1

print(sum)
```

- 实现水仙花数的程序，并画出流程图

---

流程图反向练习，给出流程图，填其中缺失的数字或者语句；
补全后将流程图变成程序（注意continue语句的练习）