def zigzag(s,numsrow):
    if numsrow==1 or numsrow>len(s):
        return s

    row=['']*numsrow
    index,step=0,1
    for x in s:
        row[index]+=x
        if index==0:
            step=1
        elif index==numsrow-1:
            step=-1
        index+=step
    return "".join(row)

print(zigzag('PAYPALISHIRING',3))