#Problem 2
#http://projecteuler.net/problem=2


def p2(max_value) :
    fn1 = 2 # fibonacci number n-1, initialized as f(2)
    fn2 = 1 # fibonacci number n-2, initialized as f(1)
    n = 3 # not needed
    result = fn1 # initial value of the sum of even numbers in the fib series

    while True :
        fn = fn1 + fn2
        if fn > max_value : break

        if fn % 2 == 0 : result += fn
        # setting variables for the next iteration
        n = n + 1
        fn2 = fn1
        fn1 = fn
    return (result, n)

if __name__ == "__main__" :
    print p2(4000000)

