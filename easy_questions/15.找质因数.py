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

# 递归函数，用于找出所有的质因数
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

# 第二种方式

factors = []
divisor = 2
while divisor * divisor <= pos_integer:  # 只需检查到√n
    if pos_integer % divisor == 0:
        factors.append(divisor)
        pos_integer //= divisor  # 改为整数除法
    else:
        divisor += 1
if pos_integer > 1:  # 处理最后剩下的质数
    factors.append(pos_integer)
print(factors)
