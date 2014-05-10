#http://projecteuler.net/problem=3

# if q = int(sqrt(n)) then there is no number p that is p > q and n % p = 0
# with that premise we will try numbers from i = int(sqrt(n)) to 1 and return the first i found that makes n % i = 0
# that i number has to be a prime number
# another interesting premise from http://es.wikipedia.org/wiki/Numeros_primos#Otras_propiedades -> all primes numbers are of the form 6*n + 1 or 6*n - 1 for all primes > 3
# so instead of trying any number we only try prime numbers

from math import sqrt

def give_me_possible_primes(n) :
    return (6*n+1, 6*n-1)

def eliminate_factor(n, m) :
    nn = n
    while (n % m == 0) :
        n /= m
    return (n, not (nn == n))

def p3b(n):
    factors = []

    n, factor_p = eliminate_factor(n, 2)
    if factor_p : factors.append(2)

    n, factor_p = eliminate_factor(n, 3)
    if factor_p : factors.append(3)

    limit = int(sqrt(n))
    i = 1
    while True:
        upper, lower = give_me_possible_primes(i)

        (n, factor_p) = eliminate_factor(n, lower)
        if factor_p : factors.append(lower)
        if lower > int(sqrt(n)) : break

        (n, factor_p) = eliminate_factor(n, upper)
        if factor_p : factors.append(upper)
        if upper > int(sqrt(n)) : break

        if n == 1 : break
        i += 1

    if n > 1 :
        factors.append(n)

    return max(factors), factors, i
        


if __name__ == "__main__" :
    print p3b(600851475143)

