import list_fun as lf

names = ["田宇", "李继英", "陈洁", "宫思琦", "刘珂", "王宇如"]
days = 5

result = []

for _ in range(days):
    result.append([])

candidates = []

a1 = lf.list_shuffle(names)

candidates = candidates + a1

a1 = lf.list_shuffle(names)
candidates = candidates + a1[0 : 4]

for i in range(len(result)):
    result[i].append(candidates[2 * i])
    result[i].append(candidates[2 * i + 1])

weekday = ["星期一", "星期二", "星期三", "星期四", "星期五"]

for i in range(len(weekday)):
    print(weekday[i], ":", result[i][0], result[i][1])