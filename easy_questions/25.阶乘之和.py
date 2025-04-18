# 求1+2!+3!+4!+.....+20!

import math
sum = 0
for n in range(1, 21):
    sum += math.factorial(n)
print(f'1+2!+3!+4!+.....+20!={sum}')