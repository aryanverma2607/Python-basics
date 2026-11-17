arr = [1,2,3,4,5,6]
# l=0
# r=len(arr) - 1
# while r>=l:
#     arr[l],arr[r] = arr[r],arr[l]
#     r-=1
#     l+=1
# print(arr)
l=0
target = 5
r=len(arr) - 1
mid = (l+r)//2
while r>=l:
    if arr[mid]<target:
        l =mid+1
    elif arr[mid]>target:
        r=mid-1
    else:
        print(mid)
        break
    mid = (l+r)//2