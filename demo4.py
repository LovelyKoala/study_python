# i = 100
# s = str(i)
# sum = s + s
# print(sum)

x = [1,2,3,4]
x[3] = 100
x.append(6)
x.append(6)
for i in x:
    print(i)
# x = range(5)
# for i in x:
#     print(i)
print("#"*100)

x2 = (1,2,3,4)
# x2[0] = 100
for i in x2:
    print(i)

print("#"*100)

x3 = {1,2,3,4}
# x4 = set([1,2,3,4])
x3.add(5)
x3.add(5)
for i in x3:
    print(i)


# print("我的猫")
# print("我","是",'中国人',sep='->')

# s = "100"
# t = 200
# x = int(s)+t
# print(x)

x4 = {"201":"张雨","201":"王武"}
x4["203"]="xxx"
x4["201"]="张雨"
print(x4["201"])