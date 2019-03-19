def letterCombine(s):
    mapping={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    if len(s)==0:
        return []
    if len(s)==1:
        return list(mapping[s[0]])
    prev=letterCombine(s[:-1])
    addtion=list(mapping[s[-1]])
    return [s+c for s in prev for c in addtion]


print(letterCombine('23'))
