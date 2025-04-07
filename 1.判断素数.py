number1 = int(input("请输入一个正整数："))
if number1 <= 0:
    print("请输入正整数！")
elif number1 == 1:
    print(number1, '既不是素数也不是合数。')
elif number1 == 2:
    print(number1, '为素数。')
else:
    is_prime = True
    for i in range(2, int(number1**0.5) + 1):
        if number1 % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number1, '为素数。')
    else:
        print(number1, '为合数。')