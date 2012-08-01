from math import sqrt

def is_pentagonal(num):
    if (1+sqrt(1+24*num)) % 6 == 0:
        return True
    else:
        return False

def pentagonal_number(num):
    return ((num * (3*num -1))/2)

'''
def generate_pentagonal():
    num = 1
    while True:
        yield pentagonal_number(num)
        num+=1
'''
'''
def generate_pentagonal(upto):
    num = 1
    count = 1
    while count <= upto:
        yield pentagonal_number(num)
        num+=1
        count += 1
'''

def generate_pentagonal(upto, start=1):
    num=start
    count = 1
    while count <= upto:
        yield pentagonal_number(num)
        num+=1
        count+=1

if __name__ == "__main__":
    pents = [x for x in generate_pentagonal(upto=5000)]

    for pent in generate_pentagonal(upto=5000):
        for rev_pent in generate_pentagonal(upto=5000):
            if is_pentagonal(pent+rev_pent) and is_pentagonal(abs(pent-rev_pent)):
            #if is_pentagonal(pent+rev_pent) and is_pentagonal(abs(pent-rev_pent)):
                print "%s,%s %s" % (pent,rev_pent,str(abs(pent-rev_pent)).rjust(30))
