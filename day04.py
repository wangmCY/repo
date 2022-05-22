# 实现100以内的偶数求和
# sum = 0
# for i in range(0, 101, 2):
#     sum += i
#
# print(sum)

# sum = 0
# for i in range(101):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# # 猜数字游戏
# import random
#
# answer = random.randint(1,100)
# count=0
# while True:
#     count+=1
#     number=int(input("请输入数字："))
#
#     if number<answer:
#         print("大一点")
#     elif number>answer:
#         print("小一点")
#     else:
#         print("你猜对了")
#         break
# print('你总共猜了%d次'% count)
# if count>7:
#     print('你的智商需要充值了。')

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

# 寻找水仙花数
"""
水仙花数即为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，例如：1^3+5^3+3^3=153。
"""
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == high ** 3 + mid ** 3 + low ** 3:
#         print(num)

# 正整数的反转
# num = int(input('num='))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

# 百钱百鸡
"""
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，
问公鸡、母鸡、小鸡各有多少只？
"""
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if z / 3 + y * 3 + x * 5 == 100:
            print('公鸡：%d只，母鸡：%d只,小鸡：%d只' % (x, y, z))
