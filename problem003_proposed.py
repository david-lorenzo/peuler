#http://projecteuler.net/problem=3

from math import sqrt

def eliminate_factor(n, m) :
    while (n % m == 0) : n /= m
    return n

def p3_proposed(n):

    if n % 2 == 0 :
        last_factor = 2
        n = eliminate_factor(n, 2)
    else :
        last_factor = 1

    max_factor = int(sqrt(n))
    factor = 3

    counter = 0
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n = eliminate_factor(n, factor)
            last_factor = factor
            max_factor = int(sqrt(n))
        factor += 2
        counter +=1

    if n == 1 : return last_factor, counter
    else : return n, counter

if __name__ == "__main__" :
    print p3_proposed(600851475143)

