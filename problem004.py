#http://projecteuler.net/problem=4

class palindrome :
    def __init__(self) :
        self.i = 9
        self.j = 9
        self.k = 9
        self.limit = 999**2
        self.stop = False

    def get_palindrome(self) :
        return self.i*10**5 + self.j*10**4 + self.k*10**3 + self.k*10**2 + self.j*10 + self.i

    def decrement(self) :
        self.k -= 1
        if self.k < 0 :
            self.k = 9
            self.j -= 1
            if self.j < 0 :
                self.j = 9
                self.i -= 1
                if self.i < 1 :
                    self.stop = True

    def next(self) :
        if self.stop : return None
        r = self.get_palindrome()
        while r > self.limit :
            self.decrement()
            r = self.get_palindrome()
        self.decrement()
        return r
            
def divisible_p(n) :
    for i in range(999,99,-1) :
        if (n % i == 0) : return True, i, n/i
    return False, None, None

def p4():
    p = palindrome()
    r = []
    n = p.next()
    while n :
        test, d1, d2 = divisible_p(n)
        if test and (int(d2/1000) == 0): return n, d1, d2, d1*d2
        n = p.next()
    return None, None, None, None

if __name__ == "__main__" :
    print p4()

