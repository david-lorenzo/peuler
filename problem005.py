#http://projecteuler.net/problem=5

def decompose(n, r) :
    for i in r.keys() :
        c = 0
        while n % i == 0 :
            n /= i
            c +=1

        if r[i] < c :
           r[i] = c
    if n > 1 :
        r[n] = 1

def p5(n):
    r = dict()
    for i in range(1, n+1) :
        decompose(i, r)

    res = 1
    for i in r.keys():
        res *= i**r[i]

    return res

if __name__ == "__main__" :
    res = p5(20)
    print res
    for i in range(1, 21) :
        print res, " % ", i, " -> ", res % i 

