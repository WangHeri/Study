
# print("----------------主菜单------------------")
# print("周杰轮，您好，欢迎来到黑马银行ATM。请选择操作：")
# print("查询余额\t[输入1]")
# print("存款\t\t[输入2]")
# print("取款\t\t[输入3]")
# print("退出\t\t[输入4]")
# input("请输入您的选择：")

# print()
# print("----------------查询余额------------------")
# print("周杰轮，您好，您的余额剩余：5000000元")
# print("------------------------------")

# print("----------------取款------------------")
# print("周杰轮，您好，您取款50000元成功")
# print("周杰轮，您好，您的余额剩余：4950000元")


# 自己写的

money = 500
name = input("请输入您的姓名:")

def main():
    print(f'{name},您好，欢迎来到银行，请选择您的操作')
    print("查询余额请输入：1")
    print("存款\t请输入：2")
    print("取款\t请输入：3")
    print("退出\t请输入：4")
    result = input("请输入您的选择： ")
    return result

# 查询余额函数
def yue(x):
    global money
    if x:
        print("------------------查询余额------------------")
        print(f'{name},您好，您当前账户余额为：{money}元\n')
        print()


# 取款函数
def qukuan():
    x = int(input("请输入你要取款的金额："))
    global money
    money = money - x
    if money >= 0:
        print("---------  ---------取款------------  ------")
        print(f'{name},您好，您取款{x}元成功')  
        print(f'{name},您好，您当前账户余额为：{money}元\n')
        print()
    else:
        money = money + x
        print("---------  ---------取款------------  ------")
        print(f'{name},您好，您取款{x}元失败，余额不足')
        print(f'{name},您好，您当前余额{money}元')
        print()
    
# 存款函数
def cunkuan():
    x = int(input("请输入你要存款的金额："))
    global money
    money = money + x
    print("---------  ---------存款------------  ------")
    print(f'{name},您好，您存款{x}元成功')  
    print(f'{name},您好，您当前账户余额为：{money}元\n')
    print()

while True:
    Keyboardinput = main()
    if Keyboardinput == "1":
        yue(1)
        continue
    elif Keyboardinput == "2":
        cunkuan()
        continue 
    elif Keyboardinput == "3":
        qukuan()
        continue             
    else:
        print("将退出源氏木语银行系统！")
        break
