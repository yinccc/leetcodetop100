def  contain(nums):
    l,r,width,area=0,len(nums)-1,len(nums)-1,0
    for w in range(width,0,-1):
        if nums[l]<nums[r]:
            area,l=max(area,w*nums[l]),l+1
        else:
            area,r=max(area,w*nums[r]),r-1
    return area

nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(contain(nums))
