#4. insert position


n=int(input("Enter size of list: "))
nums=[]

for i in range(n):
    a=int(input("Enter elment: "))
    nums.append(a)

for i in nums:
    if i>=target:
       print(nums.index(i))
       break
else:
    m=max(nums)  
    print(nums.index(m)+1)