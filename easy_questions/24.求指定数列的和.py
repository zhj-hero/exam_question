# 有一份数列：2/1, 3/2, 5/3, 8/5, 13/8.....求这个数列前20项之和

sum = 0
fenzi = 2
fenmu = 1
for n in range(1,21):
    sum += fenzi / fenmu
    fenzi, fenmu = fenzi + fenmu, fenzi
print(f'此数列前20项之和为：{sum:.2f}')