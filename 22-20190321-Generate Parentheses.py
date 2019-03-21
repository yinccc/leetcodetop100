def GenerateParentheses(n):
    res=[]
    def backtrack(s="",right=0,left=0):
        if len(s)==2*n:
            res.append(s)
        if left<n:
            backtrack(s+"(",right,left+1)
        if right<left:
            backtrack(s+")",right+1,left)
    backtrack()
    return res

print(GenerateParentheses(3))
