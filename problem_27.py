from rabin import *
import threading

max_count = 0
max_prod = 0

class LockedIterator(object):
    def __init__(self, it):
        self.lock = threading.Lock()
        self.it = it.__iter__()

    def __iter__(self): return self

    def next(self):
        self.lock.acquire()
        try:
            return self.it.next()
        finally:
            self.lock.release()

class FunctionTest(threading.Thread):
    def __init__(self, it):
        threading.Thread.__init__(self)
        self.it = it

    def run(self):
        global max_count
        global max_prod
        while True:
            (a,b) = self.it.next()
            n = 0
            while isprime_MR(f(n,a,b)):
                n += 1
            if n > max_count:
                max_count = n
                print "New max: %s" % max_count
                max_prod = a*b

def f(n, a, b):
    return n**2 + a*n + b

if __name__ == "__main__":

    gen = [(a,b) for b in range(-999, 1000) for a in range(-999, 1000)]
    locked_iterator = LockedIterator(gen)

    threads = []
    for i in range(4):
        t = FunctionTest(locked_iterator)
        t.setDaemon(True)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print "Maximum product of a and b: %s" % max_prod
