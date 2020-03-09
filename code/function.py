def inc(x):
    x = x + 1

def ap(a):
    a.append(4)

def cat(s):
    s = s + "_post" 

x = 5
inc(x)
print(x)

a = [1, 2, 3]
ap(a)
print(a)

s = "hello"
cat(s)
print(s)