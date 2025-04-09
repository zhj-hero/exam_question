# 打印乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        k=i*j
        print('{i}*{j}={k} '.format(i=i,j=j,k=k),end='')
    print()
