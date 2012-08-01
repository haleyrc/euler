import random
from fractions import gcd
import rabin
import sys
from collections import defaultdict

def f(x,c,n):
    return (x**2 + c) % n

def pollard_rho(num, c=1):
    if rabin.isprime_MR(num):
        return None
    x = random.randint(1, num-1)
    y = f(x,c,num)
    d = 1
    while d == 1:
        d = gcd(abs(x-y), num)
        if d == num:
            c = c+1
            return pollard_rho(num,c)
        x = f(x,c,num)
        y = f(f(y,c,num),c,num)
    return d


def factor(num):
    factors = _do_factor(num)
    return factors

def prime_factors(num):
    factors = [x for x in factor(num) if rabin.isprime_MR(x)]
    d = defaultdict(int)
    for fact in factors:
        d[fact] += 1
    return d

def _do_factor(num):
    facs = [num]
    a_factor = pollard_rho(num)
    if a_factor and a_factor != num:
        facs = facs + _do_factor(a_factor) + _do_factor(num/a_factor)
    return facs

def count_divisors(num):
    return _do_count_divisors(prime_factors(num))

def _do_count_divisors(d):
    count = 1
    for i in range(0,len(d.keys())):
        count = count * (d.items()[i][1] + 1)
    return count

def triangle_number(num):
    return sum(range(1,num+1))

if __name__ == "__main__":
    '''
    i = 1000000
    while True:
        if count_divisors(triangle_number(i)) > 500:
            print triangle_number(i)
            break
        else:
            i = i+1
    '''
    print prime_factors(99999999999999999999999999999999999999999999999999999999)

