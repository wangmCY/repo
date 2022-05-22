# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
#
# if unit == 'in' or unit == '英寸':
#     x = value * 2.54
#     print('%.1f英寸 = %.1f厘米' % (value, x))
# elif unit == 'cm' or unit == '厘米':
#     x = value / 2.54
#     print('%.1f英寸 = %.1f厘米' % (value, x))
#
# else:
#     print('请输入正确的单位')

# from random import randint
#
# face = randint(1, 6)
# if face == 1:
#     result = '去唱歌'
# elif face == 2:
#     result = '去吃饭'
# elif face == 3:
#     result = '去洗澡'
# elif face == 4:
#     result = '去跑步'
# elif face == 5:
#     result = '去玩游戏'
# else:
#     result = '去敲代码'
# print(face,result)

sorce = float(input('请输入成绩：'))

if sorce >= 90:
    grade = 'A'
elif sorce >= 80:
    grade = 'B'
elif sorce >= 70:
    grade = 'C'
elif sorce >= 60:
    grade = 'D'
else:
    grade = 'E'

print('对应的等级是：', grade)
