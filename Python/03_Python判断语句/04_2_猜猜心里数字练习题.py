"""
演示if elif else练习题：猜猜心里数字
"""

# 定义一个变量数字
num = 5

# 通过键盘输入获取猜想的数字，通过多次if 和 elif的组合进行猜想比较
if int(input("请猜一个数字：")) == num:
    print("恭喜第一次就猜对了呢")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("Sorry 猜错了")


A = int(input("请输入第一次猜想的数字："))
B = round(0,10)
if A == B:
	print(f"猜对了，我想的数字就是：{A}")
	break
else A = int(input("不对，再猜一次：")):
	if A == B:
		print(f"猜对了，我想的数字就是：{A}")
		break
	else A = int(input("不对，再最后猜一次："))
		if A == B:
			print(f"猜对了，我想的数字就是：{A}")
			break
		else:
			print(f"Sorry，全部猜错啦，我想的是：{A}")
			break
