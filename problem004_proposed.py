#http://projecteuler.net/problem=4

def reverse(n) :
    reverse = 0
    while n>0 :
        reverse = reverse*10 + (n%10)
        n = int(n/10)
    return reverse
    
def palindrome_p(n) :
    return (n == reverse(n))
    
def p4():
    iterations = 0
    largest = 0
    a = 999
    while a >=100:
        if (a % 11 == 0) :
            b = 999
            db = 1
        else :
            b = 990
            db = 11

        while b >= a:
            iterations += 1
            if (a*b <= largest): break
            if palindrome_p(a*b) :
                largest = a*b
            b = b - db
        a = a -1
    return (largest, iterations)


if __name__ == "__main__" :
    print p4()

