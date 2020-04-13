import json

f = open("course.json", "r+")

ct = json.load(f)

valid_date = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
czzn = ["1", "2", "3", "4", "5"]

print("欢迎使用课表！")
while True:
    print("=" * 50)
    cz = input("请选择下面的操作：（1）查课表 （2）加课表 （3）修课表 （4）删课表 (5) 退出，输入" + str(czzn) + " ： ")
    if not cz in czzn:
        print("输入的操作错误！")
        continue

    if cz == "5":
        print("欢迎下次使用，再见！")
        break

    week = input("请输入星期，例如" + str(valid_date) + " : ")
    if not week in valid_date:
        print("输入的星期错误！")
        continue

    if cz == "1":
        if week in ct:
            print(week, ":", ct[week])
        else:
            print("这天没有课，休息！")
        
    elif cz == "2":
        if week in ct:
            print("今天已经有课了，不能加课了!")
        else:
            course = input("请按顺序输入这一天要加的课程（输完后请回车）:")
            ct[week] = course
            print(week + "的课已经添加成功！！！")

    elif cz == "3":
        if not week in ct:
            print(week + "没有课，不能修改!")
        else:
            course = input("请按顺序输入改完后全部一天的课程（输完后请回车）:")
            ct[week] = course
            print(week + "的课已经修成功！！！")
    
    else:
        if not week in ct:
            print(week + "没有课，不能删除!")
        else:
            del ct[week]
            print(week + "的课已经删除成功！！！")

f.seek(0)
f.truncate()

json.dump(ct, f)
f.close()