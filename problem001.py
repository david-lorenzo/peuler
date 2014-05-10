#Problem 1
#http://projecteuler.net/problem=1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

def p1(n) :
    # simple version, bad performance O(n)
    n -=1
    result = 0
    while n>0 :
        if n%5==0 or n%3==0 :
            result += n
        n -= 1

    return result

def euler(n) :
    if (n%2 == 0) :
        return (n/2)*(n+1)
    else :
        return (n + ((n-1)/2)*n)

def p1_better(n) :
    # better version, better performance O(1)
    n -=1
    # res = multiples(3) + multiples(5) - multiples(3*5)
    # multiples(3)   = sum for m1=1, floor((n-1)/3)  of 3*m1
    # multiples(5)   = sum for m2=1, floor((n-1)/5)  of 5*m2
    # multiples(3*5) = sum for m3=1, floor((n-1)/15) of 15*m3
    # Euler told us that sum for n=1,100 is (100/2)*(100+1)
    # we do the same with each series of multiples

    return 3*euler(int(n/3)) + 5*euler(int(n/5)) - 15*euler(int(n/15))

if __name__ == "__main__" :
    print p1(1000)
    print p1_better(1000)

