#300 Longest increasing substring
class Solution300:
    def LIS(self,nums):
        if len(nums)==0:
            return  0
        dp=[1]*len(nums)
        maxlen=1
        for i in range(1,len(nums)):
            templen=0
            for j in range(i):
                if nums[i]>nums[j]:
                    templen=max(templen,dp[j])
            dp[i]=templen+1
            maxlen=max(maxlen,dp[i])
        return maxlen

#001 two sum
class Soluntion001:
    def twoSum(self,nums,target):
        dic={}
        for i in range(len(nums)):
            if target-nums[i] not in dic:
                dic[nums[i]]=i
            else:
                return [dic[target-nums[i]],i]

#002 Add Two Numbers
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution002:
    def AddTwoNumbers(self,l1,l2):
        head=root=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            v1=v2=0
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
            carry,val=divmod(v1+v2+val,10)
            head.next=ListNode(val)
            head=head.next
        return root.next

#003 Longest SubString without repeating characters
class Solution003:
    def longestSubStringwithoutrepeatingcharacters(self,string):
        max_len=0
        cur=""
        for i in string:
            if i in cur:
                cur=cur[cur.index(i)+1:]+i
            else:
                cur=cur+i
            max_len=max(max_len,len(cur))
        return max_len