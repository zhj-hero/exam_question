# 获取用户输入的整数
a=int(input('请输入一个整数：'))

# 使用循环计算阶乘
factorial=1
if a==0:
    print('0的阶乘为：1')
else:
    for i in range(1,a+1):
        factorial=factorial*i
    print(a,'的阶乘为：',factorial,sep='')

# 定义递归函数计算阶乘
def factorial(a):
    if a==0:  # 0的阶乘为1
        return 1    
    else:
        return a*factorial(a-1)  # 递归调用

# 调用递归函数并打印结果        
print(a,'的阶乘为：',factorial(a),sep='')