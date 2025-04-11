# 个数如恰好等于除了它以外的因子之和，这个数就称为“完数”。编程序找出1000以内的所有完数，(6是一个"完数"，它的因子是1,2,3)。
def is_perfect(num):
    factor_lst=[
        i
        for i in range(1,num)
        if num%i==0
    ]
    sum=0
    for factor in factor_lst:
        sum+=factor
    if sum==num:
        return True

perfect_lst=[
    nums
    for nums in range(1,1001)
    if is_perfect(nums)    
]
print(f'1000以内的完数有：',end=" ")
print(*perfect_lst,sep=',')