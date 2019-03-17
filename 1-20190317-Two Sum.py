def two_sum(nums,target):
    dic={}
    for i in range(len(nums)):
        if target-nums[i] not in dic:
            dic[nums[i]]=i
        else:
            return [dic[target-nums[i]],i]

nums=[1,3,7,16]
target=17

print(two_sum(nums,target))