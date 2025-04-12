# 海伦公式是利用三角形的三条边的边长直接求三角形面积的公式
# p=(a+b+C)/2
# S=√p(p-a)(p-b)(p-c)
import math

def triangle(side1, side2, side3):
    # 先检查所有边是否为正数
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
    
    trian = [side1, side2, side3]
    trian.sort()
    # 三角形两边之和大于第三边
    return trian[0] + trian[1] > trian[2]

try:
    sides = input('请输入三角形三条边长，以空格隔开：')
    three_side = list(map(float, sides.split(' ')))
    if len(three_side) != 3:
        print('请输入三个数字')
    elif triangle(three_side[0], three_side[1], three_side[2]):
        p = (three_side[0] + three_side[1] + three_side[2]) / 2
        area = math.sqrt(p * (p - three_side[0]) * (p - three_side[1]) * (p - three_side[2]))
except ValueError:
    print('请输入有效的数字')
finally:
    print(f'边长为{sides}的三角形，面积为{area:.2f}.')