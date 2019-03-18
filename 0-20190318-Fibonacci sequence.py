from time import time
def Fibonacci(n):
    if n<=0:
        return False
    elif n<=2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

time1=time()
print(Fibonacci(30))
time2=time()
print(time2-time1)

def FibonacciDP(n):
    f={}
    for i in range(1,n+1):
        if i<=2:
            f[i]=1
        else:
            f[i]=f[i-1]+f[i-2]
    return f[n]
time1=time()
print(FibonacciDP(30))
time2=time()
print(time2-time1)
