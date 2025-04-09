# 有四个数字:1、2、3、4，能组成多少个互不相同且无重复数字的三位数?各是多少?
# 使用for循环
num_lst1=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i:
                num=100*i+10*j+k
                num_lst1.append(num)
print(f'1、2、3、4能组成{len(num_lst1)}个互不相同且无重复数字的三位数:{num_lst1}')

# 列表推导式
num_lst2 = [
    100*i + 10*j + k
    for i in range(1, 5)
    for j in range(1, 5) 
    for k in range(1, 5)
    if len({i, j, k}) == 3  # 使用集合去重判断
]

# 优化输出格式，*解包
print(f'1、2、3、4能组成{len(num_lst2)}个互不相同且无重复数字的三位数:',end=' ')
print(*num_lst2, sep=', ')  # 使用*解包和sep参数美化输出