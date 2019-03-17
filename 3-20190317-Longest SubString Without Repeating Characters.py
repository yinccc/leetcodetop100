def longsubwithoutRC(s):
    max_len=0
    cur=''
    for item in s:
        if item in cur:
            cur=cur[cur.index(item)+1:]+item
        else:
            cur=cur+item
        max_len=max(len(cur),max_len)
    return max_len

s='abcaaacddefg'
print(longsubwithoutRC(s))
