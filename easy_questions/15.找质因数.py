# 输入一个正整数，输出它的所有质数因子(如180的质数因子为 2、2、3、3、5).
import math

def is_prime(n):
    is_p = True
    q = int(math.sqrt(n)) + 1
    if n % 2 == 0:
        pass
    else:
        for i in range(3, q, 2):
            if n % i == 0:
                is_p = False
                break  
    return is_p

# def pr_factors(num, prime_lst=None):
#     if prime_lst is None:
#         prime_lst = []
#     if num == 1:
#         return prime_lst
#     for j in range(2, num + 1):
#         if is_prime(j) and num % j == 0:
#             prime_lst.append(j)
#             return pr_factors(num // j, prime_lst)  # 关键修改：立即返回递归结果
#     return prime_lst  # 处理num本身就是质数的情况

def pr_factors(num, prime_lst=None, start=2):
    if prime_lst is None:
        prime_lst = []
    if num == 1:
        return prime_lst
    for j in range(start, num + 1):
        if is_prime(j) and num % j == 0:
            prime_lst.append(j)
            return pr_factors(num // j, prime_lst, j)  # 从j开始检查
    return prime_lst

pos_integer = int(input('请输入一个正整数：'))
print(f'{pos_integer}的质数因子有：{pr_factors(pos_integer)}')


