def sum(begin, end):
    s = 0
    for i in range(begin, end+1):
        s = s + i
    return s

def mul(begin, end):
    s = 1
    for i in range(begin, end + 1):
        s = s * i
    return s