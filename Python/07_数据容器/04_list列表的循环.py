"""
演示使用while和for循环遍历列表
"""

def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量：通过下标索引来控制，默认是0
    # 每一次循环，将下标索引变量+1
    # 循环条件：下标索引变量 < 列表的元素数量

    # 定义一个变量，用来标记列表的下标
    index = 0       # 初始下标为0
    while index < len(mylist):
        # 通过index变量取出对应下标的元素
        element = mylist[index]
        print(f"列表的元素：{element}")

        # 至关重要：将循环变量（index）每一次循环都+1
        index += 1

def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    mylist = [1, 2, 3, 4, 5]
    # for 临时变量 in 数据容器:
    for element in mylist:
        print(f"列表的元素有：{element}")


if __name__ == '__main__':
    # list_while_func()
    list_for_func()


List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List2 = []

for i in List1:
    if i % 2 == 0:
        List2.append(i)
print(f"通过for循环从，从列表{List1}中取出偶数，组成新的列表{List2}")

index = 0

while index < len(List1):
    yuansu = List1[index]
    if yuansu % 2 == 0:
        List2.append(yuansu)
    index += 1
print(f"通过while循环从，从列表{List1}中取出偶数，组成新的列表{List2}")
