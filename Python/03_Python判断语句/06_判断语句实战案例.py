"""
演示判断语句的实战案例：终极猜数字
"""

# # 1. 构建一个随机的数字变量
# import random
# num = random.randint(1, 10)

# guess_num = int(input("输入你要猜测的数字："))

# # 2. 通过if判断语句进行数字的猜测
# if guess_num == num:
#     print("恭喜，第一次就猜中了")
# else:
#     if guess_num > num:
#         print("你猜测的数字大了")
#     else:
#         print("你猜测的数字小了")

#     guess_num = int(input("再次输入你要猜测的数字："))

#     if guess_num == num:
#         print("恭喜，第二次猜中了")
#     else:
#         if guess_num > num:
#             print("你猜测的数字大了")
#         else:
#             print("你猜测的数字小了")

#         guess_num = int(input("第三次输入你要猜测的数字："))

#         if guess_num == num:
#             print("第三次猜中了")
#         else:
#             print("三次机会用完了，没有猜中。")




# 上面是老师的代码，下面两种是自己写的

import random
num = random.randint(1,10)
guess = int(input("第一次机会请输入我心里想的数字："))
if guess > num:
    print("猜大了，猜小一点")
    guess = int(input("第二次机会，请输入我心里想的数字："))
    if guess > num:
        print("猜大了，猜小一点")
        if int(input("第三次机会，请输入我心里想的数字：")) == num:
            print(f"恭喜第三次机会终于猜对了，我心里想的数字就是：",num)
        else:
            print(f"很遗憾三次机会已经用完，我心里想的数字是：",num)
    elif guess < num:
        print("猜小了了，猜大一点")
        if int(input("第三次机会，请输入我心里想的数字：")) == num:
            print(f"恭喜第三次机会终于猜对了，我心里想的数字就是：",num)
        else:
            print(f"很遗憾三次机会已经用完，我心里想的数字是：",num)
    else:
        print(f"恭喜第二次机会，猜对了，我心里想的数字就是：",num)
elif guess < num:
    print("猜小了了，猜大一点")
    guess = int(input("第二次机会，请输入我心里想的数字："))
    if guess > num:
        print("猜大了，猜小一点")
        if int(input("第三次机会，请输入我心里想的数字：")) == num:
            print(f"恭喜第三次机会终于猜对了，我心里想的数字就是：",num)
        else:
            print(f"很遗憾三次机会已经用完，我心里想的数字是：",num)
    elif guess < num:
        print("猜小了了，猜大一点")
        if int(input("第三次机会，请输入我心里想的数字：")) == num:
            print(f"恭喜第三次机会终于猜对了，我心里想的数字就是：",num)
        else:
            print(f"很遗憾三次机会已经用完，我心里想的数字是：",num)
    else:
        print(f"恭喜第二次机会，猜对了，我心里想的数字就是：",num)
else:
    print(f"恭喜第一次就猜对了，我心里想的数字就是：",num)



guessnum = int(input("第一次机会请输入我心里想的数字："))
if  guessnum == num:
    print("真厉害，第一次就猜出来了")
else:
    if guessnum > num:
        print("猜大了，再给一次机会")
        guessnum = int(input("第二次机会，请输入我心里想的数字："))
        if guessnum == num:
            print("勉强还行，第二次猜出来的")
        else:
            if guessnum > num:
                print("猜大了，最后一次机会")
                guessnum = int(input("最后一次机会，请输入我心里想的数字："))
                if guessnum == num:
                    print("刚刚及格吧，第三次猜出来的")
                else:
                    print("不及格，三次都猜不出来")
            else:
                print("猜小了，最后一次机会")
                guessnum = int(input("最后一次机会，请输入我心里想的数字："))
                if guessnum == num:
                    print("刚刚及格吧，第三次猜出来的")
                else:
                    print("不及格，三次都猜不出来")                
    else:
        print("猜小了，再给一次机会")
        guessnum = int(input("第二次机会，请输入我心里想的数字："))
        if guessnum == num:
            print("勉强还行，第二次猜出来的")
        else:
            if guessnum > num:
                print("猜大了，最后一次机会")
                guessnum = int(input("最后一次机会，请输入我心里想的数字："))
                if guessnum == num:
                    print("刚刚及格吧，第三次猜出来的")
                else:
                    print("不及格，三次都猜不出来")
            else:
                print("猜小了，最后一次机会")
                guessnum = int(input("最后一次机会，请输入我心里想的数字："))
                if guessnum == num:
                    print("刚刚及格吧，第三次猜出来的")
                else:
                    print("不及格，三次都猜不出来")


# 对上面的代码进行优化
guessnum = int(input("第一次机会请输入我心里想的数字："))
if  guessnum == num:
    print("真厉害，第一次就猜出来了")
else:
    if guessnum > num:
        print("猜大了，再给一次机会")
    else:
        print("猜小了，再给一次机会")
    guessnum = int(input("第二次机会，请输入我心里想的数字："))
    if guessnum == num:
        print("勉强还行，第二次猜出来的")
    else:
        if guessnum > num:
            print("猜大了，最后一次机会")
        else:
            print("猜小了，最后一次机会")
        guessnum = int(input("第三次机会，请输入我心里想的数字："))
        if guessnum == num:
            print("及格，用了三次机会才猜出来的")
        else:
            print(f"三次都猜不出来，笨死了，我心里想的数字是:",num)
   