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