#17 letter combination
class Solution017:
    def letterCombination(self,s):
        mapping={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(s)==0:
            return []
        if len(s)==1:
            return list(mapping[s[0]])
        prev=self.letterCombination(s[:-1])
        addition=list(mapping[s[-1]])
        return [s+c for s in prev for c in addition]


#19 romve kth node from list
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution019:
    def remove(self,head,n):
        dummy=ListNode(0)
        dummy.next=head
        first=head
        length=0
        while first!=None:
            length=length+1
            first=first.next
        length=length-n
        first=dummy
        while length>0:
            length=length-1
            first=first.next
        first.next=first.next.next
        return dummy.next


#20 valid ([{
class Solution020:
        def valid(self,s):
            stack=[]
            for p in s:
                if p in '{[(':
                    stack.append(p)
                else:
                    if not stack:
                        return False
                    elif p==")" and stack.pop()!="(":
                        return False
                    elif p=="]" and stack.pop()!="[":
                        return False
                    elif p=="}" and stack.pop()!="{":
                        return False
            return (stack==[])

#322 coins change
class Solution322:
    def coinsChange(self,coins,amount):
        maxNums=amount+1
        dp=[maxNums]*maxNums
        dp[0]=0
        for i in range(1,maxNums):
            for j in range(len(coins)):
                if coins[j]<=i:
                    dp[i]=min(dp[i],dp[i-coins[j]]+1)
        return -1 if dp[amount]>amount else dp[amount]