# 编写程序，找出所有的水仙花数:三位数，各位数字立方和等于该数字本身。
def cube(n):
    a=n%10
    b=n//10%10
    c=n//100
    return(a**3+b**3+c**3)

num_lst=[
    num
    for num in range(100,1000)
    if cube(num)==num
]
print(f'水仙花数有{len(num_lst)}个：',end=' ')
print(*num_lst,sep=',')