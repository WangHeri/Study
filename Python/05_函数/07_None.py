"""
演示特殊字面量：None
"""

# # 无return语句的函数返回值
# def say_hi():
#     print("你好呀")

# result = say_hi()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")

# # 主动返回None的函数
# def say_hi2():
#     print("你好呀")
#     return None

# result = say_hi2()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")

# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None  #等同于返回false

result = check_age(16)
"""
if not 判断是否为NONE
代码中经常会有判断变量是否为NONE的情况,主要有三种写法:
第一种: if x is None(最清晰)
第二种: if not x
第三种: if not x is Non

使用if not x这种写法的前提是：必须清楚x等于None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()时对你的判断没有影响才行.
在Python中 None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False；
因此在使用列表的时候，如果你想区分x==[]和x==None两种情况的话, 此时if not x：将会出现问题：
"""
if not result:
    # 进入if表示result是None值 也就是False
    print("未成年，不可以进入")



# None用于声明无初始内容的变量
name = None
