import math
import random

time = 3
rand = random.randrange(100, 999)
print(rand)
while time > 0:
    num = input('请输入一个三位数')
    # 输入的是字符串，需要转换一下类型
    # 检测是否是纯数字
    if num.isdigit() and 100 <= int(num) <= 999:
        num = int(num)
        # 判断输入的数与随机数比较大小
        if num == rand:
            print('恭喜回答正确')
            break
        elif num > rand:
            print('大小大了，请从新输入')
        else:
            print('小了小了，请从新输入')
        time -= 1
    else:
        print('请按规定输入')
