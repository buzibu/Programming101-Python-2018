#Sum of all digits of a number

def sum_of_digits(n):
    return sum([int(x) for x in list(str(abs(n)))])

#Turn a number into a list of digits

def to_digits(n):
    return [int(x) for x in list(str(n))]

#Turn a list of digits into a number

def to_number(digits):
    return int(''.join([str(x) for x in digits]))

#Factorial Digits

def fact_digits(n):
    import math
    return sum([math.factorial(int(x)) for x in list(str(n))])

#First nth members of Fibonacci

def fibonacci(n):
    n = abs(n)
    def fib(x):
        if x == 0:
            return 1
        elif x == 1:
            return 1
        else:
            return fib(x - 1) + fib(x - 2)
    return [fib(a) for a in range(0,n)]

#Fibonacci number

def fib_number(n):
    n = abs(n)
    def fib(x):
        if x == 0:
            return 1
        elif x == 1:
            return 1
        else:
            return fib(x - 1) + fib(x - 2)
    return int(''.join([str(fib(a)) for a in range(0,n)]))

#Palindrome

def palindrome(n):
    
