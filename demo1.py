s = float(input("输入购买数量:"))
p = input("输入单价:")
price = float(p)
if s < 6:
    j = 1.0
elif s>=6 and s<=10:
    j=0.9
else:
    j = 0.8
# 总价格 = 数量 * 单价 * 打折值
t = s * price * j
print("总费用为:%.2f"%t,"元")



