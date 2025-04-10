# 输入字符，判断是否为字母。

string=input('请输入字符：')

# 第一种方式，查询是否在a-z的ASCII码范围内
a_ord=ord('a')
z_ord=ord('z')
print(a_ord,z_ord,)
new_str_ord=ord(string.lower())
if new_str_ord in range(a_ord,z_ord+1):
    print(f'{string}是字母')
else:
    print(f'{string}不是字母')

# 蠢了，用if判断是否在a-z的ASCII码范围内就行
if 'a'<=string.lower()<='z':
    print(f'{string}是字母')
else:
    print(f'{string}不是字母')

# 第二种方式，直接调用str.isalpha()方法
if string.isalpha():
    print(f'{string}是字母')
else:
    print(f'{string}不是字母')