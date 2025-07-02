#recursion mean it call  function itself
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
