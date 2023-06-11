"""
小练习：
定义字符串变量name，内容为："itheima is a brand of itcast"
通过for循环，遍历此字符串，统计有多少个英文字母："a"
提示：
1. 计数可以在循环外定义一个整数类型变量用来做累加计数
2. 判断是否为字母"a"，可以通过if语句结合比较运算符来完成
"""
# 统计如下字符串中，有多少个字母a
name = "itheima is a brand of itcast"
"""
# # 定义一个变量，用来统计有多少个a
# count = 0

# # for 循环统计
# # for 临时变量 in 被统计的数据:
# for x in name:
#     if x == "a":
#         count += 1

# print(f"被统计的字符串中有{count}个a")
"""

num = 0
for x in name:
    if x == "a":
        num += 1
print(f"这句话里一共有{num}个a")





