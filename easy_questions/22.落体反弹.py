# 球从100米高度自由落下，每次落地后反跳回原高度的一半;再落下，求它在第10次落地时，共经过多少米?第10次反弹多高?
import re

# 递归函数
def distance(height, n, current=1, total=0):
    if current == 1:  # 第一次只有下落
        return distance(height/2, n, current+1, total + height)
    elif current > n:
        return total, height
    else:  # 后续有下落和弹起
        return distance(height/2, n, current+1, total + height*2)

# 迭代函数
def fouction(height, n):
    total = height
    courrent_height = height
    for i in range(2, n+1):
        courrent_height /= 2
        total += courrent_height * 2 
    return total, courrent_height / 2

string = input('请输入起始高度和弹跳次数，中间用逗号隔开，如“100,10”:\t')
lst = re.split(r',', string)
height = float(lst[0])
n = int(lst[1])

#递归解法 
total_distance, final_bounce = distance(height, n)
print(f'第{n}次落地时，共经过{total_distance:.2f}米，第{n}次反弹{final_bounce:.2f}米。')
# 迭代解法
total_dis, final_boun = fouction(height, n)
print(f'第{n}次落地时，共经过{total_dis:.2f}米，第{n}次反弹{final_boun:.2f}米。')