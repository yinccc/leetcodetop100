#5 palindromic
class Solution005:
    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l=l-1
            r=r+1
        return s[l+1:r]
    def palidromic(self,s):
        res=''
        for i in range(len(s)):
            #odd case
            temp=self.helper(s,i,i)
            if len(temp)>len(res):
                res=temp

            #even case
            temp=self.helper(s,i,i+1)
            if len(temp)>len(res):
                res=temp

        return res


#11 most water
class Solution011:
    def mostwater(self,height):
        L,R,width,res=0,len(height)-1,len(height)-1,0
        for i in range(width,0,-1):
            if height[L]<height[R]:
                res,L=max(res,i*height[L]),L+1
            else:
                res,R=max(res,i*height[R]),R-1
        return res


#11 threesum
class Solution015:
    def threeSum(self,nums):
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            if nums[i]==nums[i-1]:
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
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l=l+1
                    while l<r and nums[r]==nums[r-1]:
                        r=r-1
                    l=l+1
                    r=r-1
        return ans

#309
class Solution305:
    def maxprofit(self,prices):
        hold,sold,rest=float("-inf"),0,0
        for p in prices:
            hold,sold,rest=max(hold,rest-p),hold+p,max(rest,sold)
        return max(sold,rest)