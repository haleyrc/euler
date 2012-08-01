class Memoize:
    def __init__(self, func):
        self.prevs = {}
        self.func = func
    
    def __call__(self, *args):
        if not args in self.prevs:
            self.prevs[args] = self.func(*args)
        return self.prevs[args]

class Timer:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args):
        print "Timer test of function: %s" % self.func.__name__
        from time import time
        start = time()
        ret_val = self.func(*args)
        duration = time() - start
        print "Time elapsed: ", duration
        return ret_val
        
@Memoize
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def iterfib(n):
    if n < 1:
        raise Exception("n must be a number > 0.")
    if n in [1,2]:
        return 1
    ult, penult = 1,1
    for i in range(3,n+1):
        fib = ult + penult
        ult, penult = fib, ult
    return fib
        
@Timer
def run():
    pans = int("".join([str(i) for i in range(1,10)]))
    k, done = 3, False
    ult, penult = 1,1
    while True:
        if not k%10000: 
            print "k = %d"% k
        ult, penult = ult+penult, ult
        firstdigs = int("".join(sorted(str(ult)[:9])))
        lastdigs = int("".join(sorted(str(ult)[-9:])))
        # print firstdigs, lastdigs
        if lastdigs == pans and firstdigs == pans:
            return ult
        else:
            k += 1
            
if __name__ == "__main__":
    print run()
