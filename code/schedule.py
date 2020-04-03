import list_fun as lf

names = ["TY", "LK", "XU", "WLS", "LJY", "CJ"]
result = []

days = 5
people_per_day = 2

for _ in range(days):
    result.append([])

# print(result)    

candidates = []

while len(candidates) < people_per_day * days:
    candidates += lf.list_shuffle(names)

print(candidates)

for i in range(people_per_day * days):
    for j in range(len(candidates)):
        if not candidates[j] in result[i % days]:
            result[i % days].append(candidates[j])
            del candidates[j]
            break

print(result)