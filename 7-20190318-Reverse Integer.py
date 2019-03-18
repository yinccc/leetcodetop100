def reverse(n):
    tag=1
    if n<0:
        tag=-1
    else:
        tag=1
    reverse=str(abs(n))[::-1]
    reverse_n=int(reverse)
    if reverse_n<=-pow(2,31) or reverse_n>=pow(2,31):
        return 0
    return int(reverse_n)*tag

print(reverse(123))
print(reverse(-1234567))