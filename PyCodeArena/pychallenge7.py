nums = [9, 8, 7, 6]
s = 0
for i in range(1,  len(nums), 2): 
     s += nums[-1] - nums[i] 
print(s)
