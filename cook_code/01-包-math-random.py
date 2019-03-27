print('hello world')
import time

import math
import random

'''
# celi 向上取整
print(math.ceil(5.01))
print(math.ceil(5.9))
# floor向下取整
print(math.floor(8.9))

import keyword

# 查看系统保留的关键子，不可以用来当做变量命名
# print(keyword.kwlist)

# round四舍五入
print(round(5.4))
print(round(5.5))
# 开方函数：sqrt->返回浮点数
print(math.sqrt(4))
# 与幂运算差不多 pow()计算一个数的几次方
print(math.pow(2, 3))  # 2的3次方返回浮点数
print(2 ** 3)  # 返回整数

# 取绝对值 fabs()

print(math.fabs(-9))  # 返回浮点数
print(math.fabs(0))
print(math.fabs(9))

# abs() python内置函数,返回值有本身的类型而定
print(abs(9))
print(abs(-5.0))

# fsum()求和 sum()python内置函数求和
print(math.fsum([1, 2, 3, 4]))  # 返回浮点数
print(sum([1, 2, 3, 4]))


# math.modf() 将一个浮点数拆分为整数和小数部分，组成元祖(小数部分,整数部分)
print(math.modf(4.5))  # 小数在前整数在后
print(math.modf(0))
# math.copysign() # 将第二个数的符号传给第一个数,返回第一个数值的浮点数
print(math.copysign(2,-3))

print(math.pi)
print(math.e)

# random()  # 获取0-1之间的水机小数，[0,1)
# random.randint(1,9) # 随机指定开始和结束之间的整数值[1,9]
for i in range(10):
    print(random.random())
    print(random.randint(1, 9))
# random.randrange() 获取指定开始和结束之间的值,可以指定间隔值

for i in range(10):
    print(random.randrange(1, 10, 2))


# random.choice() # 随机获取列表中的值
print(random.choice([1, 2, 3, 4, 5, 6, 9]))

# random.shuffle() 随机打乱序列
list1 = [1, 2, 3, 4, 56]
random.shuffle(list1)
print(list1)

'''
# random.uniform() 随机获取指定范围的值（包括小数）
print(random.uniform(1, 9))
