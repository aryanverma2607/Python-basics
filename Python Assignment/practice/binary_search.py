nums = [5,7,7,8,8,10]
target = 8
l=0
r=len(nums)-1
mid = (l+r)//2
for i in range(len(nums)):
    mid = (l+r)//2
    if nums[mid]==target:
        print(mid)
        break
    if nums[mid] > target:
        r = mid-1
    elif nums[mid]<target:
        l = mid + 1
else:
    print("element not found")
