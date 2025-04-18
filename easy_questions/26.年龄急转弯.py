# 有5个人坐在一起,问第五个人多少岁?他 说比第4个人大2岁。问第4个人岁数,他说 比第3个人大2岁。问第三个人,又说比第2 人大两岁。问第2个人,说比第一个人大两 岁。最后问第一个人,他说是10岁。请问第 五个人多大?

# 普通迭代
age = 10
for i in range(2, 6):
    age += 2
print(f'第{i}个人{age}岁')

# 递归实现
def cal_age(n):
    if n == 1:
        return 10
    else:
        return cal_age(n-1)+2
print(f'第5个人{cal_age(5)}岁')