import random

def list_shuffle(a):
    for i in range(len(a)):
        j = random.randint(0,len(a) - 1)
        t = a[i]
        a[i] = a[j]
        a[j] = t
    return a

def get_color(c):
    j = (c-1) // 13
    if j == 0:
        return "Spade"  
    if j == 1:
        return "Heart"
    if j == 2:
        return "Club"
    return "Diamond"

def get_number(c):
    n = c % 13
    if n == 0:
        return "K"
    if n == 1:
        return "A"
    if n == 11:
        return "J"
    if n == 12:
        return "Q"
    return str(n)

def print_card(c):
    color = get_color(c)
    number = get_number(c)
    print(color, number)

print_card(24)