# 输入一行字符，分别统计其中英文字母、空格、数字和其他字符个数
string = input('请输入字符串：')
str_number = 0
digt_number = 0
other = 0
space_number = 0
# 统计英文字母、空格、数字和其他字符个数
for i in string:
    if "a" <= i <= "z" or "A" <= i <= "Z":  # 判断是否为英文字母(if i.isalpha())
        str_number += 1  
    elif "0" <= i <= "9":  # 判断是否为数字(if i.iadigit())
        digt_number += 1
    elif i.isspace():  # 判断是否为空格
        space_number += 1
    else:  # 其他字符
        other += 1

print(f'其中英文字母、空格、数字和其他字符个数分别为{str_number},{space_number},{digt_number},{other}.')

