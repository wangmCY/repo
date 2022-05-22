# 生成斐波那契数列的前20个数
"""
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐
波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
"""
# a = 0
# b = 1
#     (a, b) = (b, a + b)
#     print(a, end=" ")

# 找出10000以内的完美数
"""
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身
如6=1+2+3，28=1+2+4+7+14
"""
# import time
# import math
#
# # start = time.clock()
# for num in range(1, 10000):
#     sum = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             sum += factor
#             if factor > 1 and num / factor != factor:
#                 sum += num / factor
#     if sum == num:
#         print(num)
# # end = time.clock()
# # print("执行时间:", (end - start), "秒")

# 输出100以内的所有素数
"""
素数指的是只能被1和自身整除的正整数（不包括1）
"""
import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
