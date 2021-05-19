import time
def sumfn3(n):
    start=time.time()
    thesum=(n*(n+1))/2
    end=time.time()
    print( thesum, end-start)
sumfn3(50)
