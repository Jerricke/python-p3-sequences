#!/usr/bin/env python3

def print_fibonacci(length):
    fib = [] #[0, 1, 1, 2]
    for n in range(length):
        try: 
            prevN = fib[n - 1] #fib[3 - 1] => 1
        except IndexError:
            prevN = n
        try:
            prevN2 = fib[n - 2]
            if n == 1: 
                raise IndexError("-1")
        except IndexError:
            prevN2 = n
        fib.append(prevN + prevN2)
    print(fib)

print_fibonacci(5)