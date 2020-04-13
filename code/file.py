import json

# ct = {"周一":"语文 ，英语 ，数学 ，体育" ,
#     "周二":"数学 ，自习 ，语文 ，自习" ,
#     "周三":"自习 ，自习 ，语文 ，自习",
#     "周四":"化学 ，物理 ，生物 ，化学",
#     "周五":"语文 ，化学 ，自习 ，体育"}

f = open("data.txt", "r+")

# json.dump(ct, f)

ct = json.load(f)

print(ct["周一"])

f.close()