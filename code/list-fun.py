import random

def list_max(a):
    m = a[0]
    for i in a:
        if m < i:
            m = i
    return m

def list_min(a):
    m = a[0]
    for i in a:
        if m > i:
            m = i
    return m

def list_sum(a):
    m = 0
    for i in a:
        m += i
    return m

def list_clear(a):
    return []

def list_reverse(a):
    middle = len(a) // 2
    for i in range(0, middle + 1):
        j = -1 - i
        t = a[i]
        a[i] = a[j]
        a[j] = t
    return a

def list_rand(a):
    i = random.randint(0, len(a)-1)
    return a[i]

a = [2, 3 ,1, -1, 9]
print(a.sort())