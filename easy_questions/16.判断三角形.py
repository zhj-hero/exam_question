# 编写程序，输入三组数据，判断能否构成三角形的三条边。

def triangle(side1,side2,side3):
    trian=[side1,side2,side3]
    trian.sort()
    if trian[0]+trian[1]>trian[2] and trian[2]-trian[0]<trian[1]:
        return(True)
    
nums=input(f'请输入三组数据：')
tri_nums=nums.split(' ')
if  triangle(int(tri_nums[0]),int(tri_nums[2]),int(tri_nums[1])):
    print(f'{nums}能构成三角形')
else:
    print(f'{nums}不能构成三角形')