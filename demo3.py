even_sum = 0
odd_sum = 0
for num in range(1 , 1001):
    if num % 2 == 0:
        #偶数
        even_sum+=num
    if num % 2 == 1:
        odd_sum = odd_sum + num
print("偶数的和=%d"%even_sum)
print("奇数的和=%d"%odd_sum)