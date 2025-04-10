# 输入整数a、b表示一个闭区间，找出该区间内的所有素数并打印
# import math
# while True:
#     try:
#         prime_lst=[]
#         a,b=int(input('请输入区间下限a:')),int(input('请输入区间上限b:'))
#         if a<=b:
#             for n in range(a,b+1):
#                 if n==1:
#                     continue
#                 elif n==2:
#                    prime_lst.append(n)
#                 elif n % 2 == 0:  # 跳过偶数
#                     continue
#                 elif n>2:
#                     q=int(math.sqrt(n))+1
#                     is_prime=True
#                     for i in range(3,q,2): 
#                         if n%i==0:
#                             is_prime=False
#                             break    
#                     if is_prime:
#                         prime_lst.append(n)
#             print(f'区间[{a},{b}]内的素数有{len(prime_lst)}个:{prime_lst}')                 
#         else:
#             print('a应该小于等于b，请重新输入')
#     except ValueError :
#          print('输入类型错误，请输入整数a、b')
    
import math

def find_primes(a, b):
    prime_lst = []
    for n in range(a, b+1):
        if n <= 1:
            continue
        elif n == 2:
            prime_lst.append(n)
        elif n % 2 == 0:
            continue
        else:
            is_prime = True
            q = int(math.sqrt(n)) + 1
            for i in range(3, q, 2):
                if n % i == 0:
                    is_prime = False
                    break    
            if is_prime:
                prime_lst.append(n)
    return prime_lst

while True:
    try:
        a, b = int(input('请输入区间下限a:')), int(input('请输入区间上限b:'))
        if a <= b:
            primes = find_primes(a, b)
            print(f'区间[{a},{b}]内的素数有{len(primes)}个:{primes}')                 
        else:
            print('a应该小于等于b，请重新输入')
    except ValueError:
        print('输入类型错误，请输入整数a、b')       