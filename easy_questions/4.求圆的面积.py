# 求圆的面积
import math
while True:
    try:
        radius = float(input('请输入圆的半径：'))
        area = math.pi * radius ** 2
        print('半径为', radius, '的圆，其面积为：', area)
    except ValueError:
        print("请输入有效的数字！")
        continue
    Is = input('是否还须计算其他圆的面积？需要则输入"Y"，不需要则输入其他任意键退出：')
    if Is.upper()!= 'Y':
        break
