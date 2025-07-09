#w.p.p to print factorial of a number using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
num=5
print("factorial of ",num,"is",fact(num))
