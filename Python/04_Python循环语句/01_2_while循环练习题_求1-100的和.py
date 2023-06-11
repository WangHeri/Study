"""
演示while循环基础练习题：求1-100的和
"""
# sum = 0
# i = 1
# while i<=100:
#     sum += i
#     i += 1

# print(f"1-100累加的和是：{sum}")

sum = 0
i = 1
while i < 101:
    sum = sum + i
    i = i + 1
print(f"1-100累加和是：",sum)