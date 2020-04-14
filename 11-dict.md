# 数据结构：dict

## 基础

```python
a = {1 : "h", 2 : "e", 3 : "o"}

a[4] = "l"

a["he"] = "llo"

del a[1]

for k, v in a.items():
    print(k, v)

k = 1
if k in a:
    print("key 1 in dict")
```

## 复合数据结构

```python
courses = {
    "MON" : {"morning" : ["math", "english", "painting"], "afternoon" : ["music", "sports"]},
    "TUE" : {"morning" : ["physical", "math", "sports"],  "afternoon" : ["english"]}
}

a = courses["MON"]
print(type(a))

a = courses["MON"]["morning"]
print(type(a))

a = courses["MON"]["morning"][1]
print(type(a))

courses["MON"]["morning"][2] = "physical"

```

practice：

- 制作一个人员电话表，支持插入、查询
- 演进人员电话表，演进成人员信息表
- 制作一个课表
