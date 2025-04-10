# 比较三个数大小
number1,number2,number3=float(input('请输入第一个数')),float(input('请输入第二个数')),float(input('请输入第三个数'))

# 使用sorted函数对列表进行排序，reverse=True表示降序排序
lst=[number1,number2,number3]
list=sorted(lst,reverse=True)
print('三个数从大到小依次为：',list)

# 使用冒泡排序对列表进行排序
n=len(lst)
for i in range(n-1):
    for j in range(n-i-1):
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print('三个数从大到小依次为：',lst)