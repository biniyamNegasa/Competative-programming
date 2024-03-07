def bs(arr, target):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]<=target:
            left = mid+1
        else:
            right = mid-1
    return left
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
for _ in range(int(input())):
    val = int(input())
    print(bs(nums,val))