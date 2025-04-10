# 求直教三角形斜边
import math
while True:
    try:
        a=float(input('请输入直角三角形第一条直角边长度'))
        b=float(input('请输入直角三角形第二条直角边长度'))
        c=math.sqrt(a**2+b**2)
        print('直角边分别为',a,'和',b,'的直角三角形，其斜边长为',c)
        
    except  ValueError:
        print('请输入正确的数值')

    Is=input('是否还须计算其他Rt三角形斜边长？需要则输入“Y”，不需要则按任意键退出。')
    if Is.upper()!='Y':
        break