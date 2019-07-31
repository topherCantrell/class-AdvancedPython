from math import sqrt; from itertools import count, islice
def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def get_primes_old_rusted(start,end):
    ret = []
    for n in range(start,end):
        if is_prime(n):
            print('OLD:found one')
            ret.append(n)
    print('OLD:DONE')
    return ret

def get_primes_new_hot(start,end):
    for n in range(start,end):
        if is_prime(n):
            print('NEW:found one')
            yield n
    print('NEW:DONE')

#for n in get_primes_old_rusted(2,100):
#    print(n)

# in the command line, call __iter__ and __next__ on each