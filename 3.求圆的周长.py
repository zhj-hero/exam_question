# 求圆的周长
# 不建议写法，因为没有考虑到用户输入非数字的情况，会导致程序崩溃。
# while True:
#     radiant=int(input('请输入圆的半径'))
#     circle=2*3.14*radiant
#     print('半径为',radiant,'的圆，其周长为：',circle)
#     Is=input('是否还须计算其他圆的周长？需要则输入“Y”，不需要则按任意键退出。')
#     if  Is!='Y':
#         break



# 建议写法，使用try-except语句来捕获用户输入的异常，从而避免程序崩溃。
while True:
    try:
        radiant = float(input('请输入圆的半径：'))
        circle = 2 * 3.14 * radiant
        print('半径为', radiant, '的圆，其周长为：', circle)
    except ValueError:
        print("请输入有效的数字！")
        continue
        
    Is = input('是否还须计算其他圆的周长？需要则输入"Y"，不需要则输入其他任意键退出：')
    if Is.upper() != 'Y':
        break