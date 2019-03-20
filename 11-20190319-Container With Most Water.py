def contain(nums):
    L, R, width, res = 0, len(nums) - 1, len(nums) - 1, 0
    for w in range(width, 0, -1):
        if nums[L] < nums[R]:
            res, L = max(res, w * nums[L]), L + 1
        else:
            res, R = max(res, w * nums[R]), R - 1
    return res


nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(contain(nums))


def maxArea(height):
    L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
    for w in range(width, 0, -1):
        if height[L] < height[R]:
            res, L = max(res, height[L] * w), L + 1
        else:
            res, R = max(res, height[R] * w), R - 1
    return res


print(maxArea(nums))


def Containwatertwo(nums):
    L,R,width,res=0,len(nums)-1,len(nums)-1,0
    for w in range(width,0,-1):
        if nums[L]<nums[R]:
            res,L=max(res,nums[L]*w),L+1
        else:
            res,R=max(res,nums[R]*w),R-1
    return res

print(Containwatertwo(nums))
