# 编写程序，输入一个四位整数，反向输出对应四位数。
fourbit_number=input('请输入一个四位整数：')
reverse_number=int(fourbit_number[::-1])
print(f'{fourbit_number}的反向四位数是{reverse_number}')