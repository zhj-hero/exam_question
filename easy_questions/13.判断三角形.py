# 编写程序，输入三组数据，判断能否构成三角形的三条边。

# 原版，未考虑负数以及非数字类型的输入
# def triangle(side1,side2,side3):
#     trian=[side1,side2,side3]
#     trian.sort()
#     if trian[0]+trian[1]>trian[2] and trian[2]-trian[0]<trian[1]:
#         return(True)
    
# nums=input(f'请输入三组数据：')
# tri_nums=nums.split(' ')
# if  triangle(int(tri_nums[0]),int(tri_nums[2]),int(tri_nums[1])):
#     print(f'{nums}能构成三角形')
# else:
#     print(f'{nums}不能构成三角形')


# AI重构版，考虑负数以及非数字类型的输入
def triangle(side1, side2, side3):
    # 先检查所有边是否为正数
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
    
    trian = [side1, side2, side3]
    trian.sort()
    # 三角形两边之和大于第三边
    return trian[0] + trian[1] > trian[2]

nums = input('请输入三组数据（用空格分隔）：')
try:
    tri_nums = list(map(float, nums.split()))  # 转换为浮点数更通用
    if len(tri_nums) != 3:
        print('请输入三个数字')
    elif triangle(tri_nums[0], tri_nums[1], tri_nums[2]):
        print(f'{nums}能构成三角形')
    else:
        print(f'{nums}不能构成三角形')
except ValueError:
    print('请输入有效的数字')