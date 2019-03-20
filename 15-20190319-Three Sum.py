def threeSum(nums):
    res=[]
    nums.sort()
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            numSum=nums[i]+nums[l]+nums[r]
            if numSum>0:
                r=r-1
            elif numSum<0:
                l=l+1
            else:
                res.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l=l+1
                while l<r and nums[r]==nums[r-1]:
                    r=r-1
                l=l+1
                r=r-1
    return res

nums=[-1,0,1,2,-1,-4]

print(threeSum(nums))

def threeSumtwo(nums):
    nums.sort()
    res=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            threesum=nums[i]+nums[l]+nums[r]
            if threesum<0:
                l=l+1
            elif threesum>0:
                r=r-1
            else:
                res.append([nums[i],nums[l],nums[r]])
                while l<r and nums[r]==nums[r-1]:
                    r=r-1
                while l<r and nums[l]==nums[l+1]:
                    l=l+1
                r=r-1
                l=l+1
    return res
print(threeSumtwo(nums))