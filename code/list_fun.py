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

def list_sort(a):
    for j in range(len(a)-2):
        for i in range(len(a) - j - 1):
            if a[i] > a[i+1]:
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
    return a

def list_shuffle(a):
    for i in range(len(a)):
        j = random.randint(0,len(a) - 1)
        t = a[i]
        a[i] = a[j]
        a[j] = t
    return a

def list_in(a, x):
    for v in a:
        if v == x:
            return True
    return False      
