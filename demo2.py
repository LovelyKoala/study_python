import math

for n in range(100,1000,1):
    # l = int(n /1000 % 10) # 千位
    i = int(n / 100 % 10) # 百位
    j = int(n / 10 % 10) # 十位
    k = n % 10 # 个位数
    if n == math.pow(i,3) + math.pow(j,3) + math.pow(k,3):
        print(n)
# x = math.sin(0)
# print(x)
