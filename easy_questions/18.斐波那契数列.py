# 又称免子数列，指的是这样一个数列:1、1、2、3、5、8、13、21、34、编写程序找出第n个项

n = int(input('请输入你想查看的斐波那契数列元素序号：'))
prev, curr = 1, 1

if n == 1 or n == 2:
    print(f'斐波那契数列第{n}个元素是：1.')
else:
    for _ in range(3, n+1):
        prev, curr = curr, prev + curr
    print(f'斐波那契数列第{n}个元素是：{curr}.')

#递归实现 
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input('请输入你想查看的斐波那契数列元素序号：'))
print(f'斐波那契数列第{n}个元素是：{fibonacci(n)}.')

# 迭代实现
def fibonacci(n):
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

n = int(input('请输入你想查看的斐波那契数列元素序号：'))
print(f'斐波那契数列第{n}个元素是：{fibonacci(n)}.')

# 生成器实现
def fibonacci_gen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input('请输入你想查看的斐波那契数列元素序号：'))
fib = fibonacci_gen()
for _ in range(n-1):
    next(fib)
print(f'斐波那契数列第{n}个元素是：{next(fib)}.')