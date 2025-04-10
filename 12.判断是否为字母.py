# 输入字符，判断是否为字母。

string=input('请输入字符：')
a_ord=ord('a')
z_ord=ord('z')
print(a_ord,z_ord,)
new_str_ord=ord(string.lower())
if new_str_ord in range(a_ord,z_ord+1):
    print(f'{string}是字母')
else:
    print(f'{string}不是字母')