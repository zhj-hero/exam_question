# 复制列表

# 创建原始列表
list1 = [1,2,3,4,5]
# 打印原始列表及其内存地址
print(list1, id(list1))

# 使用copy()方法创建列表的浅拷贝
list2 = list1.copy()
# 打印拷贝后的列表及其内存地址
print(list2, id(list2))

# 创建一个空列表
list3 = []
# 使用切片赋值方式复制列表
list3[:] = list1
# 打印通过切片复制后的列表及其内存地址
print(list3, id(list3))

# 将list1重新赋值为list3
list1 = list3
# 打印重新赋值后的list1及其内存地址
print(list1, id(list1))